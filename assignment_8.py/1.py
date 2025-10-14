import re
import string

# Original text
text = "Hey!!! My Email is john_doe123@gmail.com 😄. I scored 98% in exam!!! #Success #AIrocks"

# Step 1: Convert text to lowercase
text_lower = text.lower()

# Step 2: Remove punctuation and numbers
clean_text = re.sub(r'[0-9]', '', text_lower)  # removes numbers
clean_text = clean_text.translate(str.maketrans('', '', string.punctuation))  # removes punctuation

# Step 3: Extract hashtags
hashtags = re.findall(r'#\w+', text)

# Step 4: Extract email address
email = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)

# Step 5: Print the results
print("Cleaned Text:", clean_text)
print("Extracted Hashtags:", hashtags)
print("Extracted Email:", email)
