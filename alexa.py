import speech_recognition as sr
import pyttsx3
import datetime
import pyautogui
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
    pyautogui.moveTo(192, 1064, duration = .15)
    mouse.click('left')
    #opens groove
    pyautogui.moveTo(658, 380, duration = .25)
    mouse.click('left')
    #hits kpop
    pyautogui.moveTo(54, 504, duration = 2.5)
    mouse.click('left')
    #hits play all
    pyautogui.moveTo(801, 308, duration = 1)
    mouse.click('left')
elif "play Korean pop" in text:
        #opens menu
        pyautogui.moveTo(192, 1064, duration = .01)
        mouse.click('left')
        #opens groove
        pyautogui.moveTo(658, 380, duration = .25)
        mouse.click('left')
        #hits kpop
        pyautogui.moveTo(54, 504, duration = 2.5)
        mouse.click('left')
        #hits play all
        pyautogui.moveTo(801, 308, duration = 1)
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

elif 'Youtube' in text:
    #replacing text with text without youtube
    text = text.replace('Youtube',"")
    #going to Youtube
    webbrowser.open_new_tab("https://www.youtube.com/")
    #clicking on search bar
    #typing text into search bar
    #clicking searching
    #clicking first option
#elif 'joke' in text: DO NOT USE PYJOKES- IT IS HORRIBLE
#elif text == "what is the weather":
# potentially make an alarm system using datetime and the text to speech thing
#testing git commits
else:
    speak('I cannot hear you')
