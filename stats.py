import discord
from discord.ext import commands , tasks
import datetime
import schedule


#Server stats !!!!
#Honkai impact server stats 
def setup_stats(bot):
    channel_id=1281439842365997201
    global message_id
    message_id=1282503214717210686

    def Hoyoplay_current_time():
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
        
        
        
         #weekly reset datetime
        weekly_reset_time = datetime.time(8, 30)
        
        #days till next monday
        days_until_next_monday = (7 - now.weekday()) % 7  # 0 for Monday, 6 for Sunday
        
        # change daily reset days if its monday
        if days_until_next_monday == 0 and now.time() > weekly_reset_time:
            days_until_next_monday = 7
        
        
        weekly_reset_eu = days_until_next_monday
        
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
        
        server_status = Hoyoplay_current_time()
        daily_reset_eu_hours = server_status["EU"]["daily_reset_hours"]

        
        
        embed = discord.Embed(
            title="Hoyogames Server Status Eu",
            description=f"Members: {member_count}",
            color=discord.Color.blue()
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

        embed.set_image(url="https://cdn.discordapp.com/attachments/993100691088343111/1288419482770866208/HoYoverse_gamescom_2023.jpg?ex=66f51da6&is=66f3cc26&hm=0b5091a115b3ffbb651e9cda0b83356caadc25f29addc3780efb1786b06842e0&")
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

    return update_time_message

