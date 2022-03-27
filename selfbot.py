import discord
from discord.ext import commands
import asyncio
import random

TOKEN = ""
client = commands.Bot(command_prefix=("."), self_bot=True)
phrases = [
    "feur",
    "feur",
    "feur",
    "feur",
    "feur",
    "feur",
    "feur",
    "feur",
    "feur",
    "feur",
    "feur",
    "feur",
    "feur je crois",
    "feur je pense",
    "feur, mais je suis pas sûr",
    "feur, mais à vérifier",
    "feur sans doute",
    "comme ça spontanément je dirais feur, mais information à vérifier"
]

@client.event
async def on_ready():
    print('cum')

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    message_content = str(message.content)
    channel = str(message.channel.name)
    server = str(message.guild.name)
    
    print(f'[{server}] -> ({channel}) {username}: {message_content}')
    
    if message.author == client.user:
        return

    text = message.content.lower()

    if 'quoi' in text:
        text = text.rstrip(" ?!.,§;/:")
    
    if text.endswith('quoi'):
        async with message.channel.typing():
            await asyncio.sleep(0.1)
        await message.channel.send(random.choice(phrases))
        return

client.run(TOKEN)