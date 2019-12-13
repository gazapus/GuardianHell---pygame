import pygame

class TextOnScreen(pygame.sprite.Sprite):
     def __init__(self, xPosition, YPosition, sizeText, color, font, text, value=0):
          pygame.sprite.Sprite.__init__(self)
          self.font = pygame.font.SysFont(font, sizeText)
          self.textOriginal = text
          self.value = value  #integer
          self.color = color  #tuple
          self.text = self.setFullText(text, value)
          self.rect = self.text.get_rect()
          self.rect.center = [xPosition, YPosition]

     def setFullText(self, text, value=0):
          valueText = (": " + str(value)) if value else ""
          fullText = text + valueText
          newFullText = self.font.render(fullText, True, self.color)
          return newFullText

     def setValue(self, _value):
          self.value = _value
          self.text = self.setFullText(self.textOriginal, _value)

     def updateValue(self, _value):
          self.value += _value
          self.text = self.setFullText(self.textOriginal, self.value)
