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
@bot.command()
async def join(ctx):
    pid = str(ctx.author)
    responseCode = activeGame.addPlayer(pid)
    if responseCode == 0:
        await ctx.send("No more player instances available.")
    elif responseCode == -1:
        await ctx.send("You have already joined the game.")
    else:
        await ctx.send("Joined as Player " + str(responseCode) + ".")

# Leave
@bot.command()
async def leave(ctx):
    pid = str(ctx.author)
    responseCode = activeGame.removePlayer(pid)
    if responseCode == 0:
        await ctx.send("You have not joined a game.")
    else:
        await ctx.send("You left the game.")

# Pick Color
@bot.command()
async def pickColor(ctx):
    message = await ctx.send("Pick a color:")
    activeGame.colorMessage = message
    for color in activeGame.colors:
        if color.status is False:
            emoji = bot.get_emoji(color.eid)
            await message.add_reaction(emoji)

@bot.event
async def on_reaction_add(reaction, user):
    if reaction.message == activeGame.colorMessage:
        await reaction.message.channel.send(str(user) + "reacted")

# Change Name


### Admin Commands

# Start Game

# End Game

# Game Info

# Player Info

# Change Player Color

# Remove Player

# Random Colors

### Game Enviorenment

class Player:
    def __init__(self):
        self.status = False
        self.id = None
        self.color = None

    def pickColor(self, c):
        self.color = c

    def reset(self):
        self.status = False
        self.id = None
        self.color = None

class Color:
    def __init__(self, name, value, eid):
        self.name = name
        self.value = value
        self.eid = eid
        self.status = False

class Game:
    id = 111
    # Create Empty Players
    player1, player2, player3, player4, player5, player6, player7, player8, player9, player10 = Player(), Player(), Player(), Player(), Player(), Player(), Player(), Player(), Player(), Player()
    players = [player1, player2, player3, player4, player5, player6, player7, player8, player9, player10]
    colorMessage = None

    # Colors
    green = Color("Green", 0x127F2D, 772492810683023360)
    lime = Color("Lime", 0x52ED39, 772492810837295124)
    cyan = Color("Cyan", 0x38FEDC, 772492810623516702)
    blue = Color("Blue", 0x122ECF, 772492810615783484)
    purple = Color("Purple", 0x6B30BC, 772492810666246144)
    pink = Color("Pink", 0xEB54B9, 772492810422452235)
    red = Color("Red", 0xC51111, 772492810653794354)
    orange = Color("Orange", 0xF07D0D, 772492810850402324)
    yellow = Color("Yellow", 0xF3F457, 772492810347216897)
    brown = Color("Brown", 0x72491E, 772492810614997002)
    black = Color("Black", 0x181818, 772492810263855105)
    white = Color("White", 0xD8E1EE, 772492810782900224)
    colors = [green, lime, cyan, blue, purple, pink, red, orange, yellow, brown, black, white]

    def addPlayer(ctx, pid):
        counter = 0
        for p in Game.players:
            counter += 1
            if p.status is False:
                p.id = pid
                p.status = True
                return counter
            elif p.id == pid:
                return -1
        return 0

    def removePlayer(ctx, pid):
        for p in Game.players:
            if p.id == pid:
                p.reset()

activeGame = Game()

# Error Handling
# @bot.event
# async def on_command_error(ctx, error):
#    if isinstance(error, commands.CommandNotFound):
#        await ctx.send("Invalid Command: Type .h for a list of all commands")
#    elif isinstance(error, commands.MissingRole):
#        await ctx.send("Missing Role: You have to be an Admin to use '..' commands")

bot.run(TOKEN)
