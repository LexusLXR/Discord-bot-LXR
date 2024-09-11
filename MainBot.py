import discord
from discord.ext import commands
import json
import asyncio
from chatcommands import *



with open('configuration.json', 'r') as f: 
    data = json.load(f)

bot_token = data["bot_token"]

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

# Initilizing the bot
bot = commands.Bot(command_prefix= "*", intents=intents)

# Import commands from chatcommands.py

setup_commands(bot)

@bot.event
async def on_ready():
    print("bot is ready desu!! {bot.user}")
    


bot.run(bot_token)