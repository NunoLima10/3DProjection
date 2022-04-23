

from mysqlx import View
from radioButton import RadioButton
import pygame
from cube import Cube
from point import Point
from slider import Slider
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

    rotation_x_slider = Slider(screen,(30,30), (200,10),DOT_COLOR,0,"Y-Speed ")
    rotation_y_slider = Slider(screen,(30,60), (200,10),DOT_COLOR,0,"Z-Speed ")
    rotation_z_slider = Slider(screen,(30,90), (200,10),DOT_COLOR,0,"X-Speed ")


    show_center_line = RadioButton(screen,(18,150),(255,255,255),12,"Show center line")
    show_corner_points = RadioButton(screen,(18,180),(255,255,255),12,"Show corner points")
    show_out_lines = RadioButton(screen,(18,210),(255,255,255),12,"Show out lines")
    show_line_to_corner = RadioButton(screen,(18,240),(255,255,255),12,"Show line to corner")
    
    show_line_to_corner.selected = False

    viewing_status = [show_center_line.get_state(),
                    show_corner_points.get_state(),
                    show_line_to_corner.get_state(),
                    show_out_lines.get_state()
    ]


    cube = Cube(screen, (WIDTH//2, HEIGHT//2), 100, projetion_matrix)
    center_poit = Point(screen, (WIDTH//2, HEIGHT//2), DOT_COLOR, 5)

    while True:
       

        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit()

            center_poit.mouse_trigger(event)
            rotation_x_slider.mouse_trigger(event)
            rotation_y_slider.mouse_trigger(event)
            rotation_z_slider.mouse_trigger(event)

            show_center_line.mouse_trigger(event)
            show_corner_points.mouse_trigger(event)
            show_line_to_corner.mouse_trigger(event)
            show_out_lines.mouse_trigger(event)
                
        screen.fill(BG_COLOR)
        mouse_position = pygame.mouse.get_pos()
       
        #sliders
        rotation_x_slider.update(mouse_position)
        rotation_y_slider.update(mouse_position)
        rotation_z_slider.update(mouse_position)

        #buttons
        show_corner_points.update(mouse_position)
        show_center_line.update(mouse_position)
        show_line_to_corner.update(mouse_position)
        show_out_lines.update(mouse_position)

        viewing_status = [show_center_line.get_state(),
                    show_corner_points.get_state(),
                    show_line_to_corner.get_state(),
                    show_out_lines.get_state()
        ]


        center_poit.update(mouse_position)

        x_rotation_seed = rotation_x_slider.get_swiper_percentage()
        y_rotation_seed = rotation_y_slider.get_swiper_percentage()
        z_rotation_seed = rotation_z_slider.get_swiper_percentage()

        cube.set_viewing_status(viewing_status)
        cube.update(center_poit.position,x_rotation_seed, y_rotation_seed, z_rotation_seed)
        
     
        pygame.display.update()




if __name__ =="__main__":
    main()              