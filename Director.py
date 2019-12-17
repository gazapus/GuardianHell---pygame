import pygame, os, sys, time
from Start import StartScreen
from Guardian import Guardian
from sources import guardianImagesPaths, soundPaths, scenesPaths
from Level1 import Level1
from Level2 import Level2
from Level3 import Level3
from Level4 import Level4
from Level5 import Level5
from Level6 import Level6

from GameOver import GameOver

def main():     
     #initialization  
     os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (250,30)
     pygame.init()
     pygame.mixer.init()
     clock = pygame.time.Clock()
     pygame.key.set_repeat(30)
     #Window configuration
     resolution = width, height = 800, 700
     window = pygame.display.set_mode(resolution)
     pygame.display.set_caption("Guardian Hell")
     pygame.display.set_icon(pygame.image.load('./src/images/ico.png'))
     #Instantiation of player
     player = Guardian(guardianImagesPaths, soundPaths, [400, 200], 3, 0)     
     ### Scenes statement
     scenes = []
     scene0 = StartScreen(width, height, scenesPaths["startScreen"], "Press any key to start", soundPaths['start'])
     level1 = Level1(width, height, player, scenesPaths["level1"])
     level2 = Level2(width, height, player, scenesPaths["level2"])
     level3 = Level3(width, height, player, scenesPaths["level3"])
     level4 = Level4(width, height, player, scenesPaths["level4"])
     level5 = Level5(width, height, player, scenesPaths["level5"])
     level6 = Level6(width, height, player, scenesPaths["level6"])
     gameover = GameOver(player)
     scenes.append(scene0)
     scenes.append(level1)
     scenes.append(level2)
     scenes.append(level3)
     scenes.append(level4)
     scenes.append(level5)
     scenes.append(level6)
     scenes.append(gameover)
     sceneNumber = -1
     runNextScene = True
     quit = False
     #play music
     pygame.mixer.Sound(soundPaths['music']).play(-1)
     #loop of the game
     while(not quit):
          clock.tick(60)  
          if(runNextScene):
               sceneNumber += 1  
               runNextScene = False
               #check if there are still scenes to go
               if(sceneNumber < len(scenes)): 
                    scenes[sceneNumber].initialize(window, player.points) 
                    #check if the current scene is the last and then restart the player lives and points
                    if(sceneNumber == len(scenes) - 1):
                         player.restart()
               else:
                    #restart the scenes. Start from the start screen game
                    sceneNumber = 0
                    scenes[sceneNumber].initialize(window)
          events = pygame.event.get()
          keysPressed = pygame.key.get_pressed()
          #check if the player has lost all their lives and go to the "game over" scene
          if(player.lives <= 0):
               runNextScene = True
               sceneNumber = len(scenes) - 2
          #run the scene behavior according to the events and return true if it must go to the next scene
          runNextScene = scenes[sceneNumber].runEvents(events, keysPressed, window, width, height) 
          for event in events: 
               quit = event.type == pygame.QUIT
          pygame.display.flip()
     pygame.quit() 

if __name__ == "__main__":
    main()
    os._exit(0)
