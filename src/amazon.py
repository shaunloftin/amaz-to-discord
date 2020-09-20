# AMAZ-TO-DISCORD MONITORING
# WRITTEN BY: SHAUN LOFTIN
# github.com/shaunloftin
#
# amazon.py

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def get_product_urls(url_file):
    product_urls = []
    with open(url_file, 'r') as file:
        for line in file:
            product_urls.append(line.rstrip('\n'))
    return product_urls
        
def get_original_status(status_file):
    original_status = []
    with open(status_file, 'r') as file:
        for line in file:
            original_status.append(line)
    return original_status

def get_updated_status(product_urls):
    updated_status = []
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    html = webdriver.Chrome(executable_path='/usr/bin/chromedriver', chrome_options=chrome_options)
    with open('../data/status.txt', 'w') as file:
        for url in product_urls:
            html.get(url)
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
            file.write(status+'\n')
        
    webdriver.Chrome.quit(html)
    return updated_status
