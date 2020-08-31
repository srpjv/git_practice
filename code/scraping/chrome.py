from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup
import urllib.request

class scraping():
    def __init__(self):
        self.url = "https://airtable.com/shrRXLXmGwGPdOaLF/tblWjJI9H9EXyLPPF?backgroundColor=pink&layout=card&viewControls=on"

    def loading(self):
        self.driver.get(self.url)




variable = scraping()
print(variable)
