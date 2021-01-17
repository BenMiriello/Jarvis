# from playsound import playsound
import pygame

def hello():
  print("saying 'hello'...")
  # playsound('audio/star_trek/computer_work_beep_louder.mp3')
  pygame.mixer.init()
  pygame.mixer.music.load('audio/star_trek/computer_work_beep_louder.mp3')
  pygame.mixer.music.play()
  while pygame.mixer.music.get_busy() == True:
    continue
