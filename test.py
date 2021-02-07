import speech_recognition as sr
import pyttsx3
import wave

# Configure Speech Recognition
r = sr.Recognizer()
mic = sr.Microphone(device_index=1)

# Configure Text to Speech
engine = pyttsx3.init()
engine.setProperty('rate', 200)
engine.setProperty('volume', 0.9)

with mic as source:
    r.pause_threshold = 0.5
    r.adjust_for_ambient_noise(source)
    print("Setting minimum energy threshold to {}".format(r.energy_threshold))
    print('Listening...')
    audio = r.listen(source)
try:
    spoken_text = r.recognize_google(audio, language = 'en-US')
    print('you said: ' + spoken_text)
    engine.say('You said: ' + spoken_text)
    engine.runAndWait()
except sr.UnknownValueError:
    print('Google speech recognition could not understand audio')
except sr.RequestError as e:
    print('Could not request results from google speech recognition service: {0}'.format(e))
