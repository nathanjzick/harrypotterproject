from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import os

### implicit waits are a better way to do sleeps
### https://selenium-python.readthedocs.io/waits.html

driver = webdriver.Chrome('C:\\Users\\Nathan\\chromedriver\\chromedriver.exe')
driver.get('https://www.bookscool.com/en/harrypotter.php')

book_dict = {1:'\'Harry Potter and the Philosophers Stone\'', 2:'\'Harry Potter and the Chamber of Secrets\'', 3:'\'Harry Potter and the Prisoner of Azkaban\'', 4:'\'Harry Potter and the Goblet of Fire\'', 5:'\'Harry Potter and the Order of the Phoenix\'', 6:'\'Harry Potter and the Half-Blood Prince\'', 7:'\'Harry Potter and the Deathly Hallows\''}
text_dict = {}

for n, b in book_dict.items():
  driver.find_element_by_xpath(f'//img[@alt={b}]').click()
  e = ''
  c = 1
  while e == '':
    if n not in text_dict:
      text_dict[n] = {}
    text_dict[n][c] = driver.find_element_by_xpath('//div[@id="content-text"]').text.replace('\n','')
    c += 1
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    try:
      driver.find_element_by_xpath('//a[@class="btn btn-outline-success float-right"]').click()
    except:
      e = 'End of book.'
  driver.get('https://www.bookscool.com/en/harrypotter.php')

# export dictionary to csv's per book
os.chdir('C:\\Users\\Nathan\\Documents\\LING 360\\Final Project')
error_log = open('errors.log', 'w')
for n in book_dict:
  for c in text_dict:
    with open(f'Harry_Potter_{n}_Chapter{c}.txt', 'w', encoding='utf8') as f:
      try:
        f.write(text_dict[n][c])
      except Exception as e:
        error_log.write(f'There was an error: {str(e)}')
      finally:
        pass

driver.close()
driver.quit()