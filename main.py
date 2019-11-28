import pygame, os, sys, time
from Guardian copy import Guardian
from Demon import Demon
from Factory import Factory
from EndingLine import EndingLine
from TextOnScreen import TextOnScreen

size = width, height = 800, 600
window = pygame.display.set_mode(size)
#CONFIGURACION DE PANTALLA
pygame.display.set_caption("No Escape From Hell")
windowIconPath = os.path.join('./src/images/ico.png')
windowIconImage = pygame.image.load(windowIconPath)
pygame.display.set_icon(windowIconImage)

def main():
     pygame.init()
     green = 100,100,100 #tupla
     #CONFIGURACION DE TIEMPO (FPS)
     clock = pygame.time.Clock()
     #CONFIGURACION DE LA LECTURA DEL TECLADO
     pygame.key.set_repeat(30)       #toma cada 30 ms el teclado
     #DECLARACION DE OBJETOS (SPRITES)
     player = Guardian((width/2, 200), 3, 0)    
     endingTopLine = EndingLine(width, -80)
     endingBottomLine = EndingLine(width, height + 300)
     window.blit(endingTopLine.image, endingTopLine.rect)
     demonsGoneQuantity = TextOnScreen(100, 20, 15, (0,0,0), "Demons Gone: ", 0)
     pointsOnScreen = TextOnScreen(700, 20, 15, (0,0,0), "Points: ", 0)
     demonFactory = Factory(width, height)
     treasureFactory = Factory(width, height)
     #DECLARACION DE EVENTOS (FABRICACIÓN DE DEMONIO)
     NEW_DEMON_RED = pygame.USEREVENT
     NEW_DEMON_BLUE = pygame.USEREVENT + 1
     NEW_DEMON_YELLOW = pygame.USEREVENT + 2
     NEW_COIN = pygame.USEREVENT + 3
     pygame.time.set_timer(NEW_DEMON_RED, 2000)
     pygame.time.set_timer(NEW_DEMON_BLUE, 4500)
     pygame.time.set_timer(NEW_DEMON_YELLOW, 5000)
     pygame.time.set_timer(NEW_COIN, 4000)
     #COMIENZA EL JUEGO
     while True: 
          clock.tick(60)  
          window.fill(green) 

          for event in pygame.event.get():  
               if event.type == pygame.QUIT: 
                    sys.exit()
               if event.type == NEW_DEMON_RED:   
                     demonFactory.addDemon((0,0), "./src/images/demon.png", "./src/images/demonfall.png", 0, -2, 2, False, 1)
               if event.type == NEW_DEMON_BLUE:
                    demonFactory.addDemon((0,0), "./src/images/demon2.png", "./src/images/demon2fall.png", 0, -4, 2, True, 1)
               if event.type == NEW_DEMON_YELLOW:
                    demonFactory.addDemon((0,0), "./src/images/demon3.png", "./src/images/demon3fall.png", 2, -3, 1, True, 1)
               if event.type == NEW_COIN:
                    treasureFactory.addTreasure((0,0), "./src/images/goldcoin.png", 0, -3, 10)

          keysPressed = pygame.key.get_pressed()

          if(keysPressed[pygame.K_SPACE]):
               demonsAttacked = pygame.sprite.spritecollide(player, demonFactory, False)
               player.attack(demonsAttacked)

          if(keysPressed[pygame.K_LEFT]):
               player.moveLeft(0)

          if(keysPressed[pygame.K_RIGHT]):
                    player.moveRight(width)

          if(keysPressed[pygame.K_UP]):
               player.jump()

          player.update()
          window.blit(player.image, player.rect) 
          
          treasuresTaken = pygame.sprite.spritecollide(player, treasureFactory, False)
          player.takeTreasure(treasuresTaken)

          pygame.sprite.spritecollide(endingBottomLine, demonFactory, True)
          demonsGone = pygame.sprite.spritecollide(endingTopLine, demonFactory, True)
          demonsGoneQuantity.update(len(demonsGone))
          window.blit(demonsGoneQuantity.text, demonsGoneQuantity.rect)

          pointsOnScreen.setValue(player.points)
          window.blit(pointsOnScreen.text, pointsOnScreen.rect)

          demonFactory.draw(window)
          demonFactory.update()
          treasureFactory.draw(window)
          treasureFactory.update()
          pygame.display.flip() 

if __name__ == '__main__':
    main()