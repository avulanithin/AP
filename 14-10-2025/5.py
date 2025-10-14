# Write a Python function that removes words shorter than 4 characters and extracts all capitalized words (proper nouns) from a paragraph.
import re

def process_text(paragraph):
    # Remove words shorter than 4 characters
    filtered = re.sub(r'\b\w{1,3}\b', '', paragraph)
    # Extract all capitalized words
    proper_nouns = re.findall(r'\b[A-Z][a-z]*\b', filtered)
    return filtered, proper_nouns

text = "Alice and Bob are working at OpenAI. The project deadline is next week."
filtered_text, proper_nouns = process_text(text)

print("Filtered Text:", filtered_text)
print("Proper Nouns:", proper_nouns)