# Q10. Implement text similarity using FastText:
# • Train a FastText model on a small text file.
# • Compare the similarity score between two words (e.g., ‘python’ and ‘programming’).
# • Display the vector representation of one word.

from gensim.models import FastText

# ---------------------------
# Step 1: Prepare the Training Data
# ---------------------------
# Create a small text corpus
sentences = [
    ["python", "is", "a", "popular", "programming", "language"],
    ["machine", "learning", "and", "data", "science", "use", "python"],
    ["fasttext", "is", "useful", "for", "text", "representation"],
    ["programming", "in", "python", "is", "fun"]
]

# ---------------------------
# Step 2: Train FastText Model
# ---------------------------
model = FastText(
    sentences=sentences,
    vector_size=50,   # size of each word vector
    window=3,         # context window
    min_count=1,      # include all words
    epochs=10         # number of training iterations
)

# ---------------------------
# Step 3: Compare Word Similarity
# ---------------------------
similarity_score = model.wv.similarity("python", "programming")
print(f"Similarity between 'python' and 'programming': {similarity_score:.4f}")

# ---------------------------
# Step 4: Display Word Vector
# ---------------------------
vector = model.wv["python"]
print("\nVector representation of 'python':")
print(vector)
