from flask import Flask, request, render_template
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pdfplumber
import pytesseract
from pdf2image import convert_from_bytes
import io
import re

app = Flask(__name__)

model = SentenceTransformer("all-MiniLM-L6-v2")

# 🔥 SKILLS DATABASE
SKILLS_DB = [
    "python", "java", "c", "c++", "sql", "mysql",
    "machine learning", "deep learning", "data science",
    "nlp", "tensorflow", "pytorch", "pandas", "numpy",
    "html", "css", "javascript", "react", "flask", "django"
]

# 🔹 Extract text from PDF
def extract_text_from_pdf(file):
    text = ""
    file_bytes = file.read()

    try:
        with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
    except:
        pass

    # OCR fallback
    if not text.strip():
        try:
            images = convert_from_bytes(file_bytes)
            for img in images:
                text += pytesseract.image_to_string(img)
        except:
            pass

    return text.lower()


# 🔹 Extract skills properly
def extract_skills(text):
    found_skills = set()

    for skill in SKILLS_DB:
        # better matching (handles multi-word skills)
        if skill in text:
            found_skills.add(skill)

    return list(found_skills)


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    matched = []
    missing = []
    suggestions = []

    if request.method == "POST":

        file = request.files.get("resume_file")
        job_text = request.form.get("job")

        if not file:
            return render_template("index.html", result="0.00",
                                   matched=[], missing=[],
                                   suggestions=["Upload resume"])

        if not job_text:
            return render_template("index.html", result="0.00",
                                   matched=[], missing=[],
                                   suggestions=["Enter job description"])

        resume_text = extract_text_from_pdf(file)

        if not resume_text.strip():
            return render_template("index.html", result="0.00",
                                   matched=[], missing=[],
                                   suggestions=["Unable to read PDF"])

        job_text = job_text.lower()

        # 🔥 Similarity
        resume_vector = model.encode(resume_text)
        job_vector = model.encode(job_text)

        similarity = cosine_similarity([resume_vector], [job_vector])[0][0]
        score = max(0, min(similarity * 100, 100))

        # ✅ ONLY 2 DECIMAL (NO %)
        result = f"{score:.2f}"

        # 🔥 Skill Matching Logic (FIXED)
        resume_skills = extract_skills(resume_text)
        job_skills = extract_skills(job_text)

        matched = list(set(resume_skills).intersection(set(job_skills)))
        missing = list(set(job_skills) - set(resume_skills))

        # 🔥 Suggestions
        if missing:
            suggestions.append("Add missing skills: " + ", ".join(missing))

        if score < 60:
            suggestions.append("Improve resume with more relevant experience")

        if score < 40:
            suggestions.append("Resume not aligned with job role")

    return render_template(
        "index.html",
        result=result,
        matched=matched or [],
        missing=missing or [],
        suggestions=suggestions or []
    )


if __name__ == "__main__":
    app.run(debug=True)
