
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

year = []
driver = webdriver.Chrome(executable_path=r'C:\Users\vion1\Downloads\chromedriver_win32\\chromedriver.exe')
driver.get('https://airtable.com/shrRXLXmGwGPdOaLF/tblWjJI9H9EXyLPPF?backgroundColor=pink&layout=card&viewControls=on')


soup = BeautifulSoup(driver.page_source, "lxml")

while True:
    for link in soup.find_all(class_ = "flex-auto p1"): #Ou draggableRecord rowCardContainer animate
        year = link.text


#element = driver.find_element_by_class_name("draggableRecord rowCardContainer animate")
#driver.execute_script("arguments[0].scrollIntoView(true);", element)
driver.close()


