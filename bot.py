import discord
from discord import app_commands
from discord.ext import commands
import random
import os
from dotenv import load_dotenv 


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
    try:
        synced = await bot.tree.sync()
        await channel.send("Commands (case sensitive): \n!randomBall \n!lewisEffectOn \n!lewisEffectOff \n!image \n\nEnjoy")
    except Exception as e:
        print(e)



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


@bot.tree.command(name='test')
async def test(interaction: discord.Interaction):
    await interaction.response.sent_message(f'Hey')


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



bot.run(TOKEN)

    # to run type "python bot.py"
