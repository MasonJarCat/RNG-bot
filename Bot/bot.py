# bot.py
import os
from discord.ext import commands
import discord
from dotenv import load_dotenv
import numpy as np
import pandas as pd
import matplotlib as plt
from datetime import datetime as dt
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
#intents for messaging and defualts
intents = discord.Intents.default()
intents.message_content = True

#passing the intents to the client and creating it
#creates file 
file = "Bot\Hans.xlsx"
#creates dataframe

df1 = pd.read_excel(file, sheet_name='Hans',engine = "openpyxl")  
df2 = pd.read_excel(file, sheet_name='Urban',engine = "openpyxl")  

#df1['Date'] = df1['Date'].astype('datetime64[ns]')
#[datetime.date(2022, 11, 17)]
df1['Date'] = pd.to_datetime(df1['Date'], format='[datetime.date(%Y, %m, %d)]')


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

        dti = pd.to_datetime([ctx.message.created_at])
        dti = dti.tz_convert("US/Eastern")
        df2.loc[len(df2.index)] = [arg, dti.date, dti.time, dti.day_name()] 
#populates array
@bot.command()
async def rngH(ctx, arg: int):
        await ctx.send(arg)

        dti = pd.to_datetime([ctx.message.created_at])
        dti = dti.tz_convert("US/Eastern")
        df1.loc[len(df1.index)] = [arg, dti.date, dti.time, dti.day_name()] 
       # await ctx.send(df1)
       # print(df1)

#gets average
@bot.command()
async def hansOverall(ctx):
    var = 0
    strI = "Average Hans Rating Today:"
    for x in range(len(df1.index)):
        var = var + df1.loc[x,"Rating"]
    var = var / len(df1.index)
    strI = " ".join([strI,str(var)])
    await ctx.send(strI)

@bot.command()
async def hansA(ctx):
    var = 0
    count = 0
    strI = "Average Hans Rating Today:"
    today = dt.today()
    for x in range(len(df1.index)):
      #  print("DF: " + df1.loc[x,"Date"])
       # print("Date: " + today.date())
        if df1.loc[x,"Date"] == today.date():
            var += df1.loc[x,"Rating"]
            count += 1
            print("EQUALS at " + str(x))
    var = var / count
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
async def saveH(ctx):
    #for x in range(len(df1.index)):
    df1["Date"]= df1["Date"].astype(str)
      #  df1.loc[x,"Time"]= df1.loc[x,"Time"].astype('int64')
      # openpyxl
    with pd.ExcelWriter(file, mode="a",if_sheet_exists="replace",engine = "openpyxl") as writer:
        df1.to_excel(writer, sheet_name="Hans", index=False)
    await ctx.send("Saved")

@bot.command()
async def saveU(ctx):
    with pd.ExcelWriter(file, mode="a",if_sheet_exists="replace",engine = "openpyxl") as writer:
        df2.to_excel(writer, sheet_name="Urban", index=False)
    await ctx.send("Saved")
#broken do NOT use  
@bot.command()
async def getGGraph(ctx):
   # df1.plot.scatter(x="Rating", y="Time", alpha=0.5)
    df1["Rating"].plot()
    plt.show()
    await ctx.send(plt.show())


bot.run(TOKEN)