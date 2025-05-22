from openai import OpenAI

# Initialize the client once, at the top of your script
client = OpenAI(api_key="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")

def get_screening_feedback(resume_text, job_description):
    prompt = f"""
    Given the following job description and resume, evaluate the resume:

    Job Description:
    {job_description}

    Resume:
    {resume_text}

    Provide:
    - A brief summary of the resume
    - Match percentage with job description
    - Strengths
    - Weaknesses
    - Suggest improvements
    """

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a professional resume screener."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.5
    )
    return response.choices[0].message.content

