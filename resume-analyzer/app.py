from utils import extract_text_from_pdf

resume_path = "resume.pdf"

text = extract_text_from_pdf(resume_path)

print("----- RESUME TEXT -----")
print(text[:1000])
