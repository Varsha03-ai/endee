from sentence_transformers import SentenceTransformer
from database import add_resume_embedding, search_job_fit

model = SentenceTransformer("all-MiniLM-L6-v2")

resume_text = "Varsha has experience in Python, ML, and deep learning."
vector = model.encode(resume_text)

add_resume_embedding("varsha_resume", vector, text=resume_text)

# Example job vector search
job_text = "Looking for a data scientist with Python and ML skills."
job_vector = model.encode(job_text)
results = search_job_fit(job_vector, top_k=1)
print(results)
