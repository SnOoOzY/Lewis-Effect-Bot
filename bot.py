from discord.ext import commands
import discord
import random
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
    await channel.send("Commands (case sensitive): \n!randomBall \n!lewisEffectOn \n!lewisEffectOff \n!image \n\nEnjoy")



# AUTO ADJECTIVE COMMAND / RANDOMBALL (8ball)

adjectives = ["attractive", "bald", "beautiful", "chubby", "clean", "dazzling", "drab", "elegant", "fancy", "fit", "fat", "flabby", "glamorous", "gorgeous", "handsome", "magnificent", "muscular", "skinny", "plain", "plump", "scruffy", "rizzy", "stocky", "unkempt", "unsightly", "agreeable", "ambitious", "brave", "calm", "delightful", "eager", "faithful", "gentle", "happy","angry", "sad", "lively", "nice", "mean", "witty", "fuckin stupid", "clumsy", "fierce", "grumpy", "helpless", "itchy", "stroking", "lubed up", "big", "colossal", "gigantic", "great", "huge", "immense", "large", "little", "mammoth", "tiny", "gay", "straight", "gang", "on gang this is", "on my mother", "im so gay... also", "im gay", "i wanna fuck", "is this", "was this", "salad bacon cheese oh my god", "flumpy", "plumpy", "fraser reminds me of", "raph reminds me of", "donald reminds me of", "clunie reminds me of", "cookies", "i really want cookies but i just wanna say that", "yummers", "3.1415926535897932", "women are kinda like", "men are kinda like", "women", "r", "maybe", "i do not know the answer to your question however i do have to say", "eh", "meh", "neh", "nah", "yea", "duh", "mmmmmeh", "huh? i thought", "huh?", "huh", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"]

effect = False
question = False
question_user_id = None

answers = ['yes', 'no', 'ask your mother', 'definitely', 'that is absolutely true', 'very no', 'absolutely not', 'not at all true', 'that is false', 'I do not care', 'this is not my business', 'and why is that my problem?', 'get raph to answer this idk', 'just because im an 8ball doesnt mean i can fix all of your problems', 'fuck you', 'why?', 'who?', 'how?', 'how does society accept this at all?', 'elon musk might have something to say about that', 'fuck off', 'gay', 'maybe ur just gay lol', 'come out already', 'this is so not right', 'nuh uh', 'yuh huh', 'perchance...']


@bot.event
async def on_message(message):
    global effect, question, question_user_id

    if message.author.bot:
        return
    
    if effect and message.author.id != bot.user.id:
        await message.channel.send(random.choice(adjectives) + " " + message.content)

    if question and message.author.id == question_user_id and message.author.id != bot.user.id:
        await message.channel.send("You asked: "+ message.content + "\nAnswer: " + random.choice(answers))
        question = False
        question_user_id = None

    await bot.process_commands(message)


@bot.command()
async def lewisEffectOn(ctx):
    global effect
    effect = True
    await ctx.send("Lewis effect is enabled.")

@bot.command()
async def lewisEffectOff(ctx):
    global effect
    effect = False
    await ctx.send("Lewis effect is disabled.")

@bot.command()
async def randomBall(ctx):
    global question, question_user_id
    question = True
    question_user_id = ctx.author.id
    await ctx.send(f'{ctx.author.name}, Ask me a question!')




# other commands idk


@bot.command()
async def image(ctx):
    await ctx.send(file=discord.File(r'C:/Users/lewis/Downloads/IMG_6847.jpg')) 


@bot.command()
async def commands(ctx):
    await ctx.send('Commands (case sensitive): \n!randomBall \n!lewisEffectOn \n!lewisEffectOff \n!image \n\nEnjoy')


# now im gonna try and make an 8 ball command like what i tried to do with typescript but failed massively


#abandoned code

"""@bot.command(
    name="test",
    description="test",
    guild=discord.Object(id=12417128931)
)
async def test_command(interaction):
    await interaction.response.send_message("test yes")"""




bot.run(TOKEN)

# to run type "python bot.py"