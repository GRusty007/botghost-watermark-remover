import discord
import os
from discord.ext import commands

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    await bot.change_presence(activity=discord.Streaming(name='streaming-name', url='https://www.twitch.tv/urtwitchusername'))

bot.run('MTI0ODM0NDQ5MDYzNzM5MzkyMA.GYg_Fy.QXT937rXgDCt8hrUHHjqwKL7svus9UuBFQzcj8')
