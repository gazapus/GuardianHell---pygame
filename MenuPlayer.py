import pygame

class MenuPlayer():
     def __init__(self, characters):
          self.name = ""
          self.characters = characters

def init(self, window):
     window.fill(100, 100, 100)
     for character in self.characters:
          window.blit(character.image, character.rect)


def runEvents(self, events, keysPressed):
     if(keysPressed[pygame.K_SPACE]):
          print("chose")
     if(keysPressed[pygame.K_LEFT]):
          print("left")
     if(keysPressed[pygame.K_RIGHT]):
          print("right")