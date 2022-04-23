

import pygame
from cube import Cube
pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 1080,720
BG_COLOR = (50, 50, 50)
DOT_COLOR = (230,230,230)

FPS = 60
CLOCK = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('3d Projection')



def main():
   
    projetion_matrix = [[1,0,0],[0,1,0],[0,0,0]]

    cube = Cube(screen, (WIDTH//2, HEIGHT//2), 100, projetion_matrix)

    while True:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit()


        screen.fill(BG_COLOR)
        cube.update_angle()
        cube.draw()
     
        pygame.display.update()




if __name__ =="__main__":
    main()              