import pygame

#def play():
print(pygame.init())
print(pygame.mixer.init())
print(pygame.mixer.music.load('harvard.wav'))
print(pygame.mixer.music.play())
while pygame.mixer.music.get_busy() == True:
    continue

#if __name__ == '__main__':
#    play()
