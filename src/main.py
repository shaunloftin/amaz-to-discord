# AMAZ-TO-DISCORD MONITORING
# WRITTEN BY: SHAUN LOFTIN
# github.com/shaunloftin
#
# main.py

import amazon
import todiscord
# import error

import time
import timeit

with open('../data/credentials.txt', 'r') as file:
    bot_key = file.readline()

try:
    while True:
        start = timeit.default_timer()
        product_urls = amazon.get_product_urls('../data/products.txt')
        original_status = amazon.get_original_status('../data/status.txt')
        updated_status = amazon.get_updated_status(product_urls)
        
        for x in range(0, len(updated_status)):
            if updated_status[x] == 'available' and original_status[x] != 'available':
                todiscord.notify(product_urls[x], bot_key)
        
        stop = timeit.default_timer()
        print('and i sleep - loop time: ' + str(stop-start)) 
        time.sleep(15)

except Exception as err:
    # error.err_report(Exception)
    print('error lol'+err)

