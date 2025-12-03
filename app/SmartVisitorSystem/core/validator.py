import re
from dataclasses import dataclass
from typing import Tuple


@dataclass
class ValidationResult:
    is_valid: bool
    message: str = ""


class InputValidator:
    def __init__(self) -> None:
        self._email_pattern = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w{2,}$")
        self._phone_pattern = re.compile(r"^\d{10}$")

    def validate(self, name: str, phone: str, email: str, purpose: str) -> ValidationResult:
        if not all([name.strip(), phone.strip(), email.strip(), purpose.strip()]):
            return ValidationResult(False, "All fields are required.")

        if not self._phone_pattern.match(phone.strip()):
            return ValidationResult(False, "Phone number must be a 10-digit number.")

        if not self._email_pattern.match(email.strip()):
            return ValidationResult(False, "Invalid email format.")

        return ValidationResult(True, "OK")
