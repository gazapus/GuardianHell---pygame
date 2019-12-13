import pygame, os, sys, time
from Start import StartScreen
from Guardian import Guardian
from sources import guardianPaths, soundPaths
from Level1 import Level1
from Level2 import Level2
from Level3 import Level3
from GameOver import GameOver

def main():     
     #Configuración del pantalla   
     resolution = width, height = 800, 700
     window = pygame.display.set_mode(resolution)
     pygame.display.set_caption("No Escape From Hell")
     windowIconImage = pygame.image.load('./src/images/ico.png')
     pygame.display.set_icon(windowIconImage)
     pygame.init()
     clock = pygame.time.Clock()
     pygame.key.set_repeat(30)  
     scene0 = StartScreen(width, height, "./src/images/background/h0.jpg", "Press any key to start", soundPaths['start'])
     player = Guardian(guardianPaths['run-images'], guardianPaths['stop-image'], guardianPaths['jump-image'], 
          guardianPaths['attack-image'], guardianPaths['die-images'], soundPaths, [400, 200], 3, 0)     
     level1 = Level1(width, height, player)
     level2 = Level2(width, height, player)
     level3 = Level3(width, height, player)
     scenes = []
     ###
     gameover = GameOver(str(player.points))
     scenes.append(scene0)
     scenes.append(level1)
     scenes.append(gameover)
     #scenes.append(level2)
     #scenes.append(level3)
     i = -1
     initialize = True
     quit = False
     pygame.mixer.Sound(soundPaths['music']).play(-1)

     while(not quit):
          clock.tick(60)  
          if(initialize):
               i += 1    #salta a la siguiente escena 
               scenes[i].initialize(window)  #inicializa la escena
               initialize = False  
          events = pygame.event.get()
          keysPressed = pygame.key.get_pressed()
          nextScene = scenes[i].runEvents(events, keysPressed, window, width, height)   #ejecuta los eventos en la escena
          if(nextScene):    
               initialize = True
          if(player.lives <= 0):
               quit = True
          for event in events: 
               quit = event.type == pygame.QUIT
          pygame.display.flip() 

if __name__ == "__main__":
    main()
