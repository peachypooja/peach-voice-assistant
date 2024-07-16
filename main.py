import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import webbrowser
import pyjokes
import pyautogui
import os
import time
import subprocess
import wolframalpha
import json
import requests
import cv2
from database import find
from pygame import mixer


print('Loading your AI personal assistant - Peach')

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0')


def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")

def screenshot(index : int = 0):  
    img = pyautogui.screenshot()
    img.save("screenshots\\img.png")      

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source,timeout=5)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception:
            speak("Pardon me, please say that again")
            return "None"
        return statement

def open_camera():
    os.system("start microsoft.windows.camera:")

speak("Loading your AI personal assistant Peach")
wishMe()


if __name__=='__main__':

    while True:
        speak("Tell me how can I help you?")
        mixer.init()
        mixer.music.load('C:\\Users\\Mtronics Computers\\Desktop\\peach\\imp\\init.mp3')
        mixer.music.play()
        

        statement = takeCommand().lower()
        if statement==0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('Okay, Take Care!')
            print('Okay, Take Care!')
            break

        if 'intuitive' in statement:
            speak("Opening an intuitive eye Python application")
            os.system('cd "C:/Users/Mtronics Computers/Desktop/eyes" && python IntutiveEyeX2.py')

        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'play' in statement:
            song = statement.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)
            time.sleep(5)

        elif 'search' in statement:
            result = statement.replace('search', '')
            speak('Searching' + result)
            pywhatkit.search(result)
            speak('results are displayed on your computer screen')
            time.sleep(5)  

        elif 'can i tell you my name' in statement or 'i want to tell you my name' in statement :
            speak("Please Tell me your name")
            rememberMessage = takeCommand()
            speak("you told me that your name is"+rememberMessage)
            remember = open('username.txt', 'w')
            remember.write(rememberMessage)
            remember.close()

        elif 'what is my name' in statement or 'who am I' in statement:
            remember = open('username.txt', 'r')
            speak("Your name is" + remember.read())    

        elif 'what is' in statement:
            answer = statement
            speak('searching about' + answer)
            pywhatkit.info(answer)  
            speak("Here is the result!")
            time.sleep(15)  
            
        elif 'take a screenshot' in statement or 'screenshot' in statement:
            speak("Taking a screenshot")
            screenshot()
            speak("Successfully took a screenshot, You can find it in the screenshots folder")

        elif 'database' in statement:
            speak('What you want to search in database?')
            find(takeCommand())

        elif 'who is' in statement:
             person = statement.replace('who is', '')
             info = wikipedia.summary(person, 3)
             speak("According to Wikipedia Summary")
             print(info)
             speak(info)

        elif 'tell me a story' in statement:
            speak("Krrish will now tell you a story")
            exec(open("storydbase.py").read())

        elif 'tell me a hindi story' in statement or 'tell me a story in hindi' in statement:
            speak("Okay, Playing a Hindi story on Youtube")
            exec(open("hindistories.py").read())
            
        elif 'joke' in statement:
            joke = pyjokes.get_joke()
            speak('Here is a joke')
            print(joke) 
            speak(joke) 
            
        elif 'open camera' in statement or 'camera' in statement:
            speak("Opening the camera")
            open_camera()
            time.sleep(5)
            

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("https://www.gmail.com")
            speak("Google Mail open now")
            time.sleep(5)
        
        elif "weather" in statement:
            api_key = "a931d9520c1553d49420085fc577e148"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("What's the city name?")
            city_name = takeCommand()
            complete_url = base_url + "q=" + city_name + "&appid=" + api_key
            response = requests.get(complete_url)
            data = response.json()
            if data["cod"] != "404":
                main_info = data["main"]
                current_temperature = main_info["temp"]
                current_humidity = main_info["humidity"]
                weather_info = data["weather"][0]
                weather_description = weather_info["description"]
                speak("The temperature in Kelvin unit is " +
                    str(current_temperature) +
                    "\nThe humidity in percentage is " +
                    str(current_humidity) +
                    "\nThe weather description is " +
                    str(weather_description))
                print("Temperature in Kelvin unit = " +
                    str(current_temperature) +
                    "\nHumidity (in percentage) = " +
                    str(current_humidity) +
                    "\nWeather description = " +
                    str(weather_description))
            else:
                speak("City Not Found")

                

        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am Peach, a personal assistant designed by Pooja Yadav. I am programmed to minor tasks like'
                  'doing some calculations, opening youtube ,google chrome ,gmail and stackoverflow, social medias, predict time, search'
                  ' on wikipedia, predict weather in different cities , get top headline news from times of india, tell jokes and you can'
                  ' ask me some questions too!')


        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Pooja Shardaprasad Yadav and she named me Peach from the word Peachy, which describes her cheerful and bubbly personality")
            print("I was built by Pooja Shardaprasad Yadav and she named me Peach from the word Peachy, which describes her cheerful and bubbly personality")

        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")

        elif "open facebook" in statement:
            webbrowser.open_new_tab("https://facebook.com")
            speak("Here is facebook")
        
        elif "open instagram" in statement:
            webbrowser.open_new_tab("https://instagram.com")
            speak("Here is Instagram")

        elif "open github" in statement:
            webbrowser.open_new_tab("https://github.com")
            speak("Here is GitHub")

        elif "open twitter" in statement:
            webbrowser.open_new_tab("https://twitter.com")
            speak("Here is Twitter")

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        elif 'take a note for me' in statement or 'make a reminder' in statement:
            speak("Please Proceed")
            rememberMessage = takeCommand()
            speak("you said me to remember"+rememberMessage)
            remember = open('notes.txt', 'w')
            remember.write(rememberMessage)
            remember.close()

        elif 'speak my notes' in statement or 'remind me' in statement:
            remember = open('notes.txt', 'r')
            speak("you said me to remember that" + remember.read())
        
        elif 'date' in statement:
             speak('sorry, I have a boyfriend')
             print('sorry, I have a boyfriend')

        elif 'are you single' in statement:
             speak('I am in a relationship with Krishna ji')
             print('I am in a relationship with Krishna ji')

        elif 'ask' in statement or 'question' in statement:
            speak('Sure, Please ask!')
            question=takeCommand()
            app_id="5WQAW9-RPQP5WW66Q"
            client = wolframalpha.Client('5WQAW9-RPQP5WW66Q')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif "calculate" in statement.lower(): 
              
            app_id = "5WQAW9-RPQP5WW66Q" 
            client = wolframalpha.Client('5WQAW9-RPQP5WW66Q') 
  
            indx = statement.split().index('calculate') 
            query = statement.split()[indx + 1:] 
            res = client.query(' '.join(query)) 
            answer = next(res.results).text 
            speak("The answer is " + answer) 
            print("The answer is " + answer)
            
        elif 'Thank you' in statement:
             speak('You are welcome! I am glad to help you')
             print('You are welcome! I am glad to help you')

        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])
            
        elif 'bye' in statement or 'exit' in statement or 'quit' in statement:
            speak('Goodbye!, Take care')
            break


time.sleep(3)