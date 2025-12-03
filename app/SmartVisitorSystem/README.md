# Smart Visitor Monitoring System

Smart Visitor Monitoring System for CHRIST University, Pune Lavasa Campus.

## Features

- Tkinter-based GUI for visitor registration.
- Capture visitor image from webcam or upload PNG.
- Face detection and basic preprocessing using OpenCV and Pillow.
- Visitor details and image path stored in an Excel workbook.
- Suspicious entry detection when the same visitor (name + phone) appears again on the same day.
- Suspicious entries highlighted in yellow in Excel and logged to `data/repeated_entries.log`.

## Project Structure

- `main.py`: Application entry point.
- `gui/visitor_form.py`: Tkinter GUI and main application logic.
- `core/validator.py`: Input validation (regex for email, phone, non-empty fields).
- `core/face_capture.py`: Webcam capture logic.
- `core/face_processing.py`: Image preprocessing and face detection.
- `core/excel_manager.py`: Excel file management using OpenPyXL.
- `core/alert_manager.py`: Suspicious entry alerting and logging.
- `data/visitor_log.xlsx`: Excel log (auto-created on first run).
- `data/repeated_entries.log`: Log of repeated entries.
- `data/visitor_images/`: Stored PNG images.

## Setup

From the `SmartVisitorSystem` directory, create a virtual environment (optional) and install dependencies:

```bash
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
```

## Running the Application

From the `SmartVisitorSystem` directory:

```bash
python main.py
```

## Face Verification Logic

Uploaded or captured images are resized, converted to grayscale, smoothed using Gaussian blur, and passed through OpenCV's Haar Cascade face detector. If no face is detected, the image is rejected and the user is prompted to try again.

## Excel Update & Highlight Logic

Visitor records are appended to `data/visitor_log.xlsx` with columns:

`VisitorID | Name | Phone | Email | Purpose | ImagePath | Timestamp | Status`

If suspicious entries (same name + phone on the same day) are detected, the existing matching rows are highlighted in yellow using OpenPyXL's `PatternFill`. Column widths are auto-adjusted to fit content.

## Suspicious Entry Detection

Before appending a new record, the Excel file is scanned for rows where both `Name` and `Phone` match the current visitor and the date portion of `Timestamp` equals today's date (IST). If matches are found, status is set to `SUSPICIOUS`, existing matching rows are highlighted, and a warning popup is shown. A log entry is also appended to `data/repeated_entries.log`.

## Demo Scenario

1. Run the application.
2. Enter visitor details (name, 10-digit phone, valid email, purpose).
3. Click **Capture Image** to take a picture via webcam, or **Upload Image** to select an existing PNG.
4. Click **Submit**. If a face is detected, the record is stored in Excel, and a visitor ID is displayed.
5. Repeat steps 2-4 with the same name and phone number on the same day. A suspicious entry popup appears, and matching rows in Excel are highlighted.
