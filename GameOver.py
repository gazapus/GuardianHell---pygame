from Text_input import TextInput
import pygame, time
from TextOnScreen import TextOnScreen

class GameOver():
    def __init__(self):
        self.textinput = TextInput()
        self.yourName = TextOnScreen(20, 20, 45, (150,150,0), 'Arial', "Your Name:")
        self.points = TextOnScreen(200, 40, 30, (150,150,0), 'Arial', "Points")
        self.playerPoints = 0

    def initialize(self, window, points):
        pygame.key.set_repeat(100)  
        self.playerPoints = points 
        self.points.setValue(points)

    def killAll(self):
        self.textinput.clear_text()

    def runEvents(self, events, keys, window, *others):
        window.fill((225, 225, 225))
        window.blit(self.yourName.text, self.yourName.rect)
        window.blit(self.points.text, self.points.rect)

        self.textinput.update(events)
        window.blit(self.textinput.get_surface(), (50, 100))
        for event in events :
            if(event.type == pygame.KEYUP):
                if(event.key == pygame.K_RETURN):
                    print(self.playerPoints)
                    return True
        False