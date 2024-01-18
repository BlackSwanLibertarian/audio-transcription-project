import openai

api_key = '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'
openai.api_key = api_key

def chat_with_gpt(messages):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return str(e)

conversation_history = []

while True:
    user_input = input("You: ")
    if user_input.lower() in ['quit', 'exit']:
        break
    
    conversation_history.append({"role": "system", "content": "You are a helpful assistant."})
    conversation_history.append({"role": "user", "content": user_input})
    
    response = chat_with_gpt(conversation_history)
    
    print("ChatGPT:", response)
    conversation_history.append({"role": "assistant", "content": response})
