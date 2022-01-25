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
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
driver = 0
def closer(nottime):
    thing = 0
    thing = nottime.text
    print(thing)
    thing = thing.replace('0:00 / ', "")
    thing = thing.replace(':', ".")
    thing = thing.replace(' ', '')
    print(thing)
    thing = float(thing)
    thing = thing * 100
    thing2 = thing
    while thing >= 100:
        thing2 = thing2 - 40
        thing = thing - 100

    round(thing2)
    thing = int(thing2)
    print(thing2)
    thing = thing2
    while thing2>= 1:
        print(thing2)
        time.sleep(1)
        thing2 -= 1
def closeradd(nottime):
    thing = 0
    thing = nottime.text
    print(thing)
    thing = thing.replace('0:00 / ', "")
    thing = thing.replace(':', ".")
    print(thing)
    thing = thing.replace(' ', '')
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
            while thing2>= 1:
                print(thing2)
                time.sleep(1)
                thing2 -= 1
nottime = 0
f = '0'
contains_digit = 0
thething = 0
text = ''
thing = 0
thing2 = 0
def takething():
    global text
    global contains_digit
    global f
    for character in text:
        if character.isdigit():
            contains_digit = True
            f = f + character
    if contains_digit > 0:
        f = f.replace('0', "", 1)
        print(contains_digit)
        print(f)
        text = text.replace(f, "")
        f = int(f)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def command():
    global thething
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
    text = command().lower()
    text = text.replace('alexa', "")
    if 'what time is it' in text:
        nottime = datetime.datetime.now().strftime('%I %M %p')
        good = "it is", nottime
        speak(good)
        thething = thething + 1
    elif 'who is' in text:
        text = text.replace('who is', "")
        speak(wikipedia.summary(text, 2))
        thething = thething + 1
    elif 'Google' in text:
        # replacing the text without google in it
        text = text.replace('Google', "")
        # searching up the thing in a new tab
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(chrome_options=chrome_options,
                                  executable_path=r'C:\Users\jeetd\downloads\chromedriver')
        wait = WebDriverWait(driver, 25)

        driver.get("https://www.google.com/search?q=" + text + "&start=")
        thething = thething + 1
    elif 'google' in text:
        # replacing the text without google in it
        text = text.replace('google', "")
        # searching up the thing in a new tab
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(chrome_options=chrome_options,
                                  executable_path=r'C:\Users\jeetd\downloads\chromedriver')
        wait = WebDriverWait(driver, 25)

        driver.get("https://www.google.com/search?q=" + text + "&start=")
        thething = thething + 1
    elif 'watch' in text:
        text = text.replace("watch", '')
        text = text.replace(" ", '+')
        youtub2 = 'https://www.youtube.com/results?search_query='
        youtub2 = youtub2 + text
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(chrome_options=chrome_options,
                                  executable_path=r'C:\Users\jeetd\downloads\chromedriver')
        wait = WebDriverWait(driver, 25)

        driver.get(youtub2)
        wait.until(expected_conditions.element_to_be_clickable((By.ID, "video-title"))).click()
        thething = thething + 1
    elif 'listen to' in text:
        text = text.replace('listen to', "")
        if 'song' in text:
            text = text.replace('song', "")
            text = text.replace(' ', "+")
            youtub2 = 'https://music.youtube.com/search?q='
            youtub2 = youtub2 + text
            chrome_options = Options()
            chrome_options.add_experimental_option("detach", True)
            driver = webdriver.Chrome(chrome_options=chrome_options,
                                      executable_path=r'C:\Users\jeetd\downloads\chromedriver')
            wait = WebDriverWait(driver, 25)
            driver.get(youtub2)
            wait.until(expected_conditions.element_to_be_clickable((By.XPATH,
                                                                    '//*[@id="contents"]/ytmusic-shelf-renderer[2]/div[2]/ytmusic-responsive-list-item-renderer[1]/div[2]/div[1]/yt-formatted-string/a'))).click()
            wait.until(
                expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="left-controls"]/span')))
            time.sleep(4)
            nottime = driver.find_element(By.XPATH, '//*[@id="player-overlay:0"]/div[2]/span[2]/div[1]')
            closeradd(nottime)
            time.sleep(1)
            nottime = driver.find_element(By.XPATH, '//*[@id="left-controls"]/span')
            closer(nottime)
            driver.close()
            thething = thething + 1
        elif 'playlist' in text:
            text = text.replace('playlist', "")
            text = text.replace(' ', "+")
            takething()
            text = text + ' playlist'
            youtub2 = 'https://music.youtube.com/search?q='
            youtub2 = youtub2 + text
            chrome_options = Options()
            chrome_options.add_experimental_option("detach", True)
            driver = webdriver.Chrome(chrome_options=chrome_options,
                                      executable_path=r'C:\Users\jeetd\downloads\chromedriver')
            wait = WebDriverWait(driver, 25)
            driver.get(youtub2)
            wait.until(expected_conditions.element_to_be_clickable((By.XPATH,
                                                                    '//*[@id="contents"]/ytmusic-shelf-renderer[2]/div[2]/ytmusic-responsive-list-item-renderer[1]/div[2]/div[1]/yt-formatted-string/a'))).click()
            wait.until(expected_conditions.element_to_be_clickable(
                (By.XPATH, '//*[@id="play-button"]/div/yt-icon'))).click()
            time.sleep(4)
            nottime = driver.find_element(By.XPATH, '//*[@id="player-overlay:0"]/div[2]/span[2]/div[1]')
            closeradd(nottime)
            print(f)
            f = f * 60
            f = f + 1
            time.sleep(f)
            thething = thething + 1

        elif 'artist' in text:
            text = text.replace('artist', "")
            text = text.replace(' ', "+")
            takething()
            youtub2 = 'https://music.youtube.com/search?q='
            youtub2 = youtub2 + text
            chrome_options = Options()
            chrome_options.add_experimental_option("detach", True)
            driver = webdriver.Chrome(chrome_options=chrome_options,
                                      executable_path=r'C:\Users\jeetd\downloads\chromedriver')
            wait = WebDriverWait(driver, 25)
            driver.get(youtub2)
            wait.until(expected_conditions.element_to_be_clickable(
                (By.XPATH, '//*[@id="contents"]/ytmusic-responsive-list-item-renderer/a'))).click()
            wait.until(expected_conditions.element_to_be_clickable(
                (By.XPATH, '//*[@id="play-button"]/div/yt-icon'))).click()
            time.sleep(4)
            nottime = driver.find_element(By.XPATH, '//*[@id="player-overlay:0"]/div[2]/span[2]/div[1]')
            closeradd(nottime)
            print(f)
            f = f * 60
            f = f + 1
            time.sleep(f)
            driver.close()
            thething = thething + 1
    elif "bye" in text:
        speak("Have a nice day ! ")
        driver.quit()
        thething = thething + 1
        exit()
    # elif 'joke' in text: DO NOT USE PYJOKES- IT IS HORRIBLE
    # elif text == "what is the weather":
    # potentially make an alarm system using datetime and the text to speech thing
    # testing git commits
    else:
        print('I cannot hear you')
