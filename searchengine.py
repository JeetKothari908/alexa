import webbrowser
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import speech_recognition as sr
import time
import pandas as pd

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
youtube = input("do you want to search things on youtube? ")
if youtube == 'yes':
    searching = input("what do you want to search? ")
    #dont touch this code idk what it does but it does something important
    driver = webdriver.Chrome(chrome_options = chrome_options, executable_path=r'C:\Users\jeetd\downloads\chromedriver')
    wait = WebDriverWait(driver, 25)
    #opens youtube and waits for it to load
    driver.get('https://www.youtube.com/')
    #finds the search bar using its html dom thing idk just click on the element and inspect it
    search_bar = driver.find_element_by_name("search_query")
    #puts stuff in search bar
    search_bar.send_keys(searching)
    time.sleep(1)
    search_bar.send_keys(Keys.RETURN)
    time.sleep(.35)
    wait.until(expected_conditions.presence_of_element_located((By.ID,"img" )))
    title1 = driver.find_element_by_class_name("style-scope ytd-channel-name")
    ytstuff = []
    ytstuff.append(title1)
    ytstuff_pd = pd.DataFrame(ytstuff)
    ytstuff_pd.columns('images')
    ytstuff_pd.to_csv('ytstuff.csv', index = false)
    if searching in title1:
        title1.click()
    #wait.until(expected_conditions.visibility_of_element_located((By.ID,"img" )))
    #wait.until(expected_conditions.element_to_be_clickable((By.ID,"video-title"))).click()




    # clicking on the match search having same as in searched query
    #wait.until(
    #    expected_conditions.element_to_be_clickable((By.ID, "img"))).click()

    #print current url
    #print(driver.current_url)
    #closes browser
    #driver.close()


#text = input('what do you want to search?  ')
#googling the input text
#webbrowser.open_new_tab("https://www.google.com/search?q=" + text + "&start=")
