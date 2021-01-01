import pyttsx3 

engine = pyttsx3.init() # 'sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[11].id) # 0, 7, 10, 11, 17, 21:Italian, 25, 40, 45

def speak(words):
  engine.say(words)
  engine.runAndWait()