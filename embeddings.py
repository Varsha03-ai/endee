from sentence_transformers import SentenceTransformer

# Load a pre-trained model
model = SentenceTransformer('all-MiniLM-L6-v2')  # fast and accurate

def get_embedding(text):
    """
    Convert text to a vector embedding
    """
    return model.encode(text)
