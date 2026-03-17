from endee import Endee

db = Endee()  # initialize Endee vector DB

def store_resume_embedding(resume_text, resume_id):
    embedding = generate_embedding(resume_text)
    db.upsert(vector=embedding, id=resume_id)

def search_job_fit(job_description):
    embedding = generate_embedding(job_description)
    results = db.search(vector=embedding, top_k=5)
    return results
