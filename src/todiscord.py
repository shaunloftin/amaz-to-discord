# AMAZ-TO-DISCORD MONITORING
# WRITTEN BY: SHAUN LOFTIN
# github.com/shaunloftin
#
# todiscord.py

import discord

def notify(product_url, bot_key, affiliate_tag):
    client = discord.Client()
    token = bot_key
    
    @client.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(client))
        for channel in client.get_all_channels():
            if str(channel) == "bot-test":
                await channel.send("Back in stock: " + product_url + affiliate_tag)
    
    client.run(token)
    