import pygame
from Level import Level
from TextOnScreen import TextOnScreen
from threading import Timer

class Level5(Level):
     def __init__(self, width, height, player, backgroundPath):
          super().__init__(width, height, player, backgroundPath)
          self.NEW_DOUBLE_SOUL = pygame.USEREVENT
          self.NEW_STRONG_BOOMERANG_SOUL = pygame.USEREVENT + 1
          self.NEW_SUPER_SOUL = pygame.USEREVENT + 2
          self.NEW_SUPER_FIREBALL = pygame.USEREVENT + 3
          self.NEW_DIAMOND = pygame.USEREVENT + 4
          self.NEW_COIN = pygame.USEREVENT + 5
          self.NEW_LIVES = pygame.USEREVENT + 6
          self.END_LEVEL = pygame.USEREVENT + 7
          self.timerStopAll = None

     def initialize(self, window, *others):
          super().initialize()
          window.blit(self.endingTopLine.image, self.endingTopLine.rect)
          pygame.time.set_timer(self.NEW_DOUBLE_SOUL, 4200)
          pygame.time.set_timer(self.NEW_STRONG_BOOMERANG_SOUL, 9100)
          pygame.time.set_timer(self.NEW_SUPER_SOUL, 15400)
          pygame.time.set_timer(self.NEW_SUPER_FIREBALL, 5500)
          pygame.time.set_timer(self.NEW_DIAMOND, 4500)
          pygame.time.set_timer(self.NEW_COIN, 2000)
          pygame.time.set_timer(self.NEW_LIVES, 20000)
          pygame.time.set_timer(self.END_LEVEL, 60000)
          stopTimer = Timer(55, self.stopAll)
          self.timerStopAll = stopTimer
          stopTimer.start()

     def stopAll(self):
          pygame.time.set_timer(self.NEW_STRONG_BOOMERANG_SOUL, 0)
          pygame.time.set_timer(self.NEW_DOUBLE_SOUL, 0)
          pygame.time.set_timer(self.NEW_SUPER_SOUL, 0)
          pygame.time.set_timer(self.NEW_SUPER_FIREBALL, 0)
          pygame.time.set_timer(self.NEW_COIN, 0)
          pygame.time.set_timer(self.NEW_DIAMOND, 0)
          pygame.time.set_timer(self.NEW_LIVES, 0)
          
     def runEvents(self, events, keysPressed, window, width, height):
          if(self.player.lives > 0):
               super().runBasicEvents(events, keysPressed, window, width, height)
               for event in events:  
                    if event.type == self.NEW_DOUBLE_SOUL:  
                         self.enemiesFactory.addSoulBounce()
                         self.enemiesFactory.addSoulBasic()
                    if event.type == self.NEW_STRONG_BOOMERANG_SOUL:  
                         self.enemiesFactory.addSoulBoomerangStrong()
                    if event.type == self.NEW_SUPER_SOUL:  
                         self.enemiesFactory.addSoulBonceBoomerang()
                    if event.type == self.NEW_COIN:
                         self.treasureFactory.addCoin()
                    if event.type == self.NEW_DIAMOND:
                         self.treasureFactory.addDiamond()
                    if event.type == self.NEW_SUPER_FIREBALL:
                         self.attacksFactory.addSuperFireball()
                    if event.type == self.NEW_LIVES:
                         self.livesFactory.addLive()
                         self.livesFactory.addLive()
                    if event.type == self.END_LEVEL:
                         pygame.time.set_timer(self.END_LEVEL, 0)
                         endLevelMessage = TextOnScreen(width/2, height/2, 75, (255, 233, 200), 'impact', "End of Level 5")
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
               gameOverText = TextOnScreen(width/2, height/2, 75,(255, 233, 200), 'impact', "GAME OVER")
               window.blit(gameOverText.text, gameOverText.rect)
               pygame.display.flip()
               pygame.time.wait(2000)
               return True
          return False