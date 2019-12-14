from Text_input import TextInput
import pygame, time
from TextOnScreen import TextOnScreen


class GameOver():
    def __init__(self):
        self.textinput = TextInput(max_string_length=10)
        self.yourName = TextOnScreen(20, 20, 45, (150, 150, 0), 'Arial',
                                     "Your Name:")
        self.pointsText = TextOnScreen(200, 40, 30, (150, 150, 0), 'Arial',
                                       "Points")
        self.scores = []
        self.playerPoints = 0
        self.inputName = True
        self.once = True

    def initialize(self, window, points):
        pygame.key.set_repeat(100)
        self.playerPoints = points
        self.pointsText.setValue(points)
        self.once = True

    def killAll(self):
        self.textinput.clear_text()

    def openFile(self):
        originalFile = open('score.txt', 'r+')
        lines = originalFile.readlines()
        new = self.textinput.get_text() + "*" + str(self.playerPoints) + "\n"
        lines.append(new)
        #preapra los scores para ordenarlos
        scores = []
        for line in lines:
            dataStrings = line.split("*")
            dataObject = {
                'name': dataStrings[0],
                'points': int(dataStrings[1].rstrip("\n"))
            }
            scores.append(dataObject)
        scores.sort(key=lambda x: x['points'], reverse=True)
        scores.pop()
        self.scores = scores
        #prepara el archivo para guardarlo
        newLines = []
        for score in scores:
            newLines.append(score["name"] + "*" + str(score["points"]) + "\n")
        originalFile.seek(0)
        originalFile.writelines(newLines)
        originalFile.close()

    def runEvents(self, events, keys, window, *others):
        if (self.inputName):
            window.fill((225, 225, 225))
            window.blit(self.yourName.text, self.yourName.rect)
            window.blit(self.pointsText.text, self.pointsText.rect)
            self.textinput.update(events)
            window.blit(self.textinput.get_surface(), (50, 100))
        else:
            if(self.once):
                window.fill((225, 225, 225))
                pos = 50
                counter = 1
                ranking = TextOnScreen(150, 10, 35, (100, 200, 100), 'Arial', "RANKING")
                window.blit(ranking.text, ranking.rect)
                for score in self.scores:
                    positionOnScreen = TextOnScreen(50, pos, 30, (100, 200, 100), 'Arial', str(counter))
                    pointsOnScreen = TextOnScreen(100, pos, 30, (100, 200, 100), 'Arial', str(score["points"]))
                    nameOnScreen = TextOnScreen(200, pos, 30, (100, 200, 100), 'Arial', score["name"])
                    window.blit(positionOnScreen.text, positionOnScreen.rect)
                    window.blit(pointsOnScreen.text, pointsOnScreen.rect)
                    window.blit(nameOnScreen.text, nameOnScreen.rect)
                    pos += 30
                    counter += 1
                self.once = False
        for event in events:
            if (event.type == pygame.KEYUP):
                if (event.key == pygame.K_RETURN):
                    if (self.inputName):
                        self.inputName = False
                        self.openFile()
                    else:
                        self.inputName = True #necesario ?
                        self.once = True # ?
                        return True
        False