from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


driverPath = '/Users/ishratahmed/Documents/Supplementary Resources/PySeleniumDemo/chromedriver'
url = 'https://www.khanacademy.org/math/pre-algebra/pre-algebra-ratios-rates/pre-algebra-rates/v/finding-unit-rates'
selector = '.text_12zg6rl-o_O-LabelLarge_np83x5-o_O-authorNickname_1njac9q' #selector class for the user
loadMoreBtnSelector = '.button_1eqj1ga-o_O-shared_acgh35-o_O-default_9fm203' #selector class for 'show more' button
delay = 10  # seconds

browser = webdriver.Chrome(driverPath)
browser.get(url)

#print(browser.current_url) #prints the url
#print(browser.page_source) #prints the page source



#https://stackoverflow.com/questions/49939123/scrape-dynamic-contents-created-by-javascript-using-python
try:

    for _ in range(5):  # Adjust this range according to the number of how far we wanna go down.
        WebDriverWait(browser, delay).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, loadMoreBtnSelector))).click()
        print("MORE button clicked")

    WebDriverWait(browser, delay).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, selector))
    )

except TimeoutException:
    print('Loading took too much time!')
else:
    html = browser.page_source

finally:
    browser.quit()

if html:
    soup = BeautifulSoup(html, 'lxml')
    #raw_data = soup.select_one(selector).text #Find only the first tag that matches a selector - this works
    for span in soup.select(selector): #this shows all the users in the page, but does not load users from 'show more'
        print(span.text)