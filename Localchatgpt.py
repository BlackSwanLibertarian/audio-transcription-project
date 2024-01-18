from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

def setup_model(model_name):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    return tokenizer, model

def generate_response(input_text, tokenizer, model):
    input_ids = tokenizer.encode(input_text, return_tensors='pt')
    output = model.generate(input_ids, max_length=512)
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response

# Setup model - using 'mistralai/Mixtral-8x7B-Instruct-v0.1'
model_name = 'mistralai/Mixtral-8x7B-Instruct-v0.1'
tokenizer, model = setup_model(model_name)

# Continuous chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chat ended.")
        break
    response = generate_response(user_input, tokenizer, model)
    print("AI:", response)
