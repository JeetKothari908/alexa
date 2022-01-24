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
from ytmusic import youtubemusic

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
driver = 0
def closer():
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
def closeradd():
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
def alexathing(thisissogoddamnfrustrating):
    global thething
    thisissogoddamnfrustrating = int(thisissogoddamnfrustrating)
    while thething < thisissogoddamnfrustrating:
        text = command().lower()  ## takes user command
        # text = input('testing version, what do you want to do?')

        text = text.replace('alexa', "")
        if 'what time is it' in text:
            thething = thething + 1
            time = datetime.datetime.now().strftime('%I %M %p')
            good = "it is", time
            speak(good)

        elif 'who is' in text:
            thething = thething + 1
            text = text.replace('who is', "")
            speak(wikipedia.summary(text, 2))

        elif 'Google' in text:
            thething = thething + 1
            # replacing the text without google in it
            text = text.replace('Google', "")
            # searching up the thing in a new tab
            chrome_options = Options()
            chrome_options.add_experimental_option("detach", True)
            driver = webdriver.Chrome(chrome_options=chrome_options,
                                      executable_path=r'C:\Users\jeetd\downloads\chromedriver')
            wait = WebDriverWait(driver, 25)

            driver.get("https://www.google.com/search?q=" + text + "&start=")
        elif 'google' in text:
            thething = thething + 1
            # replacing the text without google in it
            text = text.replace('google', "")
            # searching up the thing in a new tab
            chrome_options = Options()
            chrome_options.add_experimental_option("detach", True)
            driver = webdriver.Chrome(chrome_options=chrome_options,
                                      executable_path=r'C:\Users\jeetd\downloads\chromedriver')
            wait = WebDriverWait(driver, 25)

            driver.get("https://www.google.com/search?q=" + text + "&start=")
        elif 'watch' in text:
            thething = thething + 1
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

        elif 'listen to' in text:
            thething = thething + 1
            text = text.replace('listen to', "")
            youtubemusic()
        elif "bye" in text:
            thething = thething + 1
            speak("Have a nice day ! ")
            driver.quit()
            exit()
        # elif 'joke' in text: DO NOT USE PYJOKES- IT IS HORRIBLE
        # elif text == "what is the weather":
        # potentially make an alarm system using datetime and the text to speech thing
        # testing git commits
        else:
            print('I cannot hear you')
