import os
import random
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv

import Content

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD_NAME')

bot = commands.Bot(command_prefix = ".", help_command = None)

# On Connection
@bot.event
async def on_ready():
    await bot.change_presence(status = discord.Status.online, activity = discord.Game("Among Us"))
    print("Bot is ready to Rock and Roll!")

### Utility Commands

# Ping
@bot.command(aliases = ["alive"])
async def ping(ctx):
    await ctx.send("I'm al..ive, well and have a ping of " + str(round((bot.latency * 1000))) + "ms.")

# Help
@bot.command(aliases = ["h", "hilfe"])
async def help(ctx):
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
    pid = ctx.author.id
    responseCode = activeGame.addPlayer(pid)
    if responseCode == 0:
        await ctx.send("No more player instances available.")
    elif responseCode == -1:
        await ctx.send("You have already joined the game. Don't be greedy, leave some space for the rest.")
    else:
        await ctx.send("Joined as Player " + str(responseCode) + ". You can pick a color with '.pickColor'.")

# Leave
@bot.command()
async def leave(ctx):
    pid = ctx.author.id
    responseCode = activeGame.removePlayer(pid)
    if responseCode == 0:
        await ctx.send("You have not joined a game dummy.")
    else:
        await ctx.send("You left the game. Sad to see you leave... ")

# Pick Color
@bot.command()
async def pickColor(ctx):
    # Check if caller is a player
    isPlayer = False
    for player in activeGame.players:
        if ctx.author.id == player.id:
            isPlayer = True
    if isPlayer == False:
        await ctx.send("You need to join a game before you can pick a color.")
        return 1

    # Run Method
    message = await ctx.send("Pick a color:")
    # Set class variables for the reaction event
    activeGame.colorUser = ctx.author
    activeGame.colorMessage = message
    # Remove color
    for player in activeGame.players:
        if player.id == ctx.author.id:
            if player.color != None:
                oldColor = player.color.eid
                player.color = None
                for gc in activeGame.colors:
                    if gc.eid == oldColor:
                        gc.status = False
            break
    # Pick color
    for color in activeGame.colors:
        if color.status is False:
            emoji = bot.get_emoji(color.eid)
            await message.add_reaction(emoji)

@bot.event
async def on_reaction_add(reaction, user):
    # Only allow the active user to pick a color
    if reaction.message == activeGame.colorMessage and user == activeGame.colorUser:
        # Delete the first message to avoid confusion for other players
        await activeGame.colorMessage.delete()
        # Send confirmation
        await reaction.message.channel.send(str(user) + " picked  " + str(reaction))
        pickedColor = ''.join(c for c in str(reaction) if c.isdigit())
        for c in activeGame.colors:
            if c.eid == int(pickedColor):
                for p in activeGame.players:
                    if p.id == user.id:
                        p.pickColor(c)
                        c.status = True
                        break

# Free Colors

# Change Name
@bot.command()
async def test(ctx):
    m = ctx.author.color
    await ctx.send(m)

### Admin Commands

# Create Roles
@bot.command()
async def createRoles(ctx):
    for c in activeGame.colors:
        await ctx.guild.create_role(name = c.name, color = discord.Colour(c.value))
    await ctx.send("Roles Created.")

# Reset Roles
@bot.command()
async def resetRoles(ctx):
    for c in activeGame.colors:
        role = discord.utils.get(ctx.message.guild.roles, name=c.name)
        await role.delete()
    await ctx.send("Roles have been yeeted!")

# Restart Game
@bot.command()
async def resetGame(ctx):
    for player in activeGame.players:
        player.reset()
    await ctx.send("Game Reset. All data has been yeeted into oblivion...")

# Game Info
@bot.command()
async def gameInfo(ctx):
    playerCounter = 0
    for player in activeGame.players:
        if player.status:
            playerCounter += 1
    if playerCounter == 1:
        await ctx.send("There is 1 player in the lobby.")
    else:
        await ctx.send(f"There are {playerCounter} players in the lobby.")

# Player Info
@bot.command()
async def playerInfo(ctx, pid):
    validArguments = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    if pid in validArguments:
        player = activeGame.players[(int(pid) - 1)]
        await ctx.send(player.info())
    else:
        await ctx.send("ERROR: Choose a number between 1 and 10 as argument.")

@playerInfo.error
async def playerInfoError(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("ERROR: Choose a number between 1 and 10 as argument.")

# Die
@bot.command()
async def die(ctx):
    await ctx.send("How could you...")
    await bot.change_presence(status = discord.Status.offline)
    await ctx.bot.logout()

# Change Player Color

# Remove Player

### Fun

# Hi
@bot.command()
async def hi(ctx):
    if ctx.author.id == 354695565579255808:
        await ctx.send(random.choice(Content.Text.creatorMsg))
    else:
        await ctx.send(random.choice(Content.Text.message))


# Whos sus?

### Game Enviorenment

class Player:
    def __init__(self):
        self.status = False
        self.id = None
        self.color = None

    def pickColor(self, c):
        self.color = c

    def info(self):
        output = ""
        if self.status:
            output += "Status: Active\n"
            output += f"Player ID: {self.id}\n"
        else:
            output += "Status: Free\n"
        if self.color is None:
            output += "No Color Selected"
        else:
            output += f"Color: {self.color.name}"
        return output

    def reset(self):
        self.status = False
        self.id = None
        self.color = None

class GameColor:
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
    colorUser = None

    # Colors
    green = GameColor("Green", 0x127F2D, 772492810683023360)
    lime = GameColor("Lime", 0x52ED39, 772492810837295124)
    cyan = GameColor("Cyan", 0x38FEDC, 772492810623516702)
    blue = GameColor("Blue", 0x122ECF, 772492810615783484)
    purple = GameColor("Purple", 0x6B30BC, 772492810666246144)
    pink = GameColor("Pink", 0xEB54B9, 772492810422452235)
    red = GameColor("Red", 0xC51111, 772492810653794354)
    orange = GameColor("Orange", 0xF07D0D, 772492810850402324)
    yellow = GameColor("Yellow", 0xF3F457, 772492810347216897)
    brown = GameColor("Brown", 0x72491E, 772492810614997002)
    black = GameColor("Black", 0x181818, 772492810263855105)
    white = GameColor("White", 0xD8E1EE, 772492810782900224)
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
