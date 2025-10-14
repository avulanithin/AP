# From a multiline string, extract all 10-digit Indian mobile numbers (starting with 6–9).
import re

text = """
Contact me at 9876543210 or 9123456789.
My office number is 01123456789.
"""

pattern = r"\b[6-9]\d{9}\b"
mobile_numbers = re.findall(pattern, text)
print(mobile_numbers)