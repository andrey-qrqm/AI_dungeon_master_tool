import discord
import requests
import os
from dotenv import load_dotenv
from discord.ext import commands

# Load API URL
load_dotenv()
TOKEN = os.getenv("TOKEN_DISCORD_BOT")
API_URL = os.getenv("API_URL")

# Set up bot
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def generate_npc(ctx):
    """Command to generate a DND NPC"""
    print("!generate_npc command")
    response = requests.get(API_URL)
    if response.status_code == 200:
        npc = response.json()
        embed = discord.Embed(title="Generated NPC", color=discord.Color.blue())
        embed.add_field(name="Name", value=npc["name"], inline=False)
        embed.add_field(name="Race", value=npc["race"], inline=True)
        embed.add_field(name="Class", value=npc["class_"], inline=True)
        embed.add_field(name="Backstory", value=npc["backstory"], inline=False)
        await ctx.send(embed=embed)
    else:
        await ctx.send("Error generating NPC. Please try again!")


@bot.command()
async def ai(ctx, *, prompt: str):
    """Generate AI-powered text from DeepSeek"""
    response = requests.post(API_URL, json={"prompt": prompt, "max_tokens": 190})
    if response.status_code == 200:
        ai_text = response.json()["response"]
        await ctx.send(f"**AI Response:** {ai_text}")
    else:
        await ctx.send("Error: Unable to process request.")

# Run bot
bot.run(TOKEN)
