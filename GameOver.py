from Text_input import TextInput
import pygame, time
from TextOnScreen import TextOnScreen

class GameOver():
    def __init__(self):
        self.textinput = TextInput()
        self.yourName = TextOnScreen(20, 20, 45, (150,150,0), 'Arial', "Your Name:")
        self.pointsText = TextOnScreen(200, 40, 30, (150,150,0), 'Arial', "Points")
        self.playerPoints = 0

    def initialize(self, window, points):
        pygame.key.set_repeat(100)  
        self.playerPoints = points 
        self.pointsText.setValue(points)

    def killAll(self):
        self.textinput.clear_text()

    def openFile(self):
        originalFile = open('score.txt', 'r+')
        lines = originalFile.readlines()
        new = self.textinput.get_text() + "*" + str(self.playerPoints) + "\n"
        lines.append(new)
        scores = []
        for line in lines:
            if(line):
                dataStrings = line.split("*")
                dataObject = {
                    'name': dataStrings[0],
                    'points': int(dataStrings[1].rstrip("\n"))
                }
                scores.append(dataObject)
        scores.sort(key = lambda x: x['points'], reverse = True)
        newLines = []
        for score in scores:
            print(score)
            newLines.append(score["name"] + "*" + str(score["points"])+"\n")
        originalFile.seek(0)
        originalFile.writelines(newLines)
        originalFile.close()

    def runEvents(self, events, keys, window, *others):
        window.fill((225, 225, 225))
        window.blit(self.yourName.text, self.yourName.rect)
        window.blit(self.pointsText.text, self.pointsText.rect)

        self.textinput.update(events)
        window.blit(self.textinput.get_surface(), (50, 100))
        for event in events :
            if(event.type == pygame.KEYUP):
                if(event.key == pygame.K_RETURN):
                    self.openFile()
                    return True
        False