# bot.py
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
#intents for messaging and defualts
intents = discord.Intents.default()
intents.message_content = True

#passing the intents to the client and creating it

#bot creation
bot = commands.Bot(command_prefix='!',intents=intents)
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def rngU(ctx, arg: int):
        await ctx.send(arg)
@bot.command()
async def rngH(ctx, arg: int):
        await ctx.send(arg)
        await ctx.send(ctx.message.created_at)
    
bot.run(TOKEN)