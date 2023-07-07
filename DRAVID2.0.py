import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import pywhatkit
from playsound import playsound
import os
import pyjokes
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices', voices[1].id)
print("listen")
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning dear !")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon dear !")
    else:
        speak("Good Evening dear !")
    assname = ("DRAVID 2.0")
    speak("I am your Assistant")
    speak(assname)
    speak("how can i help you")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Unable to Recognize your voice.")
        return "None"
    return query
wishMe()
while True:
    query = takeCommand().lower()
    if 'wikipedia' in query:
        speak('Searching wikipedia.......')
        print("searching wikipedia.......")
        query=query.replace("wikipedia", "")
        result=wikipedia.summary(query,sentences=3)
        print(result)
        speak(result)
    elif 'open youtube' in query:
        speak("opening youtube")
        print("opening youtube")
        webbrowser.open("youtube.com")
    elif'open google' in query:
        speak("opening google")
        print("opening google")
        webbrowser.open("google.com")
    elif'open facebook' in query:
        speak("opening facebook")
        print("opening facebook")
        webbrowser.open("facebook.com")
    elif'how are you alexa' in query:
        speak("nice and fine enough ....u say how r u")
        print("nice and fine enough  ....u say how r u")
    elif'are you in a relationship' in query:
        speak("yess i am in a relation with wifi dear")
        print("yess i am in a relation with wifi dear")
    elif'find me a boyfriend' in query:
        speak("no focus on ur studies....pyaar mohobbat dhoka hai padhle abhi bhi mauka hai")
        print("no focus on ur studies....pyaar mohobbat dhoka hai padhle abhi bhi mauka hai")
    elif'are you busy alexa' in query:
        speak("who the hell is alexa...go to alexa.....byee")
        print("who the hell is alexa...go to alexa.....byee")
    elif'play music' in query:
        speak("okay playing music")
        print("okay playing music")
        music=playsound("E:\\Download\\kaun.mp3")
        print(music)
    elif'the time' in query:
        nowtime=datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"the time is {nowtime}")
        print(f"the time is {nowtime}")
    elif'play on youtube' in query:
        song=query.replace('play on youtube', '')
        speak('playing'+song)
        print(song)
        pywhatkit.playonyt(song)
    elif'open notepad' in query:
        opn=r"C:\windows\system32\notepad.exe"
        os.startfile(opn)
    elif'open paint' in query:
        opp=r"C:\windows\system32\mspaint.exe"
        os.startfile(opp)
    elif'open chrome' in query:
        opc=r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        os.startfile(opc)
    elif'joke' in query:
        speak(pyjokes.get_joke())
        print(pyjokes.get_joke())
    elif'exit' in query:
        speak("thanks for giving me time")
        print("thanks for giving me time")
        exit()
    elif "what's your name" in query or "what is your name" in query:
            speak("My friends call me ")
            speak(assname)
            print("My friends call me ", assname)
    elif "change name" in query:
        speak("What would you like to call me")
        assname = takeCommand()
        speak("Thanks for naming me")
        speak("so my name is")
        speak(assname)

