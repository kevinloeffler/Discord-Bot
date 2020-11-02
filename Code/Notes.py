# Interesting Stuff:

# Measure Latency
print("\n" + str(client.latency))

# Print all users
print(client.users)
# or
members = '\n - '.join([member.name for member in guild.members])
print(f'Guild Members:\n - {members}')

# Check connected Guilds
for guild in client.guilds:
    if guild.name == GUILD:
        break

print(
    f'{client.user} is connected to the following guild:\n'
    f'{guild.name}(id: {guild.id})\n'
)

# Respond to a message
if message.content == '99!':
    response = '99!'
    await message.channel.send(response)

# Sending an embed
@client.event
async def on_message(message):
    if message == "version":
        myEmbed = discord.Embed(title = 'Current Version', description = "Version 1.0", color = "0x00ff00")
        myEmbed.add_field(name = "Version Code:", value = "v1.0.0", inline = false)
        myEmbed.set_footer(text = "Sample Footer")
        await guild.send(embed = myEmbed)

# Message Logger
@bot.event
async def on_message(message):
    print("{aut}: {mes}".format(aut = message.author, mes = message.content))

# Join notification
@bot.event
async def on_member_join(member):
    print("{m} has joined".format(m = member))

# Left notification
@bot.event
async def on_member_remove(member):
    print("{m} has left".format(m = member))

# Info command
@bot.command()
async def info(ctx):
    await ctx.send(ctx.author)
    print(ctx.author)
    await ctx.send(ctx.channel)
    print(ctx.channel)
    await ctx.send(ctx.guild)
    print(ctx.guild)

# Command not found
@bot.command()
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Invalid Command. Type .h for a list of all commands")

# Role Check
@commands.has_role("Admin")
pass

@bot.command()
async def text(ctx):
    msg = await ctx.channel.send(' the text ')
    await msg.add_reaction('👍')

@client.event
async def on_reaction_add(reaction, user):
    if reaction.emoji('👍'):
        await reaction.channel.send('Test')
