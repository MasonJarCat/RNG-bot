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

#bot creation
bot = commands.Bot(intents=intents,command_prefix='$')
#creates dataframe
df1 = pd.DataFrame(columns=("Rating","Time", "Day"))  



@bot.command()
async def rngU(ctx, arg: int):
        await ctx.send(arg)
        df1.loc[len(df1.index)] = [arg, "12:20", "Monday"]


bot.run(TOKEN)