from resume_parser import extract_text
from embeddings import get_embedding

# Load resume text
text = extract_text("resume.pdf")
print("Resume loaded successfully!")

# Get embedding
vector = get_embedding(text)
print("Embedding length:", len(vector))
print("First 10 numbers:", vector[:10])
