from resume_parser import extract_text

try:
    text = extract_text("resume.pdf")
    print("Resume loaded successfully!\n")
    print(text[:500])  # prints first 500 characters
except Exception as e:
    print("Error:", e)
