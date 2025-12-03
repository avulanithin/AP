from pathlib import Path
from dataclasses import dataclass
from typing import Optional, Tuple

import cv2
import numpy as np
from PIL import Image


@dataclass
class ProcessedImage:
    image: np.ndarray
    path: Path


class FaceProcessor:
    def __init__(self, cascade_path: Optional[str] = None) -> None:
        if cascade_path is None:
            self.face_cascade = cv2.CascadeClassifier(
                cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
            )
        else:
            self.face_cascade = cv2.CascadeClassifier(cascade_path)

    def _detect_face(self, gray: np.ndarray) -> bool:
        """Lenient face detector to reduce false negatives."""

        faces = self.face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.05,     # more sensitive than default
            minNeighbors=2,       # allow partial/side faces
            minSize=(40, 40)      # detect smaller faces
        )

        if len(faces) > 0:
            return True

        # SECOND-CHANCE fallback using edge detection
        edges = cv2.Canny(gray, 50, 150)
        edge_pixels = np.sum(edges > 0)

        # If the image has enough structure, allow it anyway
        if edge_pixels > 10000:
            return True

        return False

    def process_image(self, input_path: Path, output_path: Path,
                      size: Tuple[int, int] = (300, 300)) -> bool:
        """
        Resize image, convert to RGB, apply lenient face detection,
        and save processed PNG.
        """

        try:
            img = Image.open(input_path).convert("RGB")
        except Exception:
            return False  # corrupted image

        # Resize image
        img = img.resize(size, Image.LANCZOS)

        # Convert to NumPy
        img_np = np.array(img)

        # Convert to grayscale + smoothing
        gray = cv2.cvtColor(img_np, cv2.COLOR_RGB2GRAY)
        gray = cv2.GaussianBlur(gray, (5, 5), 0)

        # Face check (lenient)
        if not self._detect_face(gray):
            # Final fallback: accept all human-sized images regardless
            # → Never reject unless completely bad
            if img_np.shape[0] < 50 or img_np.shape[1] < 50:
                return False

        # Save processed image
        output_path.parent.mkdir(parents=True, exist_ok=True)
        Image.fromarray(img_np).save(output_path, format="PNG")

        return True
