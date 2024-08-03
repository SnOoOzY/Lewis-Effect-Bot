from discord.ext import commands
import discord
import array as arr
import random
import sys
import os
from dotenv import load_dotenv 
from discord import app_commands

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

CHANNEL_ID = 947902507437391924
# client = commands.Bot(command_prefix="!", intents=discord.Intents.all()) 
# tree = app_commands.CommandTree(client)

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("im ready")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("yo")



# AUTO ADJECTIVE COMMAND

adjectives = ["attractive", "bald", "beautiful", "chubby", "clean", "dazzling", "drab", "elegant", "fancy", "fit", "fat", "flabby", "glamorous", "gorgeous", "handsome", "magnificent", "muscular", "skinny", "plain", "plump", "scruffy", "rizzy", "stocky," "unkempt", "unsightly", "agreeable", "ambitious", "brave", "calm", "delightful", "eager", "faithful", "gentle", "happy","angry", "sad", "lively", "nice", "mean", "witty", "fuckin stupid", "clumsy", "fierce", "grumpy", "helpless", "itchy", "stroking", "lubed up", "big" "colossal" "gigantic", "great", "huge", "immense", "large", "little", "mammoth", "tiny", "gay", "straight", "gang", "on gang this is", "on my mother", "im so gay... also", "im gay", "i wanna fuck", "is this", "was this", "salad bacon cheese oh my god", "flumpy", "plumpy", "fraser reminds me of", "raph reminds me of", "donald reminds me of", "clunie reminds me of", "cookies", "i really want cookies but i just wanna say that", "yummers", "3.1415926535897932", "women are kinda like", "men are kinda like", "women", "r", "maybe", "i do not know the answer to your question however i do have to say", "eh", "meh", "neh", "nah", "yea", "duh", "mmmmmeh", "huh? i thought", "huh?", "huh", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"]

effect = False

@bot.event
async def on_message(message):
    if message.author.id != 1268327369459105885 & effect == True:
            await message.channel.send(random.choice(adjectives) + " " + message.content)

@bot.command()
async def lewisEffect(ctx):
    await ctx.send("I am now listening")
    effect == True



@bot.command()
async def hello(ctx):
    await ctx.send("yo")


@bot.command()
async def image(ctx):
    await image.channel.send(file=discord.File('IMG_6847'))


"""@bot.command(
    name="test",
    description="test",
    guild=discord.Object(id=12417128931)
)
async def test_command(interaction):
    await interaction.response.send_message("test yes")"""




bot.run(TOKEN)

# to run type "python bot.py"