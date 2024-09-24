import discord
from discord.ext import commands, tasks
import schedule
import datetime
import pytz
import json
import asyncio


with open('configuration.json', 'r') as f: 
    data = json.load(f)

bot_token = data["bot_token"]

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

# Initilizing the bot
bot = commands.Bot(command_prefix= "*", intents=intents)






#Bot introduction
    
@bot.command()
async def hello(ctx):
    await ctx.send("Hello desu!! nice to meet you desu!!")
    
@bot.command()
async def Ziro(ctx):
    await ctx.send("GOAT of every game ||jokes on you ahaha||")
    
@bot.command()
async def sri(ctx):
    await ctx.send("Radiant valorant player :skull::skeleton:")    
    
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
        
# Wrapper function to ensure the coroutine is awaited
#Genshin daily reminder
def schedule_genshin_reminder():
     asyncio.create_task(daily_reset_hoyogames(
         channel_id=1280846388774572065,
         message="Time to do your daily commission, Tabibito!!",
         image_url="https://cdn.discordapp.com/attachments/1013901377266794619/1281096241588998199/Genshin.gif?ex=66da7959&is=66d927d9&hm=9d398aefe87dc4ab2ea1ef023c0c9437bb915a27e46de7e1f248266bfc80c8fe&",
     ))
     
schedule.every().day.at("08:30:00").do(schedule_genshin_reminder)    
 
#Honkai daily reminder 
def schedule_honkai_reminder():
    asyncio.create_task(daily_reset_hoyogames(
        channel_id=1280918129358409779,
        message="Time to do your daily commission, Kancho!!",
        image_url="https://cdn.discordapp.com/attachments/1013901377266794619/1281098159124381707/honkai.gif?ex=66da7b22&is=66d929a2&hm=e831e0aa74c754485a9c111015da335c80a12ec0e4b315b0605fbd02f5962e77&",
        ))
    
schedule.every().day.at("08:30:00").do(schedule_honkai_reminder)
     
#Honkai MA reminder
def schedule_honkai_memorial_arena_reminder():
    asyncio.create_task(daily_reset_hoyogames(
        channel_id=1280918129358409779,
        message="Time to do you Memorial Arena desu!!",
        image_url="https://cdn.discordapp.com/attachments/993100751113027585/1281434750497722499/bronya-think-loading-gif.gif?ex=66dbb49c&is=66da631c&hm=98e01d19d9e82219ff1fed14769ec5daae77a91e9f0e1b63c31b8e7b07feab56&",
        role_id=1280918307163078748
    ))
schedule.every().sunday.at("22:30:00").do(schedule_honkai_memorial_arena_reminder)    
    
#Honkai abyss reminder    
def schedule_honkai_abyss_reminder():
    asyncio.create_task(daily_reset_hoyogames(
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
            channel_id=1280846388774572065,
            message="warning desu !! your primo are in danger do your abyss desu!!",
            image_url="https://cdn.discordapp.com/attachments/555341819588902912/1281274267379564554/disappointed-lumine.gif?ex=66db1f26&is=66d9cda6&hm=48c22107d4efd9fb2625a294d4ad74cc93c718c68fc37847ce175667bda22236&",
            role_id=1280846591019716618
            ))
        
        
schedule.every().day.at("08:30:00").do(schedule_genshin_abyss_reminder) 


#Server stats !!!!
#Honkai impact server stats 
channel_id=1281439842365997201
message_id=1282503214717210686

def Honkai_current_time():
    now= datetime.datetime.now()
    
    #Calculate the daily reset time
    daily_reset_eu= datetime.datetime.combine(now.date(), datetime.time(8, 30, 0))
    
    
    #If the reset time has already passed today, move it to tommorow 
    if now > daily_reset_eu:
        daily_reset_eu += datetime.timedelta(days=1)
        
    #Time remaining for the daily reset in seconds         
    daily_reset_eu_seconds = (daily_reset_eu - now).total_seconds()
    
    #Convert seconds to hours
    daily_reset_eu_hours = int(daily_reset_eu_seconds) // 3600
    daily_reset_eu_min = (int(daily_reset_eu_seconds) % 3600) //60
    
    # Change format of remaining time in H:M
    daily_reset_eu_time_str = f"{daily_reset_eu_hours:02}:{daily_reset_eu_min:02}"
    
    
    
    # Weekly reset is in 3 days
    weekly_reset_eu= 3
    
    return{
        "EU":{"time": "08:30 AM", 
              "daily_reset":daily_reset_eu, 
              "weekly_reset":weekly_reset_eu,
              "daily_reset_hours":daily_reset_eu_time_str
        },
    }

#Task to update every 60 sec
@tasks.loop(seconds=60)
async def update_time_message():
    global message_id
    channel = bot.get_channel(channel_id)
    
    
    if channel is None:
        print(f"Channel with ID{channel_id}not found.")
        return
    
    
    guild = channel.guild
    member_count = guild.member_count
    
    server_status = Honkai_current_time()
    daily_reset_eu_hours = server_status["EU"]["daily_reset_hours"]

    
    
    embed = discord.Embed(
        title="Server Status",
        description=f"Members: {member_count}",
        color=discord.Color.red()
    )
    
    for server, status in server_status.items():
        embed.add_field(
            name=f"{server} Server",
            value=(
                f"```•Reset Time: {status['time']}```\n"
                f"```•Daily Reset in {daily_reset_eu_hours}```\n"
                f"```•Weekly Reset in {status['weekly_reset']} days```"
            ),
            inline=False             
        )

    embed.set_image(url="https://cdn.discordapp.com/attachments/547344310635462656/1282545989021863947/test.gif?ex=66dfbf88&is=66de6e08&hm=8d3b37118bbaf0d93c04eb2c595078c0407861f60188b652a3517f9cbf674a97&")
    local_time = datetime.datetime.now()
    local_time_str = local_time.strftime('%I:%M %p')
    embed.set_footer(text=f"Current time: {local_time_str}")
    
    if message_id is None:
        message = await channel.send(embed=embed)
        message_id = message.id
    else:
        # Fetch the message and update it
        try:
            message = await channel.fetch_message(message_id)
            await message.edit(embed=embed)
        except discord.NotFound:
            # If the message was deleted, send a new one
            message = await channel.send(embed=embed)
            message_id = message.id



#schedule task in an async loop
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

    

    
