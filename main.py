import pygame, os, sys, time

size = width, height = 600, 400
window = pygame.display.set_mode(size)

def main():
        #inicializar configuracion
        pygame.init()
        #CONFIGURACION DE PANTALLA
        pygame.display.set_caption("My super game")
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        windowIconPath = os.path.join('ico.png')
        windowIconImage = pygame.image.load(windowIconPath)
        pygame.display.set_icon(windowIconImage)
        green = 100,100,100 #tupla
        #CONFIGURACION DE TIEMPO (FPS)
        clock = pygame.time.Clock()
        #CONFIGURACION DE LA LECTURA DEL TECLADO
        pygame.key.set_repeat(30)       #toma cada 30 ms el teclado
        #DECLARACION DE OBJETOS (SPRITES)
        pelota = Ball(width/2, height/2)     #instancia de la clase Ball
        gato = Cat(width/2, height-150)     #instancia de la clase Ball
        grupo = Somegroup()
        #COMIENZA EL JUEGO
        while 1:
                clock.tick(60)  #Velocidad de FPS
                window.fill(green)  #rellena la ventana
                for event in pygame.event.get():   #trae todos los eventos que sucedan
                        if event.type == pygame.QUIT: 
                                sys.exit()
                        elif event.type == pygame.KEYDOWN:
                                gato.update(event)
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                                gameOver()
                if(pygame.sprite.collide_rect(pelota, gato)):
                        pelota.speed[0] = -pelota.speed[0]
                        pelota.speed[1] = -pelota.speed[1]
                #Destruye los elementos del grupo en cuanto colicionen con pelota (True)
                #Devuelve una lista con todos los elementos del grupo que toco pelota
                lista = pygame.sprite.spritecollide(pelota, grupo, True)
                pelota.update()
                window.blit(pelota.image, pelota.rect)  #dibuja una superficie sobre otra
                grupo.draw(window)
                window.blit(gato.image, gato.rect)  #dibuja una superficie sobre otra
                pygame.display.flip()   #actualiza la pantalla

def gameOver():
        font = pygame.font.SysFont('Arial', 60) #seleccion de fuente
        text = font.render('GAME OVER', True, (255, 200, 200))    #rseleccion de texto, color y visibilidad
        text_rect = text.get_rect()
        text_rect.center = [width/2, height/2]
        window.blit(text, text_rect)
        pygame.display.flip()
        time.sleep(3)
        sys.exit()


class Ball(pygame.sprite.Sprite):
        def __init__(self, width, height):
                pygame.sprite.Sprite.__init__(self)
                # load image
                self.image = pygame.image.load('intro_ball.gif')
                # Get rect from image. El recatangulo es importante para pygame ya que ese define la posicion y todo
                self.rect = self.image.get_rect()
                # Set starting position.
                #self.rect.centerx = width #self.rect.centery = height
                self.rect.center = (width, height)
                #Set move speed
                self.speed = [1,1]      #lista x,y

        def update(self):
                #Move the rect
                if self.rect.bottom >= height or self.rect.top <= 0:
                        self.speed[1] = -self.speed[1]
                elif self.rect.right >= width or self.rect.left <= 0:
                        self.speed[0] = -self.speed[0]
                self.rect.move_ip(self.speed)
               

class Cat(pygame.sprite.Sprite):
        def __init__(self, width, height):
                pygame.sprite.Sprite.__init__(self)
                # load image
                self.image = pygame.image.load('gato.png')
                # Get rect from image. El recatangulo es importante para pygame ya que ese define la posicion y todo
                self.rect = self.image.get_rect()
                # Set starting position.
                #self.rect.centerx = width #self.rect.centery = height
                self.rect.center = (width, height)
                #Set move speed
                self.speed = [1,1]      #lista x,y

        def update(self, event):
                if(event.key == pygame.K_LEFT and self.rect.left > 0):
                        self.speed = [-5,0]
                elif(event.key == pygame.K_RIGHT and self.rect.right < width):
                        self.speed = [5,0]
                else:
                        self.speed = [0,0]
                self.rect.move_ip(self.speed)

class Something(pygame.sprite.Sprite):
        def __init__(self, width, height, imagePath):
                pygame.sprite.Sprite.__init__(self)
                # load image
                self.image = pygame.image.load(imagePath)
                # Get rect from image. El recatangulo es importante para pygame ya que ese define la posicion y todo
                self.rect = self.image.get_rect()
                # Set starting position.
                #self.rect.centerx = width #self.rect.centery = height
                self.rect.center = (width, height)

class Somegroup(pygame.sprite.Group):
        def __init__(self):
                pygame.sprite.Group.__init__(self)
                cam = os.path.join('cam.png')
                some1 = Something(0,0, cam)
                pin = os.path.join('pin.png')
                some2 = Something(width, 0, pin)
                self.add(some1)
                self.add(some2)
    
if __name__ == '__main__':
    print("hola")
    main()