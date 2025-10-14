#  Remove all stopwords (like 'is', 'the', 'a', 'an', 'in') from a given text and print the cleaned output.
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

text = "This is a sample text with some stopwords. The goal is to remove all the stopwords from this text."

stop_words = set(stopwords.words('english'))
words = word_tokenize(text)
filtered_words = [word for word in words if word.lower() not in stop_words]
cleaned_text = ' '.join(filtered_words)

print(cleaned_text)#  Remove all stopwords (like 'is', 'the', 'a', 'an', 'in') from a given text and print the cleaned output.