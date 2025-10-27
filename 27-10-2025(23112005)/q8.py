# Q8. Write a Python program that:
# • Reads a paragraph from a text file.
# • Removes punctuation and numbers.
# • Extracts all email IDs and hashtags using Regular Expressions (re module).
# • Saves the cleaned text to an Excel file using Openpyxl.
import re
import openpyxl

# Read the paragraph from a text file
with open("merged.txt", "r") as file:
    paragraph = file.read()

# Remove punctuation and numbers
cleaned_text = re.sub(r"[^\w\s#@]", "", paragraph)
cleaned_text = re.sub(r"\d+", "", cleaned_text)

# Extract email IDs and hashtags
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
hashtag_pattern = r"#\w+"

email_ids = re.findall(email_pattern, cleaned_text)
hashtags = re.findall(hashtag_pattern, cleaned_text)

# Save the cleaned text and extracted data to an Excel file
workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = "Extracted Data"

# Write cleaned text
sheet["A1"] = "Cleaned Text"
sheet["A2"] = cleaned_text

# Write email IDs
sheet["B1"] = "Email IDs"
for i, email in enumerate(email_ids, start=2):
    sheet[f"B{i}"] = email

# Write hashtags
sheet["C1"] = "Hashtags"
for i, hashtag in enumerate(hashtags, start=2):
    sheet[f"C{i}"] = hashtag

# Save the workbook
workbook.save("output.xlsx")
print("Cleaned text and extracted data saved to 'output.xlsx'")

