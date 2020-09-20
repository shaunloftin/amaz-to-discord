# AMAZ-TO-DISCORD MONITORING
# WRITTEN BY: SHAUN LOFTIN
# github.com/shaunloftin
#
# todiscord.py

import discord

def notify(product_url):
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
                await channel.send("Back in stock: " + product_url)
    
    client.run(token)
    