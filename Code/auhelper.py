import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD_NAME')


### Set up:
client = discord.Client()
bot = commands.Bot(command_prefix='.')
# guild = discord.utils.get(client.guilds)
guild = client.guilds
print(guild)


@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds)
    await guild.send("Connected")
    print("Bot " + bot.user.name + " connected to " + guild.name)
    print("With the ID: " + str(bot.user.id) + "\n")

@bot.event
async def on_disconnect():
    await guild.send("Disconnected")
    print("Bot " + bot.user.name + " disconnected from " + guild.name)

@client.event
async def on_message(message):
    if message == "version":
        myEmbed = discord.Embed(title = 'Current Version', description = "Version 1.0", color = "0x00ff00")
        myEmbed.add_field(name = "Version Code:", value = "v1.0.0", inline = false)
        myEmbed.set_footer(text = "Sample Footer")
        await guild.send(embed = myEmbed)

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

client.run(TOKEN)
# bot.run(TOKEN)
