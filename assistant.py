import webbrowser
import pyttsx3
import speech_recognition as sr
import datetime
import random
import os
import pyautogui
import wikipedia

wake = 'assistant'

engine = pyttsx3.init('sapi5')
engine.setProperty('volume',1.0)
engine.setProperty('rate',150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

r = sr.Recognizer()

def speak(text):
        engine.say(text)
        engine.runAndWait()
    
def microInput():
        with sr.Microphone() as source:
            print('listening..')
            audio = r.listen(source)
            query = ''
            try:
                query = r.recognize_google(audio)
                print(query)
            except sr.UnknownValueError:
                speak('I did not get that..')
            except sr.RequestError:
                speak('network issues..')
                return "None"
            return query

def wishMe():
    hour = int(datetime.datetime.now().hour)
    date = datetime.date.today()
    time = datetime.datetime.now().strftime("%H:%M:%S")
    wrds = ["how may i help you?", "tell me something to do..", "assign me a job..", "what else can i do for you?"]
    wrd_rndm = random.choice(wrds)
    if hour >=4 and hour<12:
        speak("Good morning,sir")
    elif hour >=12 and hour<6:
        speak("Good afternoon,sir")
    elif hour >=6 and hour<24:
        speak("Good evening,sir")
    else:
        speak("It is time to sleep, please take some rest..")
    speak("jarvis at your service..")
    speak(f"The time is {time}")
    speak(f"The date is {date}")
    speak(wrd_rndm)

def cointoss():
    coin = ['head', 'tail']
    coin_toss = random.choice(coin)
    speak("tossing the coin for you..")
    speak(f"it is {coin_toss}")

def rollDice():
    a = [1, 2, 3, 4, 5, 6]
    aRand = random.choice(a)
    speak('Rolling the dice..')
    speak(f"You got a {aRand}")

def takeCommand():
    while(True):
        command = microInput().lower()
        if wake in command:
            wishMe()
            while(True):
                command = microInput().lower()
                if 'wikipedia' in command:
                    command = command.replace("wikipedia", "")
                    result = wikipedia.summary(command, sentences = 3)
                    speak('According to wikipedia...')
                    print(result)
                    speak(result)
                
                elif 'youtube' in command:
                    speak('opening youtube')
                    webbrowser.open('youtube.com')
                elif 'google' in command:
                    webbrowser.open('google.com')
                elif 'instagram' in command:
                    webbrowser.open('instagram.com')
                elif 'twitter' in command:
                    webbrowser.open('twitter.com')
                elif 'facebook' in command:
                    webbrowser.open('facebook.com')
                elif 'whatssapp' in command:
                    webbrowser.open('whatssapp.web')
                elif 'gmail' in command:
                    webbrowser.open('gmail.com')
                elif 'amazon' in command:
                    webbrowser.open('amazon.in')
                elif 'search' in command:
                    url = "https://www.google.com/search?q=" + command
                    speak('Here is what i found..')
                    webbrowser.open(url)               
                elif 'toss a coin' in command:
                    cointoss()
                elif 'play game' in command:
                    os.system('rps_game.py')
                elif 'generate password' in command:
                    os.system('pass_gen.py')
                elif 'open code' in command:
                    os.startfile("C:\\Users\\deepa\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")       
                elif 'take screenshot' in command:
                    myScrnsht = pyautogui.screenshot()
                    myScrnsht.save("scrnsht.jpg")
                elif 'quit' in command:
                    speak('Goodbye')
                    quit()
                elif 'roll a dice' in command:
                    rollDice()
                elif 'number guess' in command:
                    os.system('num_guess.py')
        else:
            pass
            
takeCommand()        




    
        





