import pygame

class TextOnScreen(pygame.sprite.Sprite):
     def __init__(self, xPosition, YPosition, sizeText, color, font, text, value=0):
          pygame.sprite.Sprite.__init__(self)
          self.font = pygame.font.SysFont(font, sizeText)
          self.textOriginal = text
          self.value = value
          self.color = color
          fullText = text + str(value)
          self.text = self.font.render(fullText, True, color)
          self.rect = self.text.get_rect()
          self.rect.center = [xPosition, YPosition]

     def update(self, value):
          self.value += value
          fullText = self.textOriginal + str(self.value)
          self.text = self.font.render(fullText, True, self.color)

     def setValue(self, _value):
          self.value = _value
          fullText = self.textOriginal + str(self.value)
          self.text = self.font.render(fullText, True, self.color)