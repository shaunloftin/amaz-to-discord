# AMAZ-TO-DISCORD MONITORING
# WRITTEN BY: SHAUN LOFTIN
# github.com/shaunloftin
#
# main.py

import amazon
import todiscord
import error

import time

with open('../data/credentials.txt', 'r') as file:
    bot_key = file.readline()

try:
    while True:
        print(1)
        product_urls = amazon.get_product_urls('../data/products.txt')
        print(2)
        original_status = amazon.get_original_status('../data/status.txt')
        print(3)
        updated_status = amazon.get_updated_status(product_urls)
        
        for x in range(0, len(updated_status)):
            if updated_status[x] == 'available' and original_status[x] != 'available':
                todiscord.notify(product_urls[x], bot_key)
    
        time.sleep(30)
except Exception:
    error.err_report(Exception)

