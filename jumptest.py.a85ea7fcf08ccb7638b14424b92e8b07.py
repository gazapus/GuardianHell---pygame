import pygame, sys
from pygame.locals import *
pygame.init()

def load_image(name):
    image = pygame.image.load(name).convert()
    return image

def resize(obj, w, h):
    global scale
    return pygame.transform.scale(obj, (int(w * scale), int(h * scale)))


pink = (255, 0, 160)
red = (255, 0, 0)
peach = (255, 118, 95)
blue = (0, 0, 255)
blue_1 = (38, 0, 160)
dark_yellow = (255, 174, 0)
green = (38, 137, 0)
orange = (255, 81, 0)
colour = [pink, red, peach, blue, blue_1, dark_yellow, green, orange, green]
clock = pygame.time.Clock()
scale = 4
screen = pygame.display.set_mode((292 * scale, 240 * scale),0, 32)
banner = load_image("banner.png") #292x35
zero = load_image("zero.png") #5x7
c = 0
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    rgb = colour[c]
    c = c + 1
    if c > 7:
        c = 0