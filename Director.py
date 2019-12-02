import pygame, os, sys, time
from Start import StartScreen
from Guardian import Guardian
from sources import guardianPaths
from Level1 import Level1

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
     scene0 = StartScreen(width, height, "./src/images/hell.jpg", "Press any key to start")
     player = Guardian(guardianPaths['run-images'], guardianPaths['stop-image'], guardianPaths['jump-image'], 
          guardianPaths['attack-image'], guardianPaths['attack-sound'], [400, 200], 1, 0)     
     level1 = Level1(width, height, player)
     scenes = []
     scenes.append(scene0)
     scenes.append(level1)
     i = -1
     initialize = True
     sceneData = {}
     quit = False
     while(not quit):
          clock.tick(60)  
          if(initialize):
               i += 1    #salta a la siguiente escena 
               scenes[i].initialize(window)  #inicializa la escena
               initialize = False  
          events = pygame.event.get()
          keysPressed = pygame.key.get_pressed()
          sceneData = scenes[i].runEvents(events, keysPressed, window, width, height)   #ejecuta los eventos en la escena
          if(sceneData.get("nextScene")):    #verifica si tiene que pasar a la siguiente escena
               initialize = True
          for event in events: 
               quit = event.type == pygame.QUIT
          pygame.display.flip() 

if __name__ == "__main__":
    main()
