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


@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds)
    print("Bot " + bot.user.name + " connected to " + guild.name)
    print("With the ID: " + str(bot.user.id) + "\n")

@bot.command()
async def test(ctx):
    await ctx.send('testing')

@bot.command(name = 'admin')
@commands.has_role('admin')
async def admin(ctx):
    await ctx.send('allowed')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')

bot.run(TOKEN)
