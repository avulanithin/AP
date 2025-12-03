from __future__ import annotations

import logging
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Optional

import tkinter as tk
from tkinter import filedialog, messagebox

from core.validator import InputValidator
from core.face_capture import FaceCapture
from core.face_processing import FaceProcessor
from core.excel_manager import ExcelManager, VisitorRecord
from core.alert_manager import AlertManager, SuspiciousAlert


IST = timezone(timedelta(hours=5, minutes=30))

logger = logging.getLogger(__name__)


class VisitorApp:
    def __init__(self) -> None:
        base_dir = Path(__file__).resolve().parent.parent
        data_dir = base_dir / "data"
        self.images_dir = data_dir / "visitor_images"
        self.log_file = data_dir / "repeated_entries.log"
        self.excel_file = data_dir / "visitor_log.xlsx"

        self.validator = InputValidator()
        self.face_capture = FaceCapture(self.images_dir)
        self.face_processor = FaceProcessor()
        self.excel_manager = ExcelManager(self.excel_file)
        self.alert_manager = AlertManager(self.log_file)

        self.root = tk.Tk()
        self.root.title("Smart Visitor Monitoring System - CHRIST University Pune Lavasa")

        self._build_ui()

        self.selected_image_path: Optional[Path] = None

    def _build_ui(self) -> None:
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack(fill=tk.BOTH, expand=True)

        tk.Label(frame, text="Full Name:").grid(row=0, column=0, sticky="e", pady=5)
        self.name_entry = tk.Entry(frame, width=40)
        self.name_entry.grid(row=0, column=1, pady=5, sticky="w")

        tk.Label(frame, text="Phone Number:").grid(row=1, column=0, sticky="e", pady=5)
        self.phone_entry = tk.Entry(frame, width=40)
        self.phone_entry.grid(row=1, column=1, pady=5, sticky="w")

        tk.Label(frame, text="Email ID:").grid(row=2, column=0, sticky="e", pady=5)
        self.email_entry = tk.Entry(frame, width=40)
        self.email_entry.grid(row=2, column=1, pady=5, sticky="w")

        tk.Label(frame, text="Purpose of Visit:").grid(row=3, column=0, sticky="e", pady=5)
        self.purpose_entry = tk.Entry(frame, width=40)
        self.purpose_entry.grid(row=3, column=1, pady=5, sticky="w")

        img_frame = tk.Frame(frame)
        img_frame.grid(row=4, column=0, columnspan=2, pady=15)

        tk.Button(img_frame, text="Capture Image", command=self.capture_image).pack(side=tk.LEFT, padx=10)
        tk.Button(img_frame, text="Upload Image", command=self.upload_image).pack(side=tk.LEFT, padx=10)

        self.image_label = tk.Label(frame, text="No image selected", fg="gray")
        self.image_label.grid(row=5, column=0, columnspan=2, pady=5)

        submit_btn = tk.Button(frame, text="Submit", command=self.submit_form, width=20, bg="#4CAF50", fg="white")
        submit_btn.grid(row=6, column=0, columnspan=2, pady=20)

    def capture_image(self) -> None:
        name = self.name_entry.get().strip() or "visitor"
        result = self.face_capture.capture_from_webcam(name)
        if not result.success or result.image_path is None:
            messagebox.showerror("Capture Error", result.message)
            return

        self.selected_image_path = result.image_path
        self.image_label.config(text=f"Selected: {self.selected_image_path.name}")

    def upload_image(self) -> None:
        file_path = filedialog.askopenfilename(
            title="Select Visitor Image",
            filetypes=[("PNG Images", "*.png")],
        )
        if not file_path:
            return

        self.selected_image_path = Path(file_path)
        self.image_label.config(text=f"Selected: {self.selected_image_path.name}")

    def submit_form(self) -> None:
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()
        purpose = self.purpose_entry.get().strip()

        validation = self.validator.validate(name, phone, email, purpose)
        if not validation.is_valid:
            messagebox.showerror("Validation Error", validation.message)
            return

        if self.selected_image_path is None:
            messagebox.showerror("Image Required", "Please capture or upload an image.")
            return

        timestamp = datetime.now(IST).strftime("%Y-%m-%d %H:%M:%S")
        safe_name = name.replace(" ", "_") or "visitor"
        filename = f"{safe_name}_{datetime.now(IST).strftime('%Y%m%d_%H%M%S')}.png"
        final_image_path = self.images_dir / filename

        ok = self.face_processor.process_image(self.selected_image_path, final_image_path)
        if not ok:
            messagebox.showerror("Face Detection Failed", "No face detected in the selected image.")
            return

        visitor_id = self.excel_manager.generate_visitor_id()
        suspicious, rows = self.excel_manager.check_suspicious(name, phone)

        status = "SUSPICIOUS" if suspicious else "NORMAL"

        record = VisitorRecord(
            visitor_id=visitor_id,
            name=name,
            phone=phone,
            email=email,
            purpose=purpose,
            image_path=str(final_image_path),
            timestamp=timestamp,
            status=status,
        )

        self.excel_manager.append_record(record, rows if suspicious else [])

        if suspicious:
            alert = SuspiciousAlert(name=name, phone=phone, timestamp=timestamp, rows=rows)
            self.alert_manager.log_and_alert(alert)

        messagebox.showinfo(
            "Registration Successful",
            f"Visitor registered successfully!\n\nVisitor ID: {visitor_id}",
        )

        self._reset_form()

    def _reset_form(self) -> None:
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.purpose_entry.delete(0, tk.END)
        self.selected_image_path = None
        self.image_label.config(text="No image selected")

    def run(self) -> None:
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        )
        self.root.mainloop()
