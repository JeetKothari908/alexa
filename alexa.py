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


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def command():
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("Alexa: Listening...")
            audio=r.listen(source)
            try:
                text = r.recognize_google(audio)
                print(text)
                return text
                break
            except:
                print("Try Again")
while True:
    text = command().lower() ## takes user command
    #text = input('testing version, what do you want to do?')
    #if 'alexa' in text:
        #text = text.replace('alexa', "")
    if 'what time is it' in text:
        time = datetime.datetime.now().strftime('%I %M %p')
        good = "it is", time
        speak(good)

    elif 'who is' in text:
        text = text.replace('who is',"")
        speak(wikipedia.summary(text,2))

    elif 'Google' in text:
        #replacing the text without google in it
        text = text.replace('Google',"")
        #searching up the thing in a new tab
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(chrome_options = chrome_options, executable_path=r'C:\Users\jeetd\downloads\chromedriver')
        wait = WebDriverWait(driver, 25)

        driver.get("https://www.google.com/search?q=" + text + "&start=")
    elif 'google' in text:
        #replacing the text without google in it
        text = text.replace('google',"")
        #searching up the thing in a new tab
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(chrome_options = chrome_options, executable_path=r'C:\Users\jeetd\downloads\chromedriver')
        wait = WebDriverWait(driver, 25)

        driver.get("https://www.google.com/search?q=" + text + "&start=")
    elif 'watch' in text:
        text = text.replace("watch", '')
        text = text.replace(" ", '+')
        youtub2 = 'https://www.youtube.com/results?search_query='
        youtub2 = youtub2 + text
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(chrome_options = chrome_options, executable_path=r'C:\Users\jeetd\downloads\chromedriver')
        wait = WebDriverWait(driver, 25)

        driver.get(youtub2)
        wait.until(expected_conditions.element_to_be_clickable((By.ID,"video-title" ))).click()

    elif 'listen to' in text:
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(chrome_options = chrome_options, executable_path=r'C:\Users\jeetd\downloads\chromedriver')
        text = text.replace('listen to',"")
        wait = WebDriverWait(driver, 25)
        text = text.replace(" ", '%20')
        youtub2 = 'https://open.spotify.com/search/'
        youtub2 = youtub2.append(text)
        wait.until(expected_conditions.visibility_of_element_located((By.ID,"cidsyncjs" ))).click()

    elif "bye" in text:
        speak("Have a nice day ! ")
        exit()
    #elif 'joke' in text: DO NOT USE PYJOKES- IT IS HORRIBLE
    #elif text == "what is the weather":
    # potentially make an alarm system using datetime and the text to speech thing
    #testing git commits
    else:
        speak('I cannot hear you')

#starting the if statements
