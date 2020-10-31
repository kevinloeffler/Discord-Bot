import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD_NAME')

bot = commands.Bot(command_prefix = ".")

# On Connection
@bot.event
async def on_ready():
    print("Bot is ready")

# Join notification
@bot.event
async def on_join(member):
    print("{m} has joined".format(m = member))

# Command
@bot.command()
async def ping(ctx):
    await ctx.send("Pong")

bot.run(TOKEN)
