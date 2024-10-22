import asyncio
from asyncio import tasks
import discord
from discord.ext import tasks
import openai
from discord import FFmpegPCMAudio, app_commands
from discord.ext import commands
import random
import os
from dotenv import load_dotenv 
import time
from datetime import datetime

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')


CHANNEL_ID = 947902507437391924
# client = commands.Bot(command_prefix="!", intents=discord.Intents.all()) 
# tree = app_commands.CommandTree(client)

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())




@bot.event
async def on_ready():
    print("im ready")
    bigBenAUTO.start()
    channel = bot.get_channel(CHANNEL_ID)
    
    try:
        await channel.send("Commands (case sensitive): \n!randomBall \n!lewisEffectOn \n!lewisEffectOff \n!image \n\nEnjoy")
    except Exception as e:
        print(e)



# AUTO ADJECTIVE COMMAND / RANDOMBALL (8ball)

adjectives = ["attractive", "bald", "beautiful", "chubby", "clean", "dazzling", "drab", "elegant", "fancy", "fit", "fat", "flabby", "glamorous", "gorgeous", "handsome", "magnificent", "muscular", "skinny", "plain", "plump", "scruffy", "rizzy", "stocky", "unkempt", "unsightly", "agreeable", "ambitious", "brave", "calm", "delightful", "eager", "faithful", "gentle", "happy","angry", "sad", "lively", "nice", "mean", "witty", "fuckin stupid", "clumsy", "fierce", "grumpy", "helpless", "itchy", "stroking", "lubed up", "big", "colossal", "gigantic", "great", "huge", "immense", "large", "little", "mammoth", "tiny", "gay", "straight", "gang", "on gang this is", "on my mother", "im so gay... also", "im gay", "i wanna fuck", "is this", "was this", "salad bacon cheese oh my god", "flumpy", "plumpy", "fraser reminds me of", "raph reminds me of", "donald reminds me of", "clunie reminds me of", "cookies", "i really want cookies but i just wanna say that", "yummers", "3.1415926535897932", "women are kinda like", "men are kinda like", "women", "r", "maybe", "i do not know the answer to your question however i do have to say", "eh", "meh", "neh", "nah", "yea", "duh", "mmmmmeh", "huh? i thought", "huh?", "huh", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"]

effect = False
question = False
question_user_id = None
measure = False
suffixOn = False
timerOn = False
guessTheNumOn = False
gptQuestion = False

answers = ['yes', 'no', 'ask your mother', 'definitely', 'that is absolutely true', 'very no', 'absolutely not', 'not at all true', 'that is false', 'I do not care', 'this is not my business', 'and why is that my problem?', 'get raph to answer this idk', 'just because im an 8ball doesnt mean i can fix all of your problems', 'fuck you', 'why?', 'who?', 'how?', 'how does society accept this at all?', 'elon musk might have something to say about that', 'fuck off', 'gay', 'maybe ur just gay lol', 'come out already', 'this is so not right', 'nuh uh', 'yuh huh', 'perchance...']


@bot.event
async def on_message(message):
    global effect, question, question_user_id, measure, suffixOn, timerOn, guessTheNumOn, gptQuestion, messages

    if message.author.bot:
        return
    
    if effect and message.author.id != bot.user.id:
        await message.channel.send(random.choice(adjectives) + " " + message.content)

    if question and message.author.id == question_user_id and message.author.id != bot.user.id:
        await message.channel.send("You asked: "+ message.content + "\nAnswer: " + random.choice(answers))
        question = False
        question_user_id = None
    



    if measure and message.author.id != bot.user.id:
        await message.channel.send('The length of ' + message.content + ' is ' + str(random.randint(0, 5000)) + ' ' + random.choice(measurements))
        measure = False

    if suffixOn and message.author.id != bot.user.id:
        await message.channel.send(message.content + random.choice(suffix))

    if guessTheNumOn and message.author.id != bot.user.id:
        userGuess = int(message.content.lower())
        randomNum = random.randint(0, 40)
    
        while timerOn:
            if userGuess == randomNum:
                await message.channel.send('Congrats, you win!')
                guessTheNumOn  = False
                timerOn = False
            else: 
                await print(userGuess)
        await message.channel.send(f'You lose! The number was {randomNum}')
        guessTheNumOn  = False

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


@bot.command()
async def askGPT(message):
    global gptQuestion, question_user_id
    gptQuestion = True
    question_user_id = message.author.id
    await message.channel.send(f'{message.author.name}, ask ChatGPT a question!')

# other commands idk


@bot.command()
async def image(ctx):
    await ctx.send(file=discord.File(r'C:/Users/lewis/Downloads/IMG_6847.jpg')) 


@bot.tree.command(name='commands', description='List of all commands')
async def commands(interaction: discord.Interaction):
    await interaction.send('Commands (case sensitive): \n!randomBall \n!lewisEffectOn \n!lewisEffectOff \n!image \n!inger \n!ingerOff \n!blackJack \n!ruler \n!guessTheNum  \n \n\nEnjoy')


@bot.tree.command(name='test', description='tests slash commands')
async def test(interaction: discord.Interaction):
    await interaction.response.send_message('Hey')


# Blackjack

user_tokens = 50


cards = {'Ace' : 1, '2' : 2, '3' : 3, '4' : 4, '5': 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9, '10' : 10, 'Jack' : 10, 'Queen' : 10, 'King' : 10}
deck = list(cards.keys()) * 4
random.shuffle(deck)

def deal_card(deck):
    return deck.pop()


player_hand = []
dealer_hand = []

player_hand.append(deal_card(deck))
player_hand.append(deal_card(deck))


dealer_hand.append(deal_card(deck))
dealer_hand.append(deal_card(deck))


def display_hands(player_hand, dealer_hand, reveal_dealer = False):
    player_display = ', '.join(player_hand)
    player_total = calculate_hand(player_hand)
    dealer_total = calculate_hand(dealer_hand)

    if reveal_dealer:
        dealer_display = ', '.join(dealer_hand)
        return (f'Players hand: {player_display} (Total: {player_total})\n'
                f'Dealers hand: {dealer_display} (Total: {dealer_total})')
    else:
        dealer_display = dealer_hand[0] + ', [Hidden]'
    return (f'Players hand: {player_display} (Total: {player_total})\n'
            f'Dealers hand: {dealer_display}')

def calculate_hand(hand):
    value = 0
    aces = 0

    for card in hand:
        value += cards[card]
        if card == 'Ace':
            aces += 1

    while value <= 11 and aces > 0:
        value += 10
        aces -= 1

    return value


@bot.command()
async def blackJack(ctx):
    player_hand = []
    dealer_hand = []
    global user_tokens
    user_tokens -= 5
    
    # Initial deal
    player_hand.append(deal_card(deck))
    player_hand.append(deal_card(deck))
    
    dealer_hand.append(deal_card(deck))
    dealer_hand.append(deal_card(deck))
    
    await ctx.send(display_hands(player_hand, dealer_hand))
    
    while True:
        await ctx.send('User tokens: ' + str(user_tokens) + '\nHit or Stand?')

        global msg
        global check

        def check(msg):
            return msg.author == ctx.author and msg.content.lower() in ['hit', 'stand']
        
        
        msg = await bot.wait_for('message', check=check)

        if msg.content.lower() == 'hit':
            player_hand.append(deal_card(deck))
            await ctx.send(display_hands(player_hand, dealer_hand))
            
            if calculate_hand(player_hand) > 21:
                await ctx.send('You bussssed! losaaaah')
                return
        else:
            break

    while calculate_hand(dealer_hand) < 17:
        dealer_hand.append(deal_card(deck))

        await ctx.send(display_hands(player_hand, dealer_hand, reveal_dealer=True))

        player_total = calculate_hand(player_hand)
        dealer_total = calculate_hand(dealer_hand)

        if dealer_total > 21:
            await ctx.send('you won fuck u')
            user_tokens += 10
        elif player_total > dealer_total:
            await ctx.send('you won fuck u')
            user_tokens += 10
        elif player_total < dealer_total:
            await ctx.send('LMFAOOOO I WON AHHAHAHAHAHA')
        else:
            await ctx.send('its a.. tie? idk get ur money back')
            user_tokens += 5

        return


measurements = ['kilometres', 'miles', 'hamburgers', 'crocodiles', 'bald eagles', 'centimetres', 'millimetres', 'metres', 'megametres', 'AU', 'lightyears', 'nanometres', 'feet', 'yards', 'toes', 'seconds', 'minutes', 'years', 'tomorrows']


@bot.command()
async def ruler(message):
    await message.channel.send('What would you like to measure?')
    global measure
    measure = True


suffix = ['ing', 'nd' 'st', 'rd', 'th', 'ed', 'ily', 's', 'ist' 'ance', 'ible', 'ous', 'some', 'ery', 'ess', 'ish']

@bot.command()
async def inger(message):
    await message.channel.send('I will now take every single message and add something to the end yk')
    global suffixOn
    suffixOn = True

@bot.command()
async def ingerOff(message):
    await message.channel.send('NUH UH ITS OFF NOOOOOOO')
    global suffixOn
    suffixOn = False


@bot.command()
async def guessTheNum(message):
    global guessTheNumOn, timerOn
    guessTheNumOn = True 
    await message.channel.send('RULES: \nThe player will have 20 seconds to guess the right number (between 1 - 40)\nYour time begins in 3 seconds')
    time.sleep(3)
    timerOn = True
    await message.channel.send('go go go!')
    
    
    async def timer():
        global timerOn
        s = 25
        while s > 0:
            timer = datetime.timedelta(seconds = s)
            print(timer)
            time.sleep(1)
            s -= 1
        print('balls')
        timerOn = False

    if timerOn:
        await timer()

@tasks.loop(seconds=1)
async def bigBenAUTO():

    time_now = datetime.now().strftime("%H:%M:%S")

    if time_now in ["00:00:00", "01:00:00", "02:00:00", "03:00:00", "04:00:00", "05:00:00" "06:00:00", "07:00:00", "08:00:00", "09:00:00", "10:00:00", "11:00:00", "12:00:00", "13:00:00", "14:00:00", "15:00:00", "16:00:00", "17:00:00", "18:00:00", "19:00:00", "20:00:00", "21:00:00", "22:00:00", "23:00:00"]: 

        channel = bot.get_channel(1150868133582737529)

        if channel is not None and channel.guild.voice_client is None:
            print(f"Connecting to voice channel: {channel.name}")
            voice_client = await channel.connect()

            try:
                source = FFmpegPCMAudio('C:/Users/lewis/Downloads/bigbenny.mp3')
                voice_client.play(source, after=lambda e: print(f"Playback finished: {e}" if e else "Playback finished."))
                
                while voice_client.is_playing():
                    await asyncio.sleep(1) 
                
                await voice_client.disconnect()

            except Exception as e:
                print(f"Error: {e}")
                if voice_client.is_connected():
                    await voice_client.disconnect()

@bot.command()
async def bigBen(ctx):
    if ctx.author.voice:
        voice_channel = ctx.author.voice.channel
        voice_client = await voice_channel.connect()

        try:
            source = FFmpegPCMAudio('C:/Users/lewis/Downloads/bigbenny.mp3')
            voice_client.play(source, after=lambda e: print(f'Playback finished: {e}' if e else 'Playback finished.'))
            
            while voice_client.is_playing():
                    await asyncio.sleep(1) 
            
            await voice_client.disconnect()
        except Exception as e:
                print(f'Error: {e}')
                await voice_client.disconnect()
        else:
            await ctx.send('You are not connected to a voice channel.')


@bot.command()
async def espresso(ctx):
    if ctx.author.voice:
        voice_channel = ctx.author.voice.channel
        voice_client = await voice_channel.connect()

        try:
            source = FFmpegPCMAudio('C:/Users/lewis/Downloads/espresso.mp3')
            voice_client.play(source, after=lambda e: print(f'Playback finished: {e}' if e else 'Playback finished.'))

            while voice_client.is_playing():
                await asyncio.sleep(1)

            await voice_client.disconnect()
        except Exception as e:
            print(f'Error: {e}')
            await voice_client.disconnect()
        else:
            await ctx.send('lemesso')



bot.run(TOKEN)

# to run type "python bot.py"
