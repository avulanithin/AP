# From a multiline string, extract all 10-digit Indian mobile numbers (starting with 6–9).
import re

# Take input from the user
text = input("Enter text containing phone numbers: ")

# Regex pattern to find 10-digit mobile numbers
pattern = r"\b\d{10}\b"

mobile_numbers = re.findall(pattern, text)

print("Mobile numbers found:", mobile_numbers)
