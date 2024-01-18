import PyPDF2
import openai
import re


def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                # Correct spacing issues
                page_text = re.sub(r'(\w)\s+(\w)', r'\1\2', page_text)
                text += page_text + '\n'  # Preserve line breaks
    return text

def format_extracted_text(text):
    # Replace bullet points symbols if needed
    formatted_text = text.replace('•', '\n• ')
    return formatted_text



def summarize_text(text, openai_api_key):
    openai.api_key = openai_api_key

    response = openai.ChatCompletion.create(
        model="gpt-4-1106-preview",  # Using the specified chat model
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Summarize the following resume into three bullet points:\n\n" + text}
        ]
    )
    # Assuming the last message from the model will be the summary
    return response.choices[-1].message['content'].strip()

# ... (existing imports and functions)

def generate_resume_insights(resume_summary, job_summary, openai_api_key):
    openai.api_key = openai_api_key

    prompt = ("Given the following resume summary and job description summary, "
              "provide insights on how the resume could be improved for this job:\n\n"
              "Resume Summary:\n" + resume_summary + "\n\n"
              "Job Description Summary:\n" + job_summary)

    response = openai.ChatCompletion.create(
        model="gpt-4-1106-preview",  # Using the specified chat model
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    # Assuming the last message from the model will be the insights
    return response.choices[-1].message['content'].strip()


def main():
    pdf_file_path = 'C:/Users/raamc/OneDrive/Desktop/Resume/Raam_Charran_Resume.pdf'
    openai_api_key = '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'     # Replace with your OpenAI API key

    extracted_text = read_pdf(pdf_file_path)
    formatted_text = format_extracted_text(extracted_text)
    print(formatted_text)
'''
    resume_summary = summarize_text(resume_text, openai_api_key)

# Ask the user to input the job description
    job_description = input("Enter the job description:\n")   


        # Summarize job posting
    job_summary = summarize_text(job_description, openai_api_key)

    resume_improvement_insights = generate_resume_insights(resume_summary, job_summary, openai_api_key)
    print("Resume Improvement Insights:\n", resume_improvement_insights)
'''
if __name__ == "__main__":
    main()