import pygame
from Level import Level
from TextOnScreen import TextOnScreen
from threading import Timer

class Level1(Level):
     def __init__(self, width, height, player, backgroundPath):
          super().__init__(width, height, player, backgroundPath)
          self.NEW_BASIC_SOUL = pygame.USEREVENT
          self.NEW_BOUNCER_SOUL = pygame.USEREVENT + 1
          self.NEW_BOOMERANG_SOUL = pygame.USEREVENT + 2
          self.NEW_FIREBALL = pygame.USEREVENT + 3
          self.NEW_COIN = pygame.USEREVENT + 4
          self.NEW_DIAMOND = pygame.USEREVENT + 5
          self.NEW_LIVE = pygame.USEREVENT + 6
          self.END_LEVEL = pygame.USEREVENT + 7
          self.timerStopAll = None
     
     def initialize(self, window, *others):
          super().initialize()
          window.blit(self.endingTopLine.image, self.endingTopLine.rect)
          pygame.time.set_timer(self.NEW_BASIC_SOUL, 3000)
          pygame.time.set_timer(self.NEW_BOUNCER_SOUL, 8000)
          pygame.time.set_timer(self.NEW_BOOMERANG_SOUL, 10000)
          pygame.time.set_timer(self.NEW_FIREBALL, 5800)
          pygame.time.set_timer(self.NEW_COIN, 4500)
          pygame.time.set_timer(self.NEW_LIVE, 21000)
          pygame.time.set_timer(self.END_LEVEL, 60000)
          stopTimer = Timer(54, self.stopAll)
          self.timerStopAll = stopTimer
          stopTimer.start()

     def stopAll(self):
          pygame.time.set_timer(self.NEW_BASIC_SOUL, 0)
          pygame.time.set_timer(self.NEW_BOUNCER_SOUL, 0)
          pygame.time.set_timer(self.NEW_BOOMERANG_SOUL, 0)
          pygame.time.set_timer(self.NEW_FIREBALL, 0)
          pygame.time.set_timer(self.NEW_COIN, 0)
          pygame.time.set_timer(self.NEW_LIVE, 0)
          
     def runEvents(self, events, keysPressed, window, width, height):
          if(self.player.lives > 0):
               super().runBasicEvents(events, keysPressed, window, width, height)
               for event in events:  
                    if event.type == self.NEW_BASIC_SOUL:  
                         self.enemiesFactory.addSoulBasic()
                    if event.type == self.NEW_BOUNCER_SOUL:  
                         self.enemiesFactory.addSoulBounce()
                    if event.type == self.NEW_BOOMERANG_SOUL:  
                         self.enemiesFactory.addSoulBoomerang()
                    if event.type == self.NEW_COIN:
                         self.treasureFactory.addCoin()
                    if event.type == self.NEW_FIREBALL:
                         self.attacksFactory.addFireball()
                    if event.type == self.NEW_LIVE:
                         self.livesFactory.addLive()
                    if event.type == self.END_LEVEL:
                         pygame.time.set_timer(self.END_LEVEL, 0)
                         endLevelMessage = TextOnScreen(width/2, height/2, 75, (255, 233, 200), 'impact', "End of Level 1")
                         window.blit(endLevelMessage.text, endLevelMessage.rect)
                         pygame.display.flip()
                         pygame.time.wait(1000)
                         return True
                    ###--------------atajo----------------
                    if event.type == pygame.KEYUP:
                         if event.key == pygame.K_TAB:
                              self.stopAll()
                              self.timerStopAll.cancel()
                              pygame.time.set_timer(self.END_LEVEL, 0)
                              return True
          else:
               gameOverText = TextOnScreen(width/2, height/2, 75, (250, 0, 0), 'impact', "GAME OVER")
               window.blit(gameOverText.text, gameOverText.rect)
               self.timerStopAll.cancel()
               pygame.time.set_timer(self.END_LEVEL, 0)
               pygame.display.flip()
               pygame.time.wait(2000)
               return True
          return False