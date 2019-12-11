import pygame
from sources import guardianPaths
from Level import Level
from TextOnScreen import TextOnScreen
from threading import Timer

class Level2(Level):
     def __init__(self, width, height, player):
          super().__init__(width, height, player, "./src/images/background/h2.jpg")
          self.thereAreEnemies = True
          self.NEW_BASIC_SOUL = pygame.USEREVENT
          self.NEW_COIN = pygame.USEREVENT + 1
          self.END_LEVEL = pygame.USEREVENT + 2
          self.NEW_FIREBALL = pygame.USEREVENT + 3
          self.NEW_DIAMOND = pygame.USEREVENT + 4
          self.NEW_LIVE = pygame.USEREVENT + 5
          pygame.time.set_timer(self.NEW_BASIC_SOUL, 1000)
          pygame.time.set_timer(self.NEW_COIN, 4500)
          pygame.time.set_timer(self.NEW_FIREBALL, 2000)
          pygame.time.set_timer(self.NEW_DIAMOND, 2200)
          pygame.time.set_timer(self.NEW_LIVE, 1500)
          pygame.time.set_timer(self.END_LEVEL, 20000)

     def stopEnemies(self):
          self.thereAreEnemies = False

     def runEvents(self, events, keysPressed, window, width, height):
          super().runBasicEvents(events, keysPressed, window, width, height)
          Timer(15, self.stopEnemies).start()
          for event in events:  
               if(self.thereAreEnemies):
                    if event.type == self.NEW_BASIC_SOUL:  
                         self.enemiesFactory.addSoulBoomerang()
                    if event.type == self.NEW_COIN:
                         self.treasureFactory.addCoin()
                    if event.type == self.NEW_DIAMOND:
                         self.treasureFactory.addDiamond()
                    if event.type == self.NEW_FIREBALL:
                         self.attacksFactory.addAttack()
                         self.attacksFactory.addSuperAttack()
                    if event.type == self.NEW_LIVE:
                         self.livesFactory.addLive()
               elif event.type == self.END_LEVEL:
                    endLevelMessage = TextOnScreen(width/2, height/2, 50, (250, 0, 0), 'Arial', "Fin de nivel 1")
                    window.blit(endLevelMessage.text, endLevelMessage.rect)
                    pygame.display.flip()
                    pygame.time.wait(1000)
                    return {'nextScene': True}
          return {}

         
