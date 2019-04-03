from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import os

# sets path to where chrome driver is
driver = webdriver.Chrome('C:\\Users\\Nathan\\chromedriver\\chromedriver.exe')
# gets page with harry potter books
driver.get('https://www.bookscool.com/en/harrypotter.php')
# dictionary of seven books with int key and string value
book_dict = {1:'\'Harry Potter and the Philosophers Stone\'', 2:'\'Harry Potter and the Chamber of Secrets\'', 3:'\'Harry Potter and the Prisoner of Azkaban\'', 4:'\'Harry Potter and the Goblet of Fire\'', 5:'\'Harry Potter and the Order of the Phoenix\'', 6:'\'Harry Potter and the Half-Blood Prince\'', 7:'\'Harry Potter and the Deathly Hallows\''}
# loops through book dictionary with n being the book number and b being the name of the book
for n, b in book_dict.items():
  # clicks on the correct book
  driver.find_element_by_xpath(f'//img[@alt={b}]').click()
  # initialize variables
  e = ''
  c = 1
  # loops until an error is found (error will be missing button and end of book)
  while e == '':
    # puts text found in content-text div & removes all new line characters
    text = driver.find_element_by_xpath('//div[@id="content-text"]').text.replace('\n','')
    # creates a new text file with the corresponding book and chapter
    with open(f'C:\\Users\\Nathan\\Documents\\LING 360\\Final Project\\text\\Book_{n}\\Chapter_{c}.txt', mode='w', encoding='utf8') as f:
      # exception handling to ensure the scraper finishes even with errors
      try:
        f.write(text)
      except Exception as e:
        print(f'\n\nThere was an error: {str(e)}\n\n')
      finally:
        pass
    # increment chapter counter
    c += 1
    # scroll to the bottom of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    try:
      # click next chapter button
      driver.find_element_by_xpath('//a[@class="btn btn-outline-success float-right"]').click()
    except:
      # fill e with error to break out of while loop
      e = 'End of book.'
  # goes back to page with all books to move onto next book
  driver.get('https://www.bookscool.com/en/harrypotter.php')

# close selenium web browser
driver.close()
driver.quit()