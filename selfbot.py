import discord
from discord.ext import commands
import asyncio

TOKEN = "enter yourt discord token here"
client = commands.Bot(command_prefix=("."), self_bot=True)
ponctuation = ['?','!',' ','.',',']

@client.event
async def on_ready():
    print('cum')

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    message_content = str(message.content)
    channel = str(message.channel.name)
    
    print(f'{username}: {message_content} ({channel})')
    
    if message.author == client.user:
        return
    
    text = message.content
    text = text.lower()

    if 'quoi' in text:
        for i in ponctuation:
            text = text.replace(i,'')
    
    if text.endswith('quoi'):
        async with message.channel.typing():
            await asyncio.sleep(0.125)
        await message.channel.send('feur')
        return

client.run(TOKEN)