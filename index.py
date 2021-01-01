import speech_recognition as sr
import pyttsx3
import wikipedia
# import datetime
import webbrowser
# import os
import time
# import subprocess
# from ecapture import ecapture as ec
# import wolframalpha
# import json
# import requests

from speak import speak

import tellTime

# speak("I think it's a good idea and I stand by it.")

def takeCommand():
  
  r = sr.Recognizer() 

  # from the speech_Recognition module  
  # we will use the Microphone module 
  # for listening the command 
  with sr.Microphone() as source: 
    print('Listening') 

    r.pause_threshold = 0.7
    audio = r.listen(source) 

    try: 
      print("Recognizing") 

      Query = r.recognize_google(audio, language='en-in') 
      print("the command is printed=", Query) 
          
    except Exception as e: 
      print(e) 
      print("Say that again sir") 
      return "None"
        
    return Query 

def tellDay(): 
  day = datetime.datetime.today().weekday() + 1

  Day_dict = {1: 'Monday', 2: 'Tuesday',  
              3: 'Wednesday', 4: 'Thursday',  
              5: 'Friday', 6: 'Saturday', 
              7: 'Sunday'} 
    
  if day in Day_dict.keys(): 
    day_of_the_week = Day_dict[day] 
    print(day_of_the_week) 
    speak("The day is " + day_of_the_week) 

def Hello():
  speak("Hello I am Jarvis. How may I help you?")
  # speak('You are a good boy Arthur')
  # speak('Tu sei un buon cane e il migiliore ragazzo, Arturo')
  # speak("Sogni d'oro i miei carini.")
  # speak("I think it's a good idea and I stand by it")

def Take_query():
  Hello()
  while(True):
    query = takeCommand().lower()

    if "open google" in query:
      speak("Opening Google ")
      webbrowser.open('www.google.com')
      continue

    elif "what day is it" in query: 
      tellDay() 
      continue

    elif tellTime.conditions(query):
      tellTime.response(query)
      continue

    elif "bye" in query: 
      speak("Bye then.") 
      exit()

    elif 'look up' in query:
      speak("Checking the wikipedia ")
      query = query.replace('look up', '')

      result = wikipedia.summary(query, sentences=4)
      speak('So apparently, ')
      speak(result)
      speak('Boom.')
      continue

    elif 'tell me your name' in query:
      speak("I am Jarvis.")
      continue

if __name__ == '__main__':
  Take_query()
