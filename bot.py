from discord.ext import commands
import discord
import array as arr
import random
import sys

import os
from dotenv import load_dotenv 

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client(intents=discord.Intents.default())

CHANNEL_ID = 947902507437391924

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


IDs = ["480047238123487244", "285076009168928769", "787063772351037450", "702175304709570661", "682701719704043526", "643110608358866964", "743862901412069446", "766973033767239710", "502889074462294016", "734266946224390184", "1086006930587267225", "1086006930587267225", "1086006930587267225", "510819042836217873", "713730351553577032"]

@bot.event
async def on_ready():
    print("im ready for it baby")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Sigma!")

@bot.command()
async def hello(ctx):
    await ctx.send("hello, I want you.")



@bot.event
async def on_message(message):
    if message.author.id == type(int(IDs[int])):
        await message.channel.send(message.content + " AUGHHHHH")




client.run(TOKEN)

# to run type "python bot.py"