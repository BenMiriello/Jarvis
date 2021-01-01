from playsound import playsound

from speak import speak
from takeCommand import takeCommand
from hello import hello
import goodbye
import tellTime
import tellDay
import search
import searchWikipedia

def Take_query():
  hello()
  while(True):
    query = takeCommand()

    if search.conditions(query):
      playsound('audio/star_trek/comms_end_reversed.mp3')
      search.response()
      playsound('audio/star_trek/comms_end.mp3')
      continue

    elif tellDay.conditions(query):
      playsound('audio/star_trek/comms_end_reversed.mp3')
      tellDay.response()
      playsound('audio/star_trek/comms_end.mp3')
      continue

    elif tellTime.conditions(query):
      playsound('audio/star_trek/comms_end_reversed.mp3')
      tellTime.response()
      playsound('audio/star_trek/comms_end.mp3')
      continue

    elif searchWikipedia.conditions(query):
      playsound('audio/star_trek/comms_end_reversed.mp3')
      searchWikipedia.response(query)
      playsound('audio/star_trek/comms_end.mp3')
      continue

    elif goodbye.conditions(query):
      playsound('audio/star_trek/comms_end_reversed.mp3')
      goodbye.response()
      playsound('audio/star_trek/comms_end.mp3')
      exit()

if __name__ == '__main__':
  Take_query()
