from PyPDF2 import PdfReader

def extract_text_from_pdf(file_path):
    text = ""
    
    reader = PdfReader(file_path)
    
    for page in reader.pages:
        text += page.extract_text()
    
    return text

def extract_skills(text):
    # Simple predefined skill list (you can expand later)
    skills_list = [
        "python", "java", "c", "c++", "machine learning", "deep learning",
        "data science", "nlp", "sql", "html", "css", "javascript",
        "react", "node", "tensorflow", "pandas", "numpy"
    ]
    
    text = text.lower()
    found_skills = []

    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)

    return found_skills
