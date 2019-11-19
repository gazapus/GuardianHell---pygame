import pygame, os, sys, time
from guardian import Guardian
from demon import Demon

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
     player = Guardian((width/2, 100), 'guardian.png', 3)    
     aDemon = Demon((width/2, height), 'demon.png', [0,-2], 3)    
     bDemon = Demon((width/4, height + 50), 'demon.png', [0,-2], 3)    
     #COMIENZA EL JUEGO
     while True:
          clock.tick(60)  
          window.fill(green) 
          for event in pygame.event.get():  
               if event.type == pygame.QUIT: 
                    sys.exit()
               elif event.type == pygame.KEYDOWN:
                    if(event.key == pygame.K_SPACE and pygame.sprite.collide_rect(player, aDemon)):
                         if(player.rect.centery >= aDemon.rect.top):
                              aDemon.getAttack()
                    if(event.key == pygame.K_SPACE and pygame.sprite.collide_rect(player, bDemon)):
                         if(player.rect.centery >= bDemon.rect.top):
                              bDemon.getAttack()
                    player.update(event, width)
          aDemon.update()
          bDemon.update()
          window.blit(player.image, player.rect) 
          window.blit(aDemon.image, aDemon.rect)  
          window.blit(bDemon.image, bDemon.rect)  
          pygame.display.flip()  

if __name__ == '__main__':
    print("hola")
    main()