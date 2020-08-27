import requests
from bs4 import BeautifulSoup
import pandas as pd

webpage_response = requests.get("https://airtable.com/shrRXLXmGwGPdOaLF/tblWjJI9H9EXyLPPF?backgroundColor=pink&layout=card&viewControls=on")

webpage = webpage_response.content
soup = BeautifulSoup(webpage, "html.parser")
print(soup)
new_soup = str(soup)
with open("new_doc_test", "w") as test:
    test.write(new_soup)


email = soup.find_all("@")
email_list = []


#print(email)
for i in email:
    email_list.append(i)

#print(email_list)






















