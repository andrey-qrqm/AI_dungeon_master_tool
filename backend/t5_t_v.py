from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_dataset, concatenate_datasets
import os

"""DESCRIBE THE MODEL"""
model_name = "google/flan-t5-small"  # Change this if needed
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

"""INTRODUCE TRAINING"""
json_files = ["AI_dungeon_master_tool/backend/dnd-5e-srd/json/01 races.json",
              "dnd-5e-srd/json/00 legal.json",
              "AI_dungeon_master_tool/backend/dnd-5e-srd/json/02 classes.json"]

datasets = []

for json_file in json_files:
    dataset = load_dataset("json", data_files=json_file)
    datasets.append(dataset["train"])  # Assuming 'train' is the key you want

combined_dataset = concatenate_datasets(datasets)

print(combined_dataset[10:])

"""GENERATE OUTPUT"""
def generate_text(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=100)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

print(generate_text("What is the capital of USA?"))
