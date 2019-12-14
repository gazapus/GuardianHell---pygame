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
     gameover = GameOver()
     scenes.append(scene0)
     scenes.append(level1)
     scenes.append(gameover)
     #scenes.append(level2)
     #scenes.append(level3)
     levelNumber = -1
     nextScene = True
     quit = False
     pygame.mixer.Sound(soundPaths['music']).play(-1)

     while(not quit):
          clock.tick(60)  
          if(nextScene):
               scenes[levelNumber].killAll()
               levelNumber += 1  
               if(levelNumber < len(scenes)): 
                    scenes[levelNumber].initialize(window, player.points) 
                    nextScene = False 
                    player.lives = 1    #cambiar luego
                    player.points = 0
               else:
                    levelNumber = 0
                    scenes[levelNumber].initialize(window)
                    nextScene = False

          events = pygame.event.get()
          keysPressed = pygame.key.get_pressed()
          nextScene = scenes[levelNumber].runEvents(events, keysPressed, window, width, height) 
          if(player.lives <= 0):
               nextScene = True
               levelNumber = len(scenes) - 2
               player.runDie()
          for event in events: 
               quit = event.type == pygame.QUIT
          pygame.display.flip()
     pygame.quit() 

if __name__ == "__main__":
    main()
    print("Bye")
    os._exit(0)
