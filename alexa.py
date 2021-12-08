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
from selenium.webdriver.chrome.options
import Optionsimport speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    # read the audio data from the default microphone
    audio_data = r.record(source, duration=5)
    # record the data from the microphone for 5 seconds
    print("Recognizing...")
    # convert speech to text
    text = r.recognize_google(audio_data)
    print(text)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#setting up selenium
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options = chrome_options, executable_path=r'C:\Users\jeetd\downloads\chromedriver')
#starting the if statements
if 'what time is it' in text:
    time = datetime.datetime.now().strftime('%I %M %p')
    good = "it is", time
    speak(good)

elif "Korean pop" in text:
    #opens menu
    pag.moveTo(192, 1064, duration = .15)
    mouse.click('left')
    #opens groove
    pag.moveTo(658, 380, duration = .25)
    mouse.click('left')
    #hits kpop
    pag.moveTo(54, 504, duration = 2.5)
    mouse.click('left')
    #hits play all
    pag.moveTo(801, 308, duration = 1)
    mouse.click('left')
elif "play Korean pop" in text:
    #opens menu
    pag.moveTo(192, 1064, duration = .15)
    mouse.click('left')
    #opens groove
    pag.moveTo(658, 380, duration = .25)
    mouse.click('left')
    #hits kpop
    pag.moveTo(54, 504, duration = 2.5)
    mouse.click('left')
    #hits play all
    pag.moveTo(801, 308, duration = 1)
    mouse.click('left')
elif 'who is' in text:
    text = text.replace('who is',"")
    speak(wikipedia.summary(text,2))
elif 'is' in text:
    text = text.replace('is',"")
    speak(wikipedia.summary(text,2))

elif 'Google' in text:
    #replacing the text without google in it
    text = text.replace('Google',"")
    #searching up the thing in a new tab
    webbrowser.open_new_tab("https://www.google.com/search?q=" + text + "&start=")

elif 'watch' in text:
    text = text.replace('watch',"")
    #opens youtube and waits for it to load
    driver.get('https://www.youtube.com/')
    #finds the search bar using its html dom thing idk just click on the element and inspect it
    search_bar = driver.find_element_by_name("search_query")
    #puts stuff in search bar
    search_bar.send_keys(text)
    #clicks return
    search_bar.send_keys(Keys.RETURN)
#elif 'joke' in text: DO NOT USE PYJOKES- IT IS HORRIBLE
#elif text == "what is the weather":
# potentially make an alarm system using datetime and the text to speech thing
#testing git commits
else:
    speak('I cannot hear you')
