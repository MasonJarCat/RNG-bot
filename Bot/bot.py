# bot.py
import os
from discord.ext import commands
import discord
from dotenv import load_dotenv
import numpy as np
import pandas as pd
import matplotlib as plt
import datetime as dt
import openpyxl as px
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
#intents for messaging and defualts
intents = discord.Intents.default()
intents.message_content = True

#passing the intents to the client and creating it
#creates dataframe

#df1 = pd.DataFrame(columns=("Rating","Time", "Day"))
df1 = pd.read_excel('Hans.xlsx', engine = "openpyxl")  
#bot creation
specialOfTheDay = []
bot = commands.Bot(command_prefix='!',intents=intents)
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def rngU(ctx, arg: int):
        await ctx.send(arg)
#populates array
@bot.command()
async def rngH(ctx, arg: int):
        await ctx.send(arg)

        dti = pd.to_datetime([ctx.message.created_at])
        dti = dti.tz_convert("US/Eastern")
        df1.loc[len(df1.index)] = [arg, dti.time, dti.day_name()] 
       # await ctx.send(df1)
       # print(df1)

#gets average
@bot.command()
async def getRate(ctx):
    var = 0
    strI = "Average Hans Rating Today:"
    for x in range(len(df1.index)):
        var = var + df1.loc[x,"Rating"]
    var = var / len(df1.index)
    strI = " ".join([strI,str(var)])
    await ctx.send(strI)

  #report the days special  
@bot.command()
async def repSpec(ctx, arg):
    specialOfTheDay.append(arg)
    await ctx.send("Thank you for reporting")

# get the days special
@bot.command()
async def spec(ctx):
    str = "The Specials Of The Day Are: "
    for i in range(len(specialOfTheDay)):
        str = " ".join([str, specialOfTheDay[i]])
    await ctx.send(str)

#saves it to an excel file via command
@bot.command()
async def save(ctx):
    with pd.ExcelWriter("Hans.xlsx", mode="a",if_sheet_exists="replace",engine = "openpyxl") as writer:
        df1.to_excel(writer, sheet_name="Sheet 1", index=False)
    await ctx.send("Saved")
    

#broken do NOT use
@bot.command()
async def getGGraph(ctx):
   # df1.plot.scatter(x="Rating", y="Time", alpha=0.5)
    df1["Rating"].plot()
    plt.show()
    await ctx.send(plt.show())

bot.run(TOKEN)