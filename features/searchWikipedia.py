from utilities.speak import speak
import wikipedia

def conditions(query):
  validQueries = [
    'wikipedia',
    # 'search wikipedia',
    # 'from wikipedia',
    # 'on wikipedia',
  ]

  return any(string in query for string in validQueries)

def response(query):
  speak("Checking the wikipedia ")
  query = query.replace('look up', '')

  result = wikipedia.summary(query, sentences=2)
  speak('So apparently, ')
  speak(result)
  speak('Boom.')