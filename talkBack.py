import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 200)
engine.setProperty('volume', 0.9)
r = sr.Recognizer()
speech = sr.Microphone(device_index=1)
with speech as source:
    audio = r.adjust_for_ambient_noise(source)
    print('Listening...')
    audio = r.listen(source)
try:
    recog = r.recognize_google(audio, language = 'en-US')
    print("You said: " + recog)
    engine.say("You said: " + recog)
    engine.runAndWait()
except sr.UnknownValueError:
    engine.say("Google Speech Recognition could not understand audio")
    engine.runAndWait()
except sr.RequestError as e:
    engine.say("Could not request results from Google Speech Recognition service; {0}".format(e))
    engine.runAndWait()
