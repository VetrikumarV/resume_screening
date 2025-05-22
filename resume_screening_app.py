import streamlit as st
from docx import Document
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key="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"  # Paste your key directly, enclosed in quotes)

# Helper: extract text from DOCX file
def extract_docx(file):
    doc = Document(file)
    return "\n".join([para.text for para in doc.paragraphs])

# Helper: get resume screening feedback from OpenAI
def get_screening_feedback(resume_text, job_description):
    prompt = f""" ... """
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a professional resume screener."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.5
    )
    return response.choices[0].message.content

# Streamlit UI

st.title("🤖 Resume Screening with GPT")

job_description = st.text_area("Paste the Job Description", height=200)
resume_file = st.file_uploader("Upload a Resume (DOCX only)", type=["docx"])

# Your button handling goes here:
if st.button("Analyze Resume") and resume_file and job_description:
    file_text = extract_docx(resume_file)
    with st.spinner("Analyzing resume with GPT..."):
        feedback = get_screening_feedback(file_text, job_description)
        st.markdown("### 📝 Screening Results")
        st.write(feedback)
else:
    st.warning("Please upload a resume and provide a job description.")
