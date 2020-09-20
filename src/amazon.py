# AMAZ-TO-DISCORD MONITORING
# WRITTEN BY: SHAUN LOFTIN
# github.com/shaunloftin
#
# amazon.py

from selenium import webdriver
from bs4 import BeautifulSoup

def get_product_urls(url_file):
    product_urls = []
    with open(url_file, 'r') as file:
        for line in file:
            product_urls.append(line)
    return product_urls
        
def get_original_status(status_file):
    original_status = []
    with open(status_file, 'r') as file:
        for line in file:
            original_status.append(line)
    return original_status

def get_updated_status(product_urls):
    updated_status = []
    html = webdriver.Chrome(executable_path='../data/chromedriver.exe')
    with open('../data/status.txt', 'w') as file:
        for url in product_urls:
            html.get(url)
            print("bruh")
            soup = BeautifulSoup(html.page_source, 'lxml')
            availability = soup.find('div', attrs={'id' : 'availability'})
            items = availability.findAll('span', attrs={'class' : 'a-declarative', 'class' : 'a-size-medium'})
        
            status = "available"
            for x in items:
                if 'Currently un' in x.text:
                    status = 'unavailable'
                    break
                if 'Available from' in x.text:
                    status = 'other-seller'
                    break
            updated_status.append(status)
            file.write(status)
        
    webdriver.Chrome.quit(html)
    return updated_status