import speech_recognition as sr
import pyttsx3
import datetime
import pyautogui as pag
import mouse
import wikipedia
import webbrowser

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
    #replacing text with text without youtube
    text = text.replace('watch',"")
    #going to Youtube
    webbrowser.open_new_tab("https://www.youtube.com/")
    #clicking on search bar
    pag.moveTo(596,170, duration = 2.5)
    mouse.click('left')
    #typing text into search bar
    pag.typewrite(text, interval = 0.05)
    #clicking searching]
    pag.moveTo(1260,170,duration = 0.25)
    mouse.click('left')
    #clicking first option
    pag.moveTo(650,350,duration = 3)
    mouse.click('left')
#elif 'joke' in text: DO NOT USE PYJOKES- IT IS HORRIBLE
#elif text == "what is the weather":
# potentially make an alarm system using datetime and the text to speech thing
#testing git commits
else:
    speak('I cannot hear you')
