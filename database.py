import chromadb

# Initialize ChromaDB client and collection
client = chromadb.Client()
collection = client.create_collection("resumes")

def add_resume_embedding(resume_id, vector, text=""):
    """
    Add a resume embedding to ChromaDB.
    'text' can be the resume text or a placeholder string
    """
    collection.add(
        documents=[text],      # string version of resume
        embeddings=[vector],   # actual vector embedding
        metadatas=[{"resume_id": resume_id}],
        ids=[resume_id]
    )

def search_job_fit(job_vector, top_k=1):
    """
    Compare job description embedding with resumes in ChromaDB.
    Returns the top matching resumes.
    """
    results = collection.query(
        query_embeddings=[job_vector],
        n_results=top_k
    )
    return results
