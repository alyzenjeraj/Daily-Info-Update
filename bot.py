from weatherCheck import webScrapeWeather

import discord
from discord.ext import commands, tasks
from discord.utils import get

import python_weather
import asyncio

from datetime import datetime
from threading import Timer

# location = ''
# weather = ''

bot = commands.Bot('!')
weather = ''
weatherStatus = ''

@bot.event
async def on_ready():
    print('Online!')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('!configure'))

@bot.command(aliases=['configure','c'])
async def _start(ctx, *city):

    while True:
        try:
        # fetch a weather forecast from a city
            global weather
            weather = webScrapeWeather(city)[0]
            global weatherStatus
            weatherStatus = webScrapeWeather(city)[1]
            # await ctx.send(weather)
            give_weather.start()
            break
        except:
            await ctx.send('Location not found, try again.')
    # returns the current day's forecast temperature (int)
    # global weather 
    # weather = weather.current.temperature

@bot.command(aliases=['weather','w'])
async def _w(ctx):
    global weather
    await ctx.send(weather)

@tasks.loop(seconds=10)
async def give_weather():
    channel = bot.get_channel(858181017096945674)
    global weather
    print(weather)
    await channel.send(weather)
    embed=discord.Embed(title="**Good Morning, @Jopee!**", description="Here's your daily run down:", color=0xffed09)
    embed.set_thumbnail(url="http://ssl.gstatic.com/onebox/weather/64/sunny.png")
    embed.add_field(name=weatherStatus, value=weather, inline=False)
    await channel.send(embed=embed)
# @tasks.loop(hours=24)
# async def called_once_a_day():
#     await ctx.author.send()
#     embed=discord.Embed(title="**Good Morning, {message.author}!**", description="Here's how today is going to look:", color=0xffed09)
#     embed.set_thumbnail(url="https://i.pinimg.com/originals/53/22/c2/5322c2cad533e12e552d0dfdc89b4c25.png")
#     embed.add_field(name="Sunny", value={weather}, inline=False)
#     await ctx.send(embed=embed)

# @called_once_a_day.before_loop
# async def before():
#     x=datetime.today()
#     y=x.replace(day=x.day+1, hour=8, minute=0, second=0, microsecond=0)
#     delta_t=y-x
#     secs=delta_t.seconds+1
#     await bot.wait_until_ready()

# called_once_a_day.start()
bot.run("ODU4MTk5MDA4NzU2MTA1Mjc3.YNaqHA.-h_TXXDp7hoGel-5utBcugPJOCo")