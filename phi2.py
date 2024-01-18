import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load model and tokenizer
model_name = "microsoft/phi-2"
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float32, trust_remote_code=True)

# Start interactive chat
while True:
    prompt = input("You: ")
    if prompt.lower() == "exit":
        break

    inputs = tokenizer(prompt, return_tensors="pt", return_attention_mask=False)
    outputs = model.generate(**inputs, max_length=50)
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    print("Phi-2:", generated_text)

print("Chat ended.")
