import discord
from discord.ext import commands
import json
import asyncio
from chatcommands import *
from reminder import *
from stats import *


with open('configuration.json', 'r') as f: 
    data = json.load(f)

bot_token = data["bot_token"]

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

# Initilizing the bot
bot = commands.Bot(command_prefix= "*", intents=intents)

setup_commands(bot)
setup_reminders(bot)
update_time_message = setup_stats(bot)


# Schedule task in an async loop
async def schedule_loop():
    while True:
        schedule.run_pending()
        await asyncio.sleep(1)


@bot.event
async def on_ready():
    print("bot is ready desu!! {bot.user}")
    bot.loop.create_task(schedule_loop())
    
    update_time_message.start()


bot.run(bot_token)