import os
import discord
import random
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD_NAME')

client = discord.Client()

### Set up:
globalDelimiter = '.'

### Messages
def commands(input):
    pass


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!\n')


@client.event
async def on_message(message):
    # Important check: prevents recursion
    if message.author != client.user:
        if message.content[0] == globalDelimiter:
            await message.channel.send('command recived')
            print('response sent')

client.run(TOKEN)
