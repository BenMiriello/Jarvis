import speech_recognition as sr
from playsound import playsound

import settings

def takeCommand():

  r = sr.Recognizer()

  use_mic_index = settings.mic_index and len(sr.Microphone.list_microphone_names()) > settings.mic_index
  mic_params = {'device_index': settings.mic_index} if use_mic_index else {}

  with sr.Microphone(**mic_params) as source:
    print('Listening')

    r.pause_threshold = 0.5
    audio = r.listen(source)

    try:
      print("Recognizing")

      Query = r.recognize_google(audio, language='en-in')
      print("I heard: ", Query)
      return Query

    except Exception as e:
      print(e)
      print("Say that again")
      return "None"
