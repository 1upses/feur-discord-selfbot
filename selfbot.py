import discord
from discord.ext import commands
import asyncio

TOKEN = "enter your token here"
client = commands.Bot(command_prefix=("."), self_bot=True)

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
        await message.channel.send('feur')
        return

client.run(TOKEN)