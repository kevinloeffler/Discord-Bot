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

# Sending an Invite
@client.event
async def on_message(message):
    if message == "version":
        myEmbed = discord.Embed(title = 'Current Version', description = "Version 1.0", color = "0x00ff00")
        myEmbed.add_field(name = "Version Code:", value = "v1.0.0", inline = false)
        myEmbed.set_footer(text = "Sample Footer")
        await guild.send(embed = myEmbed)
