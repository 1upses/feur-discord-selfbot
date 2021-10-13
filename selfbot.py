import discord
from discord.ext import commands
import asyncio

TOKEN = ""
client = commands.Bot(command_prefix=("."), self_bot=True)

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
    
    end_mess = message.content.endswith
    
    if end_mess('quoi') or end_mess('quoi ?') or end_mess('quoi?') or end_mess('Quoi'):
        async with message.channel.typing():
            await asyncio.sleep(0.125)
        await message.channel.send('feur')
        return

client.run(TOKEN)