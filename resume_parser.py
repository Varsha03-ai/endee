import pdfplumber
import docx2txt

def extract_text(file_path):
    """
    Extract text from a PDF or DOCX resume
    """
    if file_path.endswith('.pdf'):
        with pdfplumber.open(file_path) as pdf:
            text = ''
            for page in pdf.pages:
                text += page.extract_text() + '\n'
        return text
    elif file_path.endswith('.docx'):
        return docx2txt.process(file_path)
    else:
        raise ValueError("Unsupported file type. Use PDF or DOCX.")
