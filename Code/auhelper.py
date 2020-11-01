import os
import random
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv

import Content

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD_NAME')

bot = commands.Bot(command_prefix = ".")
admin = commands.Bot(command_prefix = "..")

# On Connection
@bot.event
async def on_ready():
    await bot.change_presence(status = discord.Status.online, activity = discord.Game("Among Us"))
    print("Bot is ready")

### Utility Commands

# Ping
@bot.command()
async def ping(ctx):
    await ctx.send(round((bot.latency * 1000), 2))

# Help
@bot.command()
async def h(ctx):
    helpEmbed = discord.Embed()
    helpEmbed.add_field(name = "How to use this bot", value = Content.Help.howToPlay, inline = False)
    helpEmbed.add_field(name = "Commands", value = Content.Help.commands, inline = False)
    await ctx.send(embed = helpEmbed)

# About
@bot.command()
async def about(ctx):
    aboutEmbed = discord.Embed(title = 'Among Us Helper')
    aboutEmbed.add_field(name = "Version", value = Content.Help.version, inline = True)
    aboutEmbed.add_field(name = "Release", value = Content.Help.release, inline = True)
    aboutEmbed.add_field(name = "Source Code", value = Content.Help.source, inline = False)
    aboutEmbed.set_footer(text = "Developed by Kevin Loeffler, distributed under the MIT License")
    await ctx.send(embed = aboutEmbed)

### Game Commands

# Join

# Leave

# Pick Color

# Change Name


### Admin Commands

# Start Game

# End Game

# Change Player Color

# Remove Player

# Random Colors

### Game Enviorenment



# Error Handling
# @bot.event
# async def on_command_error(ctx, error):
#    if isinstance(error, commands.CommandNotFound):
#        await ctx.send("Invalid Command: Type .h for a list of all commands")
#    elif isinstance(error, commands.MissingRole):
#        await ctx.send("Missing Role: You have to be an Admin to use '..' commands")

bot.run(TOKEN)
