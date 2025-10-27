# Q9. Using NLTK, create a Python program that:
# • Tokenizes a paragraph into sentences and words.
# • Removes stopwords.
# • Prints the top 5 most frequent words and their counts.
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Sample paragraph
paragraph = "Natural Language Processing (NLP) is a fascinating field of study. It focuses on the interaction between computers and human language. With the rise of big data, NLP has become increasingly important for extracting meaningful information from text. Applications of NLP include sentiment analysis, machine translation, and chatbots."

# Tokenize into sentences
sentences = sent_tokenize(paragraph)

# Tokenize into words
words = word_tokenize(paragraph)

# Remove stopwords
stop_words = set(stopwords.words("english"))
filtered_words = [word for word in words if word.lower() not in stop_words]

# Print the top 5 most frequent words and their counts
fdist = FreqDist(filtered_words)
print("Top 5 most frequent words:")
for word, count in fdist.most_common(5):
    print(f"{word}: {count}")

# Output sentences and filtered words (optional)
print("\nTokenized Sentences:")
for sentence in sentences:
    print(sentence)

print("\nFiltered Words:")
print(filtered_words)

