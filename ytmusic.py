import speech_recognition as sr
import pyttsx3
import datetime
import pyautogui as pag
import mouse
import wikipedia
import webbrowser
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import speech_recognition as sr
import time


text = input('testing version ')
text = text.replace('listen to',"")
if 'song' in text:
    text = text.replace('song', "")
    text = text.replace(' ', "+")
    youtub2 = 'https://music.youtube.com/search?q='
    youtub2 = youtub2 + text
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(chrome_options = chrome_options, executable_path=r'C:\Users\jeetd\downloads\chromedriver')
    wait = WebDriverWait(driver, 25)
    driver.get(youtub2)
    wait.until(expected_conditions.element_to_be_clickable((By.XPATH,'//*[@id="contents"]/ytmusic-responsive-list-item-renderer/div[2]/div[1]/yt-formatted-string/a'))).click()
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH,'//*[@id="left-controls"]/span')))
    nottime = driver.find_element_by_xpath('//*[@id="left-controls"]/span')
    thing = nottime.text
    print(thing)
    thing = thing.replace('0:00 / ', "")
    thing = thing.replace(':', ".")
    thing = float(thing)
    thing = thing * 100
    if thing >= 100:
        thing = thing - 40
    print(thing)
    round(thing)
    thing = int(thing)
    time.sleep(thing)
elif 'playlist' in text:
    text = text.replace('playlist', "")
    text = text.replace(' ', "+")
    youtub2 = 'https://music.youtube.com/search?q='
    youtub2 = youtub2 + text
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(chrome_options = chrome_options, executable_path=r'C:\Users\jeetd\downloads\chromedriver')
    wait = WebDriverWait(driver, 25)
    driver.get(youtub2)
    wait.until(expected_conditions.element_to_be_clickable((By.XPATH,'//*[@id="contents"]/ytmusic-responsive-list-item-renderer/a'))).click()
    time.sleep(2)
    wait.until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="play-button"]/div/yt-icon'))).click()
elif 'artist' in text:
    text = text.replace('artist', "")
    text = text.replace(' ', "+")
    youtub2 = 'https://music.youtube.com/search?q='
    youtub2 = youtub2 + text
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(chrome_options = chrome_options, executable_path=r'C:\Users\jeetd\downloads\chromedriver')
    wait = WebDriverWait(driver, 25)
    driver.get(youtub2)
    wait.until(expected_conditions.element_to_be_clickable((By.XPATH,'//*[@id="contents"]/ytmusic-responsive-list-item-renderer/a'))).click()
    time.sleep(2)
    wait.until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="play-button"]/div/yt-icon'))).click()
