# AMAZ-TO-DISCORD MONITORING
# WRITTEN BY: SHAUN LOFTIN
# github.com/shaunloftin
#
# main.py

import amazon
import error

import discord
import time
import timeit

with open('../data/credentials.txt', 'r') as file:
    bot_key = file.readline()
    affiliate_tag = file.readline()
    channel_alerts_id = int(file.readline())
    channel_status_id = int(file.readline())

try:
    client = discord.Client()
    token = bot_key
    
    product_urls = amazon.get_product_urls('../data/products.txt')
    original_status = amazon.get_original_status('../data/status.txt')
    
    @client.event
    async def on_ready():
        channel_alerts = client.get_channel(channel_alerts_id)
        channel_status = client.get_channel(channel_status_id)
        
        while True:
            start = timeit.default_timer()
            updated_status = amazon.get_updated_status(product_urls)
            
            for x in range(0, len(updated_status)):
                if updated_status[x] == 'available' and original_status[x] != 'available':
                    await channel_alerts.send("Back in stock: " + product_urls[x] + affiliate_tag)
            
            original_status = updated_status
            stop = timeit.default_timer()
            report = 'Success. Runtime: ' + str(stop-start)
            error.log(report) 
            await channel_status.send(report)
            time.sleep(15)
    
    client.run(token)

except Exception as e:
    email_success = error.err_report(e)
    if email_success != 0:
        error.log(email_success)
    error.log(e)
