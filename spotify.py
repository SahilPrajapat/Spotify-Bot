from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

email="email"
password="password"

driver=webdriver.Chrome()
driver.get("https://open.spotify.com/")

loginButton = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/header/div[5]/button[2]')
loginButton.click()
time.sleep(5)

emailContainer = driver.find_element_by_name('username')
emailContainer.send_keys(email)

passContainer = driver.find_element_by_id('login-password')
passContainer.send_keys(password)

passContainer.send_keys(Keys.RETURN)

time.sleep(10)

closeCookie = driver.find_element_by_xpath('//*[@id="onetrust-close-btn-container"]/button').click()

searchButton = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/nav/div[1]/ul/li[2]/a').click()
time.sleep(2)

# search = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/header/div[3]/div/div/input')
# search.send_keys("chaska")
# search.send_keys(Keys.RETURN)
# time.sleep(5)

# action = ActionChains(driver)
# song1 = driver.find_element_by_xpath('//*[@id="searchPage"]/div/div/section[2]/div[2]/div/div/div/div[2]/div[2]/div')
# action.move_to_element(song1).perform()
# time.sleep(1)
# play = driver.find_element_by_xpath('//*[@id="searchPage"]/div/div/section[2]/div[2]/div/div/div/div[2]/div[2]/div/div[1]/div[1]/button')
# play.click()
# time.sleep(10)
# # ----------------------------------------------------------------------------------------------------------------------------------------------------------
# search = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/header/div[3]/div/div/input')
# search.clear()
# search.send_keys("lut gaye")
# search.send_keys(Keys.RETURN)
# time.sleep(5)

# song2 = driver.find_element_by_xpath('//*[@id="searchPage"]/div/div/section[2]/div[2]/div/div/div/div[2]/div[1]/div')
# action.move_to_element(song2).perform()
# time.sleep(1)
# play = driver.find_element_by_xpath('//*[@id="searchPage"]/div/div/section[2]/div[2]/div/div/div/div[2]/div[1]/div/div[1]/div[1]/button')
# play.click()
# time.sleep(30)

def searchAndPlay(s, hoverX, playX):
    search = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/header/div[3]/div/div/input')
    search.clear()
    search.send_keys(s)
    search.send_keys(Keys.RETURN)
    time.sleep(5)

    action = ActionChains(driver)
    song = driver.find_element_by_xpath(hoverX)
    action.move_to_element(song).perform()
    time.sleep(1)
    play = driver.find_element_by_xpath(playX)
    play.click()
    time.sleep(10)

sName = "chaska"
hx = '//*[@id="searchPage"]/div/div/section[2]/div[2]/div/div/div/div[2]/div[2]/div'
px = '//*[@id="searchPage"]/div/div/section[2]/div[2]/div/div/div/div[2]/div[2]/div/div[1]/div[1]/button'
searchAndPlay(sName, hx, px)

sName = "beautiful mistake"
hx = '//*[@id="searchPage"]/div/div/section[2]/div[2]/div/div/div/div[2]/div[1]/div'
px = '//*[@id="searchPage"]/div/div/section[2]/div[2]/div/div/div/div[2]/div[1]/div/div[1]/div[1]/button'
searchAndPlay(sName, hx, px)
