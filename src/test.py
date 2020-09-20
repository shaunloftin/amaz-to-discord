import discord

credentials = []
with open('../data/credentials.txt', 'r') as file:
    for line in file:
        credentials.append(line)

client = discord.Client()

token = credentials[0]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    for channel in client.get_all_channels():
        if str(channel) == "bot-test":
            # await channel.send(f"""peepee poopoo check""")
            await channel.send("test")

client.run(token)