import pygame, time
from TextOnScreen import TextOnScreen

class StartScreen(pygame.sprite.Sprite):
     def __init__(self, width, height, background, textStart, soundPath):
          pygame.sprite.Sprite.__init__(self)
          self.background = pygame.image.load(background)
          self.startMessage = TextOnScreen(width/2, height/2 + 150, 45, (255,237,54), 'gothicum', textStart)
          self.startSound = pygame.mixer.Sound(soundPath)

     def initialize(self, window, *others):
          window.blit(self.background, (0,0))
          window.blit(self.startMessage.text, self.startMessage.rect)

     def killAll (self):
          pass

     def runEvents(self, events, *others):
          for event in events :
               if(event.type == pygame.KEYUP):
                    self.startSound.play()
                    return True
          return False