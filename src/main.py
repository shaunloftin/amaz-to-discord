# AMAZ-TO-DISCORD MONITORING
# WRITTEN BY: SHAUN LOFTIN
# github.com/shaunloftin
#
# main.py

import amazon
import todiscord
from error import err_report

from datetime import datetime
import time
import timeit

def log(e):
    with open('../data/log.txt', 'a') as file:
        now = datetime.now()
        output = now.strftime("%d/%m/%Y %H:%M:%S") + ' --- ' + str(e) + '\n'
        print(output)
        file.write(output)

with open('../data/credentials.txt', 'r') as file:
    bot_key = file.readline()
    affiliate_tag = file.readline()

try:
    product_urls = amazon.get_product_urls('../data/products.txt')
    updated_status = amazon.get_updated_status(product_urls)
    while True:
        start = timeit.default_timer()
        original_status = amazon.get_original_status('../data/status.txt')
        updated_status = amazon.get_updated_status(product_urls)
        
        for x in range(0, len(updated_status)):
            if updated_status[x] == 'available' and original_status[x] != 'available':
                todiscord.notify(product_urls[x], bot_key, affiliate_tag)
        
        stop = timeit.default_timer()
        log('Success. Runtime: ' + str(stop-start)) 
        time.sleep(2)

except Exception as e:
    email_success = err_report(e)
    if email_success != 0:
        log(email_success)
    log(e)
