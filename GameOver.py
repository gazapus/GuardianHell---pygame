from Text_input import TextInput
import pygame, time
from TextOnScreen import TextOnScreen

class GameOver():
    def __init__(self, player):
        self.textinput = TextInput(text_color=(225, 14, 0), max_string_length=10, font_family='gothicum')
        self.playerPointsOnScreen = TextOnScreen(320, 100, 50, (225, 14, 0), 'gothicum', "POINTS ")
        self.scores = [] 
        self.playerPoints = 0 
        self.inputName = True
        self.showOwnScore = False
        self.player = player

    def initialize(self, window, points):
        self.playerPoints = points
        self.player.setGameOverImage()
        self.loadScoresFromFile()
        self.showOwnScore = True
        self.inputName = self.isNewRecord()
        self.playerPointsOnScreen.setValue(points) 
        self.textinput.clear_text()
        pygame.key.set_repeat(100)
        
    def isNewRecord(self):
        leastScore = self.scores[-1]['points']
        return self.playerPoints > leastScore
        
    def loadScoresFromFile(self):
        originalFile = open('score.txt', 'r')
        lines = originalFile.readlines()[:10]
        scores = []
        for line in lines:
            dataStrings = line.split("*")
            dataObject = {
                'name': dataStrings[0],
                'points': int(dataStrings[1].rstrip("\n"))
            }
            scores.append(dataObject)
        self.scores = scores
        
    def updateScores(self):
        newScore = {
            "name": self.textinput.get_text(),
            "points": self.playerPoints
        }
        self.scores.append(newScore)
        self.scores.sort(key=lambda x: x['points'], reverse=True)
        self.scores.pop()
        
    def saveScoresToFile(self):
        newLines = []
        for score in self.scores:
            newLines.append(score["name"] + "*" + str(score["points"]) + "\n")
        originalFile = open('score.txt', 'w')
        originalFile.writelines(newLines)
        originalFile.close()
        
    """def saveFile(self):
        originalFile = open('score.txt', 'r')
        lines = originalFile.readlines()[:10]
        new = self.textinput.get_text() + " *" + str(self.playerPoints) + "\n"
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
        originalFile.close()
        originalFile = open('score.txt', 'w')
        originalFile.writelines(newLines)
        originalFile.close()"""

    def runEvents(self, events, keys, window, *others):
        if(self.showOwnScore):
            window.fill((0, 0, 0))
            window.blit(self.playerPointsOnScreen.text, self.playerPointsOnScreen.rect)
            if (self.inputName):
                youtNameText = TextOnScreen(100, 200, 40, (225, 14, 0), 'gothicum', "NAME:")
                window.blit(youtNameText.text, youtNameText.rect)
                self.textinput.update(events)
                window.blit(self.textinput.get_surface(), (172, 175))
        else:
            window.fill((0, 0, 0))
            yLinePosition = 100
            counter = 1
            ranking = TextOnScreen(350, 50, 40, (225, 15, 0), 'gothicum', "RANKING")
            window.blit(ranking.text, ranking.rect)
            for score in self.scores:
                positionOnScreen = TextOnScreen(240, yLinePosition, 30, (225, 15, 0), 'gothicum', str(counter))
                pointsOnScreen = TextOnScreen(300, yLinePosition, 30, (225, 15, 0), 'gothicum', str(score["points"]))
                nameOnScreen = TextOnScreen(420, yLinePosition, 30, (225, 15, 0), 'gothicum', score["name"])
                window.blit(positionOnScreen.text, positionOnScreen.rect)
                window.blit(pointsOnScreen.text, pointsOnScreen.rect)
                window.blit(nameOnScreen.text, nameOnScreen.rect)
                yLinePosition += 30
                counter += 1
        window.blit(self.player.image, (300, 450))
        for event in events:
            if (event.type == pygame.KEYUP):
                if (event.key == pygame.K_RETURN):
                    if (self.showOwnScore):
                        self.showOwnScore = False
                        self.updateScores()
                        self.saveScoresToFile()
                    else:
                        return True
        return False