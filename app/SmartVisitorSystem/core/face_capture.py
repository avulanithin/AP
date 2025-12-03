from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Optional

import cv2
from PIL import Image

IST = timezone(timedelta(hours=5, minutes=30))


@dataclass
class CaptureResult:
    success: bool
    image_path: Optional[Path]
    message: str = ""


class FaceCapture:
    def __init__(self, save_dir: Path) -> None:
        self.save_dir = save_dir
        self.save_dir.mkdir(parents=True, exist_ok=True)

        # Haar cascade for face preview
        self.cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        )

    def capture_from_webcam(self, visitor_name: str) -> CaptureResult:
        """Show live webcam preview. Press SPACE to capture, ESC to cancel."""
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            return CaptureResult(False, None, "Unable to open webcam.")

        captured_frame = None

        while True:
            ret, frame = cap.read()
            if not ret:
                continue

            # Draw face rectangles for preview
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.cascade.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h),
                              (0, 255, 0), 2)

            cv2.putText(frame,
                        "Press SPACE to capture, ESC to cancel",
                        (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7, (255, 255, 255), 2)

            cv2.imshow("Camera Preview - Smart Visitor Monitoring System", frame)

            key = cv2.waitKey(1)

            if key == 27:  # ESC key → cancel
                cap.release()
                cv2.destroyAllWindows()
                return CaptureResult(False, None, "Capture cancelled.")

            if key == 32:  # SPACE key → capture
                captured_frame = frame
                break

        cap.release()
        cv2.destroyAllWindows()

        if captured_frame is None:
            return CaptureResult(False, None, "Failed to capture image.")

        # Save image with timestamp
        timestamp = datetime.now(IST).strftime("%Y%m%d_%H%M%S")
        safe_name = visitor_name.strip().replace(" ", "_") or "visitor"
        filename = f"{safe_name}_{timestamp}.png"
        img_path = self.save_dir / filename

        # Convert BGR → RGB for PIL saving
        rgb = cv2.cvtColor(captured_frame, cv2.COLOR_BGR2RGB)
        Image.fromarray(rgb).save(img_path, format="PNG")

        return CaptureResult(True, img_path, "Image captured successfully.")
