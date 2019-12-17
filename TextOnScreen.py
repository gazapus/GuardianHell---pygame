import pygame

class TextOnScreen(pygame.sprite.Sprite):
     """
    This class allows you to create text that can also contain an updatable numeric value 
    that will display on the screen
    """
     def __init__(self, xPosition, YPosition, sizeText, color, font, text, value=0):
          """
          param xPosition: position on the x-axis
          param yPosition: position on the y-axis
          param sizeText: text size
          param color: tuple containing the rgb color values
          param font: type font
          param text: text to show on the screen
          param value: numeric value to show on the screen, if it is zero wont be showed
          """
          pygame.sprite.Sprite.__init__(self)
          self.font = pygame.font.SysFont(font, sizeText)
          self.textOriginal = text
          self.value = value  #integer
          self.color = color  #tuple
          self.text = self.setFullText(text, value)
          self.rect = self.text.get_rect()
          self.rect.center = [xPosition, YPosition]

     def setFullText(self, text, value=0):
          """
          Set the text and value
          """
          valueText = (": " + str(value)) if value else ""
          fullText = text + valueText
          newFullText = self.font.render(fullText, True, self.color)
          return newFullText
     
     def setText(self, text):
          """
          Set just text
          """
          self.text = self.font.render(text, True, self.color)

     def setValue(self, _value):
          """
          Set just value
          """
          self.value = _value
          self.text = self.setFullText(self.textOriginal, _value)

     def updateValue(self, _value):
          """
          add the value received by parameter to the current value
          """
          self.value += _value
          self.text = self.setFullText(self.textOriginal, self.value)
