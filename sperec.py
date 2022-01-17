import speech_recognition as sr
import pyttsx3
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
            print('Listening')
            audio=r.listen(source)
            try:
                text = r.recognize_google(audio)
                print(text)
                return text
                break
            except:
                speak("Try Again")
while True:
    text = command().lower() ## takes user command
    if 'end' in text:
        exit()
