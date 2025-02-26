import transformers
import torch
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Hugging Face model details
model_id = "meta-llama/Meta-Llama-3.1-8B-Instruct"
HF_TOKEN = os.getenv("HUGGING_FACE_TOKEN")

# Initialize the pipeline correctly
pipeline = transformers.pipeline(
    "text-generation",
    model=model_id,
    model_kwargs={"torch_dtype": torch.bfloat16},
    device_map="auto",
    token=HF_TOKEN  # Corrected argument
)

# Prepare the correct input format
initial_prompt = "You are a pirate chatbot who always responds in pirate speak! Who are you?"
outputs = pipeline(
    initial_prompt,  # Must be a string, not a list
    max_new_tokens=256,
)


def generate_response(user_input: str, max_tokens: int = 200):
    # Construct the prompt correctly
    message_stack = "You are a Dungeon and Dragons specialized chatbot, who knows all the races and classes in D&D.\n"
    message_stack += f"User: {user_input}\nAI:"

    # Generate response
    output = pipeline(
        message_stack,  # Use correct variable
        max_new_tokens=max_tokens,
    )
    print(output[0]["generated_text"])
    # Extract the generated text properly
    return output[0]["generated_text"]


# Print the corrected output
print(outputs[0]["generated_text"])  # No need for [-1]
