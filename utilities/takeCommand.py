import speech_recognition as sr
from playsound import playsound

from settings import mic_index

def takeCommand():

  r = sr.Recognizer()

  use_mic_index = mic_index and len(sr.Microphone.list_microphone_names()) > mic_index
  mic = sr.Microphone(device_index=mic_index) if use_mic_index else sr.Microphone()

  with mic as source:
    print('Listening')

    r.pause_threshold = 0.5
    audio = r.listen(source)

    try:
      print("Recognizing")

      Query = r.recognize_google(audio, language='en-in')
      print("I heard: ", Query)

    except Exception as e:
      print(e)
      print("Say that again")
      return "None"
