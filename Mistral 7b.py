from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "mistralai/Mixtral-8x7B-Instruct-v0.1"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Use the specific instruction format
prompt = "<s> [INST] Write a story about a robot who falls in love with a human [/INST] Model answer</s>"
inputs = tokenizer(prompt, return_tensors="pt")

outputs = model.generate(**inputs, max_new_tokens=50)
generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

print(generated_text)
