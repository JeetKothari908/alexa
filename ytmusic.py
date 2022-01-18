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

nottime = 0
def closer():
    thing = 0
    thing = nottime.text
    print(thing)
    thing = thing.replace('0:00 / ', "")
    thing = thing.replace(':', ".")
    thing = thing.replace(' ', "")
    print('05',thing,'05')
    thing = float(thing)
    thing = thing * 100
    thing2 = thing
    while thing >= 100:
        thing2 = thing2 - 40
        thing = thing - 100
    time.sleep(thing2)
def closeradd():
    thing = 0
    thing = nottime.text
    print(thing)
    thing = thing.replace('0:00 / ', "")
    thing = thing.replace(':', ".")
    thing = thing.replace(' ', "")
    print('05',thing,'05')
    thing = float(thing)
    thing = thing * 100
    thing2 = thing
    while thing >= 100:
        thing2 = thing2 - 40
        thing = thing - 100
    if thing2 > 30:
        time.sleep(6)
        skipad = driver.find_element_by_xpath('//*[@id="ad-text:6"]').click()
    else:
        time.sleep(thing2)

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
    wait.until(expected_conditions.element_to_be_clickable((By.XPATH,'//*[@id="contents"]/ytmusic-responsive-list-item-renderer[2]/div[2]/div[1]/yt-formatted-string/a'))).click()
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH,'//*[@id="left-controls"]/span')))
    time.sleep(4)
    nottime = driver.find_element_by_xpath('//*[@id="player-overlay:0"]/div[2]/span[2]/div[1]')
    closeradd()
    time.sleep(1)
    nottime = driver.find_element_by_xpath('//*[@id="left-controls"]/span')
    closer()
    driver.close()
elif 'playlist' in text:
    text = text.replace('playlist', "")
    text = text.replace(' ', "+")
    f = '0'
    for character in text:

        if character.isdigit():

            contains_digit = True
            f = f + character
    f = f.replace('0', "", 1)
    print(contains_digit)
    print(f)
    text = text.replace(f, "")
    f = int(f)
    text = text +' playlist'
    youtub2 = 'https://music.youtube.com/search?q='
    youtub2 = youtub2 + text
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(chrome_options = chrome_options, executable_path=r'C:\Users\jeetd\downloads\chromedriver')
    wait = WebDriverWait(driver, 25)
    driver.get(youtub2)
    wait.until(expected_conditions.element_to_be_clickable((By.XPATH,'//*[@id="contents"]/ytmusic-responsive-list-item-renderer[2]/div[2]/div[1]/yt-formatted-string/a'))).click()
    wait.until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="play-button"]/div/yt-icon'))).click()
    time.sleep(4)
    nottime = driver.find_element_by_xpath('//*[@id="player-overlay:0"]/div[2]/span[2]/div[1]')
    closeradd()
    print(f)
    f = f * 60
    f = f + 1
    time.sleep(f)

    driver.close()
elif 'artist' in text:
    text = text.replace('artist', "")
    text = text.replace(' ', "+")
    f = '0'
    for character in text:

        if character.isdigit():

            contains_digit = True
            f = f + character
    f = f.replace('0', "", 1)
    print(contains_digit)
    print(f)
    text = text.replace(f, "")
    f = int(f)
    text = text +' artist'
    youtub2 = 'https://music.youtube.com/search?q='
    youtub2 = youtub2 + text
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(chrome_options = chrome_options, executable_path=r'C:\Users\jeetd\downloads\chromedriver')
    wait = WebDriverWait(driver, 25)
    driver.get(youtub2)
    wait.until(expected_conditions.element_to_be_clickable((By.XPATH,'//*[@id="contents"]/ytmusic-responsive-list-item-renderer[2]/div[2]/div[1]/yt-formatted-string/a'))).click()
    wait.until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="play-button"]/div/yt-icon'))).click()
    time.sleep(4)
    nottime = driver.find_element_by_xpath('//*[@id="player-overlay:0"]/div[2]/span[2]/div[1]')
    closeradd()
    print(f)
    f = f * 60
        f = f + 1
    time.sleep(f)

    driver.close()
