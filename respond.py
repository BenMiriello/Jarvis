from playsound import playsound

def respond(query, feature):
  playsound('audio/star_trek/comms_end_reversed.mp3')
  feature.response(query)
  playsound('audio/star_trek/comms_end.mp3')