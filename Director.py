import pygame, os, sys, time
from Start import StartScreen
from threading import Timer
from Guardian import Guardian
from Level1 import Level

def main():     
     #Configuración del pantalla   
     resolution = width, height = 600, 800
     window = pygame.display.set_mode(resolution)
     pygame.display.set_caption("No Escape From Hell")
     windowIconImage = pygame.image.load('./src/images/ico.png')
     pygame.display.set_icon(windowIconImage)
     pygame.init()
     clock = pygame.time.Clock()
     pygame.key.set_repeat(30)  
     scene0 = StartScreen(width, height, "./src/images/hell.jpg", "Press any key to start")
     #scene1 = StartScreen("./src/images/hell.jpg", "SCENE 2")
     assetPlayer = {
          "left":"./src/images/guardian-l.png",
          "right":"./src/images/guardian-r.png",
          "left-attack":"./src/images/guardian-l-a.png",
          "right-attack":"./src/images/guardian-r-a.png"
     }
     player = Guardian(assetPlayer, width/2, height/4, 3, 0)   
     sceneLevel1 = Level(width, height, player )
     scenes = []
     scenes.append(scene0)
     scenes.append(sceneLevel1)
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
