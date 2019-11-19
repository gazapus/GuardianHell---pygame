import pygame

class Guardian(pygame.sprite.Sprite):
        def __init__(self, startingPosition, guardianPath, lives):
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.image.load(guardianPath)
                self.rect = self.image.get_rect()
                self.rect.center = startingPosition
                self.speed = [0,0]
                self.lives = lives

        def update(self, event, width):
                if(event.key == pygame.K_LEFT and self.rect.left > 0):
                        self.speed = [-5,0]
                elif(event.key == pygame.K_RIGHT and self.rect.right < width):
                        self.speed = [5,0]
                else:
                        self.speed = [0,0]
                self.rect.move_ip(self.speed)