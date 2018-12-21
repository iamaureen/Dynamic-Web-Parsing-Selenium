from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time


driverPath = '/Users/ishratahmed/Documents/Supplementary Resources/PySeleniumDemo/chromedriver'
url = 'https://www.khanacademy.org/math/pre-algebra/pre-algebra-ratios-rates/pre-algebra-rates/v/finding-unit-rates'
usernameSelector = '.text_12zg6rl-o_O-LabelLarge_np83x5-o_O-authorNickname_1njac9q' #selector class for the user
loadMoreBtnSelector = '.button_1eqj1ga-o_O-shared_acgh35-o_O-default_9fm203' #selector class for 'show more' button
ulPostSelector = 'listWrapper_17u7rry'
liPostSelector = 'post_b12blo'
delay = 10  # seconds

browser = webdriver.Chrome(driverPath)
browser.get(url)

#print(browser.current_url) #prints the url
#print(browser.page_source) #prints the page source

#reference:
# https://stackoverflow.com/questions/39112138/use-selenium-to-click-a-load-more-button-until-it-doesnt-exist-youtube
# https://stackoverflow.com/questions/49939123/scrape-dynamic-contents-created-by-javascript-using-python
# https://stackoverflow.com/questions/11908249/debugging-element-is-not-clickable-at-point-error
try:

    for _ in range(1):  # Adjust this range according to the number of how far we wanna go down (i.e., number of times show more is clicked).
        WebDriverWait(browser, delay).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, loadMoreBtnSelector))).click()
        time.sleep(2)
        print("MORE button clicked")
        time.sleep(5) #attempts to click the button too early upon page refresh, as a result raises exception. so added timer.


    WebDriverWait(browser, delay).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, usernameSelector))
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
    # for span in soup.select(usernameSelector): # this shows all the users in the page, but does not load users from 'show more'
    #                                            # also only selects the one those are visible in the webpage;
    #                                            # does not select the hidden ones with the same selector
    #     print(span.text)
    #
    # get the div that has all the posts
    # print(soup.select('div.default_olfzxm-o_O-container_k9kem1'))

    #get the total number of posts displayed in the DOM
    ultag = soup.find_all('ul', {'class': ulPostSelector})

    postsVisibleInDOM = ultag[0].find_all('li', recursive=False) #recursive = False; only gets the immediate children - this indicates total number of posts displayed in the DOM
    print('total number of posts visible in the DOM', len(postsVisibleInDOM))
    #print(list(enumerate(ultag[0].find_all('li'))))

    for litag in postsVisibleInDOM:
        # print(litag) #prints the entire <li><div><div>post</div><div>answer</div></div></li>

        # print(litag.findChildren()[0].find_all('span',{'class':'text_12zg6rl-o_O-LabelLarge_np83x5'})) #finds all the span tags for reply/comment

        # find returns the first occurence of the given selector - post author
        print(litag.find('span', {'class': 'text_12zg6rl-o_O-LabelLarge_np83x5-o_O-authorNickname_1njac9q'}).text)
        # find returns the first occurence of the given selector - post content
        print(litag.find('span',{'class':'text_12zg6rl-o_O-Body_1rk1c4b-o_O-content_q7x1i'}).text)






