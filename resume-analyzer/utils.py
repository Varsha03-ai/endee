from PyPDF2 import PdfReader

# Function to extract text from PDF
def extract_text_from_pdf(file_path):
    text = ""
    try:
        reader = PdfReader(file_path)
        for page in reader.pages:
            if page.extract_text():
                text += page.extract_text()
    except Exception as e:
        print("Error reading PDF:", e)
    return text


# Function to extract skills from text
def extract_skills(text):
    skills_list = [
        "python", "java", "c", "c++", "machine learning",
        "data science", "sql", "deep learning", "nlp",
        "tensorflow", "pandas", "numpy", "html", "css",
        "javascript", "react"
    ]

    text = text.lower()
    found_skills = []

    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)

    return found_skills
