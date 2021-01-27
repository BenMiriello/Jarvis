import speech_recognition as sr
from playsound import playsound

def takeCommand():

  r = sr.Recognizer()

  with sr.Microphone(device_index=0) as source:
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

if __name__ == '__main__':
  takeCommand()
