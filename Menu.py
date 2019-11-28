import pygame, time
from TextOnScreen import TextOnScreen

class MenuCharacter(pygame.sprite.Sprite):
     def __init__(self, background, *characters, width, height):
          pygame.sprite.Sprite.__init__(self)
          self.background = pygame.image.load(background)
          self.characters = self.saveCharacters(*characters)

     def saveCharacters(self, characters):
          charDicc = {}
          keyCounter = 0
          for character in characters:
               charDicc.update({keyCounter: character})

     def printCharacters(characters, widthScreen, height):
          widthCharacter = widthScreen / len(characters)
          characterPosition = widthCharacter
          for key, character in characters.items():
               character.rect.centerx = characterPosition
               character.rect.centery = height/2



     def runEvents(self, events, window):
          for event in events :
               if(event.type == pygame.KEYUP):
                    return {"nextScene": True}
          window.blit(self.background, (0,0))
          window.blit(self.startMessage.text, self.startMessage.rect)
          return{"nextScene": False}