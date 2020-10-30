import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD_NAME')

client = discord.Client()

### Set up:
bot = commands.Bot(command_prefix='.')

### Messages
def commandsCMD(input):
    if input == '.start':
        pass
    elif input == '.join':
        pass
    elif input == '.sus':
        pass


@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds)
    print("Bot " + bot.user.name + " connected to " + guild.name)
    print("With the ID: " + str(bot.user.id) + "\n")

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

@bot.event
async def on_message(message):
    pass

bot.run(TOKEN)
