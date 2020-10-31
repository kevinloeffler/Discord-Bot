import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD_NAME')

client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    print("Bot is Ready")

@client.event
async def on_message(message):
    print("{aut}: {mes}".format(aut = message.author, mes = message.content))

client.run(TOKEN)
