# import speech_recognition as sr
import pyttsx3
# import datetime
# import wikipedia
# import webbrowser
# import os
# import time
# import subprocess
# from ecapture import ecapture as ec
# import wolframalpha
# import json
# import requests

engine = pyttsx3.init() # 'sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) # 7
engine.say("I think it's a good idea and I stand by it")
engine.runAndWait()

def speak(words):
  engine.say(words)
  engine.runAndWait()



# def wishMe():
#   hour = datetime.datetime.now().hour
#   if hour >= 0 and hour < 12:
#     speak('Hello, Good Morning')
#     print('Hello, Good Morning')
#   elif hour >= 12 and hour < 18:
#     speak('Hello, Good Afternoon')
#     print('Hello, Good Afternoon')
#   else:
#     speak('Hello, Good Evening')
#     pring('Hello, Good Evening')

