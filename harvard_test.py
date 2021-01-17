import speech_recognition as sr
from playsound import playsound
r = sr.Recognizer()

# harvard = sr.AudioFile('harvard.wav')
mic = sr.Microphone()

def testHarvard():
  with mic as source:
    audio = r.record(source)
    said_text = r.recognize_google(audio)
    print(said_text)
    print("I heard: ", said_text)

if __name__ == "__main__":
  testHarvard()
