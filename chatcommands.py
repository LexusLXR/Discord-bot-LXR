#BOT COMMANDS
import discord
from discord.ext import commands

def setup_commands(bot):

    @bot.command()
    async def hello(ctx):
        await ctx.send("Hello desu!! nice to meet you desu!!")
    
    @bot.command()
    async def Ziro(ctx):
        await ctx.send("GOAT of every game ||jokes on you ahaha||")
    
    @bot.command()
    async def sri(ctx):
        await ctx.send("Radiant valorant player :skull::skeleton:") 

