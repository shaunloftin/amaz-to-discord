from selenium import webdriver
from selenium.webdriver.chrome.options import Options

CHROMEDRIVER_PATH = "/usr/bin/chromedriver"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-setuid-sandbox")
chrome_options.add_argument("--disable-features=VizDisplayCompositor")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(CHROMEDRIVER_PATH,options=chrome_options)
driver.get("https://www.google.com")
print(driver.title)
driver.close()
