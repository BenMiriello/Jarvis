from utilities.speak import speak
import wikipedia

def conditions(query):
  return 'look up' in query

def response(query):
  speak("Checking the wikipedia ")
  query = query.replace('look up', '')

  result = wikipedia.summary(query, sentences=2)
  speak('So apparently, ')
  speak(result)
  speak('Boom.')