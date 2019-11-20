import pygame, os, sys, time
from guardian import Guardian
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
     player = Guardian((width/2, 100), 3)    
     df = DemonFactory(30, 'demon.png', 'demonfall.png', 0,-2, 1)  
     df2 = DemonFactory(30, 'demon2.png', 'demon2fall.png', 0,-3, 1)
     endingLine = EndingLine(width, -50)
     demonsGoneQuantity = TextOnScreen(100, 20, 15, (0,0,0), "Demons Gone: ", 0)
     demonsShotQuantity = TextOnScreen(500, 20, 15, (0,0,0), "Demons shot: ", 0)
     window.blit(endingLine.image, endingLine.rect)
     #COMIENZA EL JUEGO
     while True:
          clock.tick(60)  
          window.fill(green) 
          for event in pygame.event.get():  
               if event.type == pygame.QUIT: 
                    sys.exit()
               elif event.type == pygame.KEYDOWN:
                    if(event.key == pygame.K_SPACE):
                         demonsAttackedDf = pygame.sprite.spritecollide(player, df, False)
                         demonsAttackedDf2 = pygame.sprite.spritecollide(player, df2, False)
                         allDemonsAttacked = demonsAttackedDf + demonsAttackedDf2
                         if(allDemonsAttacked):
                              for demon in allDemonsAttacked:
                                   points = demon.getAttack()
                                   demonsShotQuantity.update(points)
                    player.update(event, width)
          demonsGone = pygame.sprite.spritecollide(endingLine, df, True)
          demonsGone += pygame.sprite.spritecollide(endingLine, df2, True)
          demonsGoneQuantity.update(len(demonsGone))
          window.blit(player.image, player.rect) #recibe la imagen y las coordenadas de su ubicacion(tupla)
          window.blit(demonsGoneQuantity.text, demonsGoneQuantity.rect)
          window.blit(demonsShotQuantity.text, demonsShotQuantity.rect)
          df.draw(window)
          df2.draw(window)
          df2.update()
          df.update()
          pygame.display.flip() 
          #OTROS

if __name__ == '__main__':
    print("hola")
    main()