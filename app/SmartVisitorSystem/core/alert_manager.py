import logging
from dataclasses import dataclass
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import List

from tkinter import messagebox

IST = timezone(timedelta(hours=5, minutes=30))

logger = logging.getLogger(__name__)


@dataclass
class SuspiciousAlert:
    name: str
    phone: str
    timestamp: str
    rows: List[int]


class AlertManager:
    def __init__(self, log_path: Path) -> None:
        self.log_path = log_path
        self.log_path.parent.mkdir(parents=True, exist_ok=True)

    def log_and_alert(self, alert: SuspiciousAlert) -> None:
        message = (
            f"Suspicious entry detected for {alert.name} ({alert.phone}) at "
            f"{alert.timestamp}. Matching rows: {alert.rows}\n"
        )

        with self.log_path.open("a", encoding="utf-8") as f:
            f.write(message)

        logger.warning(message.strip())

        messagebox.showwarning(
            "Suspicious Entry Detected",
            f"The visitor appears to have entered earlier today.\n\nName: {alert.name}\nPhone: {alert.phone}",
        )
