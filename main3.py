import pygame, os, sys, time
from guardiancopy2 import Guardian
from demon import Demon
from DemonFactory import DemonFactory
from endingLine import EndingLine
from TextOnScreen import TextOnScreen

size = width, height = 800, 600
window = pygame.display.set_mode(size)

def main():
     pygame.init()
     #CONFIGURACION DE PANTALLA
     pygame.display.set_caption("No Escape From Hell")
     windowIconPath = os.path.join('ico.png')
     windowIconImage = pygame.image.load(windowIconPath)
     pygame.display.set_icon(windowIconImage)
     green = 100,100,100 #tupla
     #CONFIGURACION DE TIEMPO (FPS)
     clock = pygame.time.Clock()
     #CONFIGURACION DE LA LECTURA DEL TECLADO
     pygame.key.set_repeat(30)       #toma cada 30 ms el teclado
     #DECLARACION DE OBJETOS (SPRITES)
     player = Guardian((width/2, 100), 3, 0)    
     df = DemonFactory(30, 300, width, height, 'demon.png', 'demonfall.png', 0,-2, 2, False, 1)  
     df2 = DemonFactory(30, 400, width, height, 'demon2.png', 'demon2fall.png', 0,-3, 2, True, 2)
     df3 = DemonFactory(30, 500, width, height, 'demon3.png', 'demon3fall.png', -3,-3, 1, True, 3)
     endingTopLine = EndingLine(width, -50)
     window.blit(endingTopLine.image, endingTopLine.rect)
     demonsGoneQuantity = TextOnScreen(100, 20, 15, (0,0,0), "Demons Gone: ", 0)
     pointsOnScreen = TextOnScreen(700, 20, 15, (0,0,0), "Points: ", 0)
     #COMIENZA EL JUEGO
     while True:
          clock.tick(60)  
          window.fill(green) 

          for event in pygame.event.get():  
               if event.type == pygame.QUIT: 
                    sys.exit()
          keysPressed = pygame.key.get_pressed()

          if(keysPressed[pygame.K_SPACE]):
               demonsAttacked = pygame.sprite.spritecollide(player, df, False)
               demonsAttacked += pygame.sprite.spritecollide(player, df2, False)
               demonsAttacked += pygame.sprite.spritecollide(player, df3, False)
               player.attack(demonsAttacked)

          if(keysPressed[pygame.K_LEFT]):
               player.moveLeft(0)

          if(keysPressed[pygame.K_RIGHT]):
                    player.moveRight(width)

          if(keysPressed[pygame.K_UP]):
               player.jump()

          player.update()
          window.blit(player.image, player.rect) 
             
          demonsGone = pygame.sprite.spritecollide(endingTopLine, df, True)
          demonsGone += pygame.sprite.spritecollide(endingTopLine, df2, True)
          demonsGone += pygame.sprite.spritecollide(endingTopLine, df3, True)
          demonsGoneQuantity.update(len(demonsGone))
          window.blit(demonsGoneQuantity.text, demonsGoneQuantity.rect)

          pointsOnScreen.setValue(player.points)
          window.blit(pointsOnScreen.text, pointsOnScreen.rect)

          df.draw(window)
          df2.draw(window)
          df3.draw(window)
          df3.update()
          df2.update()
          df.update()
          pygame.display.flip() 
          #OTROS

if __name__ == '__main__':
    print("hola")
    main()