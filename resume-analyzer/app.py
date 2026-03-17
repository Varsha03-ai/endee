from utils import extract_text_from_pdf, extract_skills

# Resume
resume_path = "resume.pdf"
resume_text = extract_text_from_pdf(resume_path)

# Job Description (you can change this later)
job_description = """
Looking for a Python developer with experience in machine learning,
data science, and SQL. Knowledge of deep learning is a plus.
"""

# Extract skills
resume_skills = extract_skills(resume_text)
jd_skills = extract_skills(job_description)

# Matching logic
matching_skills = list(set(resume_skills) & set(jd_skills))
missing_skills = list(set(jd_skills) - set(resume_skills))

# Match score
if len(jd_skills) > 0:
    match_score = (len(matching_skills) / len(jd_skills)) * 100
else:
    match_score = 0

# Output
print("\n===== RESULT =====")
print("Resume Skills:", resume_skills)
print("Job Skills:", jd_skills)
print("Matching Skills:", matching_skills)
print("Missing Skills:", missing_skills)
print(f"Match Score: {match_score:.2f}%")
