import openai
from PyPDF2 import PdfReader
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

api_key = input("Enter your OpenAI API key: ")  # Securely input your API key here
openai.api_key = api_key

def chat_with_gpt(messages):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Updated model to "gpt-4"
            messages=messages
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return str(e)

def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

def create_pdf(file_path, content):
    c = canvas.Canvas(file_path, pagesize=letter)
    width, height = letter
    c.setFont("Helvetica", 12)
    lines = content.split('\n')
    y_position = height - 50  # Start 50 pixels from the top
    for line in lines:
        c.drawString(50, y_position, line)
        y_position -= 15  # Move down 15 pixels for the next line
    c.save()

def main():
    file_path = r"C:\Users\raamc\OneDrive\Desktop\Resume\Raam Charran Resume .pdf"  # Hardcoded input file path
    content = read_pdf(file_path)
    print("Original Content:")
    print(content)
    
    conversation_history = [{"role": "system", "content": "You are a helpful assistant."}]
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit']:
            break
        conversation_history.append({"role": "user", "content": user_input})
        response = chat_with_gpt(conversation_history)
        print("ChatGPT:", response)
        conversation_history.append({"role": "assistant", "content": response})
        
        if input("Do you want to apply this change to the content? (yes/no): ").lower() == 'yes':
            content = content.replace(user_input, response)
    
    new_file_path = r"C:\Users\raamc\OneDrive\Desktop\Resume\Raam Charran Resume gptupdated.pdf"  # Hardcoded output file path
    create_pdf(new_file_path, content)
    print(f"Updated resume has been saved to {new_file_path}")

if __name__ == "__main__":
    main()
