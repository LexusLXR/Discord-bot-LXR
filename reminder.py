import discord
from discord.ext import commands
import schedule
import asyncio
import datetime



#Hoyogames reminder   
async def daily_reset_hoyogames(bot, channel_id, message, image_url=None, role_id=None):
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
        
def setup_reminders(bot):
    
    #Genshin Daily reminder
    def schedule_genshin_reminder():
        asyncio.create_task(daily_reset_hoyogames(
            bot,
            channel_id=1280846388774572065,
            message="Time to do your daily commission, Tabibito!!",
            image_url="https://cdn.discordapp.com/attachments/1013901377266794619/1281096241588998199/Genshin.gif"
        ))
    schedule.every().day.at("08:30:00").do(schedule_genshin_reminder)    
    
    #Honkai Daily reminder    
    def schedule_honkai_reminder():
        asyncio.create_task(daily_reset_hoyogames(
            bot,
            channel_id=1280918129358409779,
            message="Time to do your daily commission, Kancho!!",
            image_url="https://cdn.discordapp.com/attachments/1013901377266794619/1281098159124381707/honkai.gif"
        ))
                
    schedule.every().day.at("08:30:00").do(schedule_honkai_reminder) 
    
    
    #Honkai MA reminder
    def schedule_honkai_memorial_arena_reminder():
        asyncio.create_task(daily_reset_hoyogames(
            bot,
            channel_id=1280918129358409779,
            message="Time to do you Memorial Arena desu!!",
            image_url="https://cdn.discordapp.com/attachments/993100751113027585/1281434750497722499/bronya-think-loading-gif.gif?ex=66dbb49c&is=66da631c&hm=98e01d19d9e82219ff1fed14769ec5daae77a91e9f0e1b63c31b8e7b07feab56&",
            role_id=1280918307163078748
        ))
    schedule.every().thursday.at("22:30:00").do(schedule_honkai_memorial_arena_reminder)     
    
    
     #Honkai abyss reminder    
    def schedule_honkai_abyss_reminder():
        asyncio.create_task(daily_reset_hoyogames(
            bot,
            channel_id=1280918129358409779,
            message="your crystals are in danger desu!! time to do your abyss desu!!",
            image_url="https://cdn.discordapp.com/attachments/555341819588902912/1281267140145578077/herrscher-of-sentience.gif?ex=66db1883&is=66d9c703&hm=1237de798486065e658927e47b4ceae8f625af768bbf3c1d3a74160ac67c3e8c&",
            role_id=1280918307163078748
            )) 

    schedule.every().wednesday.at("22:00:00").do(schedule_honkai_abyss_reminder) 
    schedule.every().sunday.at("22:00:00").do(schedule_honkai_abyss_reminder) 
    
    
    #Genshin abyss reminder
    def schedule_genshin_abyss_reminder():
        today = datetime.datetime.now()
        if today.day == 14:
            asyncio.create_task(daily_reset_hoyogames(
                bot,
                channel_id=1280846388774572065,
                message="warning desu !! your primo are in danger do your abyss desu!!",
                image_url="https://cdn.discordapp.com/attachments/555341819588902912/1281274267379564554/disappointed-lumine.gif?ex=66db1f26&is=66d9cda6&hm=48c22107d4efd9fb2625a294d4ad74cc93c718c68fc37847ce175667bda22236&",
                role_id=1280846591019716618
                ))
            
            
    schedule.every().day.at("08:30:00").do(schedule_genshin_abyss_reminder) 
                
        
        
        
        
        
        
        