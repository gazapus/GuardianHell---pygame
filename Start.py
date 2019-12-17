import pygame, time
from TextOnScreen import TextOnScreen

class StartScreen(pygame.sprite.Sprite):
     """
     Game start scene with only one image and one text. When you tap any key you go to the next scene
     """
     def __init__(self, width, height, background, textStart, soundPath):
          """
          param width: width screen
          param height: height screen
          param background: background screen path
          param textStart: text that will be visible on this scene
          param soundPath: sound that will played to out of this scene
          """
          pygame.sprite.Sprite.__init__(self)
          self.background = pygame.image.load(background)
          self.startMessage = TextOnScreen(width/2, height/2 + 150, 45, (255,237,54), 'gothicum', textStart)
          self.startSound = pygame.mixer.Sound(soundPath)

     def initialize(self, window, *others):
          window.blit(self.background, (0,0))
          window.blit(self.startMessage.text, self.startMessage.rect)

     def runEvents(self, events, *others):
          for event in events :
               if(event.type == pygame.KEYUP):
                    self.startSound.play()
                    return True
          return False