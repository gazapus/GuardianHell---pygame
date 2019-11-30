import pygame, os, sys, time
from NewDemon import Demon
from sources import guardianPaths
from NewFactory import Factory
from NewLine import Line

size = width, height = 800, 650
window = pygame.display.set_mode(size)

def main():
     pygame.init()
     green = 0,50,100 
     clock = pygame.time.Clock()
     pygame.key.set_repeat(30)  
     NEW_SOUL = pygame.USEREVENT
     pygame.time.set_timer(NEW_SOUL, 3000)  
     factorySoul = Factory(width, height)  

     endingLine = Line(width, 100)
     window.blit(endingLine.image, endingLine.rect)
     while True: 
          clock.tick(60)  
          window.fill(green) 
          for event in pygame.event.get():  
               if event.type == pygame.QUIT: 
                    sys.exit()
               if event.type == NEW_SOUL:  
                    factorySoul.addSoulBounceBoomerangStrong()
          soulsImpact = pygame.sprite.spritecollide(endingLine, factorySoul, False)
          for soul in soulsImpact:
               soul.getAttack(1)
          factorySoul.draw(window)
          factorySoul.update(0, width, height, 0) #cambiae esto
          pygame.display.flip() 

if __name__ == '__main__':
    main()