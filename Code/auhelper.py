import os
import random
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD_NAME')

bot = commands.Bot(command_prefix = ".")

# On Connection
@bot.event
async def on_ready():
    await bot.change_presence(status = discord.Status.online, activity = discord.Game("Among Us"))
    print("Bot is ready")

# Ping
@bot.command()
async def ping(ctx):
    await ctx.send(round((bot.latency * 1000), 2))

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Invalid Command: Type .h for a list of all commands")
    elif isinstance(error, commands.MissingRole):
        await ctx.send("Missing Role: You have to be an Admin to use '..' commands")

bot.run(TOKEN)
