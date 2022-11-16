# bot.py
import os
from discord.ext import commands
import discord
from dotenv import load_dotenv
import numpy as np
import pandas as pd
import matplotlib as mp
import datetime as dt

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
#intents for messaging and defualts
intents = discord.Intents.default()
intents.message_content = True

#passing the intents to the client and creating it
client = discord.Client(intents=intents)
#bot creation
bot = commands.Bot(intents=intents,command_prefix='$')
#creates dataframe
df1 = pd.DataFrame(columns=("Rating","Time", "Day"))  

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
@client.event
async def on_message(message):
        if(message.content.startswith("!rngU")):
            await message.channel.send('Hello!')
@bot.command()
async def rngU(ctx, arg: int):
        await ctx.send(arg)

@bot.command()
async def rngU(ctx, arg: int):
        await ctx.send(arg)
        df1.loc[len(df1.index)] = [10, "12:20", "Monday"]


client.run(TOKEN)