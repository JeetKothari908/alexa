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



text = input('what do you want to listen to? ')
#text = text.replace('listen to',"")
text = text.replace(" ", '+')
youtub2 = 'https://music.youtube.com/search?q='
youtub2 = youtub2 + text
#pag.moveTo(913, 545, 0.01)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options = chrome_options, executable_path=r'C:\Users\jeetd\downloads\chromedriver')
driver.get(youtub2)
wait = WebDriverWait(driver, 25)
#a = ActionChains(driver)
#wait.until(expected_conditions.element_to_be_clickable((By.ID,"ripple" )))
time.sleep(1)
#figure out how to use xpath and then use it!
thing = driver.find_element_by_class_name("yt-simple-endpoint style-scope ytmusic-responsive-list-item-renderer")
thing.click()
wait.until(expected_conditions.element_to_be_clickable((By.name,"tp-yt-paper-button" ))).click()
#thing2 = driver.find_element_by_name('tp-yt-paper-button')
#thing2.click()
