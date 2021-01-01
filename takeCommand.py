import speech_recognition as sr

def takeCommand():

  r = sr.Recognizer()

  with sr.Microphone() as source:
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

    return Query.lower()