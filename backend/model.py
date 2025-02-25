from transformers import LlamaForCausalLM, LlamaTokenizer
import torch

# Path to your local LLaMA 7B model or Hugging Face model ID
MODEL_PATH = "/path/to/llama-7b"  # Replace with your model path or Hugging Face model ID

print("Loading LLaMA 7B model... (This may take a few minutes)")

# Load tokenizer and model
tokenizer = LlamaTokenizer.from_pretrained(MODEL_PATH)
model = LlamaForCausalLM.from_pretrained(
    MODEL_PATH,
    torch_dtype=torch.float32  # Use float32 for CPU
)

# Ensure the model is on CPU
model.to("cpu")

print("Model loaded successfully!")


def generate_ai_response(prompt: str, max_tokens: int = 200):
    """
    Generates AI response from the LLaMA 7B model based on the input prompt.
    """
    inputs = tokenizer(prompt, return_tensors="pt").to("cpu")  # Ensure inputs are on CPU
    with torch.no_grad():
        output = model.generate(**inputs, max_length=max_tokens)

    response_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return response_text


print(generate_ai_response(prompt="Describe an ancient wizard NPC."))
