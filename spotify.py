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
text = text.replace('listen to',"")
text = text.replace(" ", '%20')
youtub2 = 'https://open.spotify.com/search/'
youtub2 = youtub2 + text
#pag.moveTo(913, 545, 0.01)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options = chrome_options, executable_path=r'C:\Users\jeetd\downloads\chromedriver')
driver.get(youtub2)
wait = WebDriverWait(driver, 25)
a = ActionChains(driver)
wait.until(expected_conditions.visibility_of_element_located((By.className,"spotify-logo--text" )))
play = find_element_by_id('play-button')
a.move_to_element(play).perform()
time.sleep(1)
div.click()
