import discord
import schedule
import datetime
import asyncio
#Hoyogames reminder
    
async def daily_reset_hoyogames(channel_id, message, image_url=None, role_id=None):
    channel = bot.get_channel(channel_id)
    if channel:
        embed = discord.Embed(
            title="Daily Reminder Desu!!!!",
            description=message,
            color=discord.Color.blue()
        )
        embed.set_image(url=image_url)
        embed.set_footer(text="Stay on top of your task Desu")
        await channel.send(content=f"<@&{role_id}>",embed=embed) 
    else:
        print(f"Channel with ID{channel_id} not found.")