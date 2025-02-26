from fastapi import FastAPI
from pydantic import BaseModel
#from model import generate_ai_response
from llama_test_v import generate_response
import random

app = FastAPI()


# Example AI Response (Replace with real AI model later)
def generate_dnd_npc():
    names = ["Eldrin", "Morgrim", "Thalia", "Vorstag", "Seraphina"]
    races = ["Elf", "Dwarf", "Human", "Tiefling", "Orc"]
    classes = ["Wizard", "Rogue", "Paladin", "Bard", "Druid"]
    return {
        "name": random.choice(names),
        "race": random.choice(races),
        "class": random.choice(classes),
        "backstory": "An exiled warrior with a mysterious past."
    }


# Define API response model
class NPCResponse(BaseModel):
    name: str
    race: str
    class_: str
    backstory: str


class AIRequest(BaseModel):
    prompt: str
    max_tokens: int = 200  # Default token limit


# Response Model
class AIResponse(BaseModel):
    response: str


@app.post("/generate_ai", response_model=AIResponse)
async def generate_ai_text(request: AIRequest):
    """
    Generate AI-powered text using DeepSeek.
    """
    ai_text = generate_response(request.prompt)
    return AIResponse(response=ai_text)


@app.get("/generate_npc", response_model=NPCResponse)
async def generate_npc():
    npc = generate_dnd_npc()
    return NPCResponse(
        name=npc["name"],
        race=npc["race"],
        class_=npc["class"],
        backstory=npc["backstory"]
    )
