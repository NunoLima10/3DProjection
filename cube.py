
from turtle import position
import numpy as np
import pygame
from math import cos, sin

class Cube:
    def __init__(self, surface: pygame.Surface, start_position: tuple, size: int, projection_matrix: list) -> None:
        super().__init__()

        self.center = start_position
        self.projection_matrix = projection_matrix
        self.size = size
        self.surface = surface


        #views
        self.show_corner_points = True
        self.show_line_to_corner = False
        self.show_center_line = True
        self.show_out_lines = True

        #color
        self.line_color = (230,230,230)

        #rotaion
        self.x_angle = 0
        self.y_angle = 0
        self.z_angle = 0

        self.xrotation = [[1, 0, 0],[0, cos(self.x_angle), -sin(self.x_angle)], [0, sin(self.x_angle), cos(self.x_angle)]]

        self.yrotation = [[cos(self.y_angle), 0, sin(self.y_angle)],[0, 1, 0], [-sin(self.y_angle), 0, cos(self.y_angle)]]

        self.zrotation = [[cos(self.z_angle), -sin(self.z_angle), 0],[sin(self.z_angle), cos(self.z_angle),0], [0,0,1]]
        

        self.cube_points = [
        np.matrix([[-1], [-1], [1]]),
        np.matrix([[1], [-1], [1]]),
        np.matrix([[1],  [1], [1]]),
        np.matrix([[-1], [1], [1]]),
        np.matrix([[-1], [-1], [-1]]),
        np.matrix([[1], [-1], [-1]]),
        np.matrix([[1], [1], [-1]]),
        np.matrix([[-1], [1], [-1]])
        ]

        self.projected_poits = []


    def set_viewing_status(self, viewing_status)-> None:
        self.show_center_line = viewing_status[0]
        self.show_corner_points = viewing_status[1]
        self.show_line_to_corner = viewing_status[2]
        self.show_out_lines = viewing_status[3]
    
 
    def update_angle(self, x_rotation_seed, y_rotation_seed, z_rotation_seed)-> None:
        self.z_angle += x_rotation_seed / 10
        self.y_angle += y_rotation_seed / 10
        self.x_angle += z_rotation_seed / 10


        self.xrotation = [[1, 0, 0],[0, cos(self.x_angle), -sin(self.x_angle)], [0, sin(self.x_angle), cos(self.x_angle)]]

        self.yrotation = [[cos(self.y_angle), 0, sin(self.y_angle)],[0, 1, 0], [-sin(self.y_angle), 0, cos(self.y_angle)]]

        self.zrotation = [[cos(self.z_angle), -sin(self.z_angle), 0],[sin(self.z_angle), cos(self.z_angle),0], [0,0,1]]

    def reset_angle(self)-> None:
        self.x_angle = 0
        self.y_angle = 0
        self.z_angle = 0


    def draw_line(self, start_point, end_point)-> None:
            pygame.draw.line(self.surface, self.line_color, self.projected_poits[start_point], self.projected_poits[end_point], 1)
        
    def draw_cube_lines(self)-> None:
        number_of_face = int(len(self.projected_poits) / 2)
        for point_index in range(number_of_face):
        
             self.draw_line(point_index, (point_index + 1) % number_of_face)
             self.draw_line(point_index + number_of_face, (point_index + 1) % number_of_face + number_of_face)
             self.draw_line(point_index, point_index + number_of_face)
            
    def draw_corner_points(self)-> None:
        for point in self.projected_poits:
            pygame.draw.circle(self.surface,(0,255,0),point,  5)

    def draw_line_to_corner(self)-> None:
            for point in self.projected_poits:
                pygame.draw.line(self.surface, (128,128,128), point, self.center, 1)

    # def fill_cube(self)-> None:
    #     #pygame.draw.polygon(self.surface,(200,200,200),self.projected_poits[0:4])
    #     pygame.draw.polygon(self.surface,(170,170,170),self.projected_poits[4:8])


    def interpolation(self,point1,point2, t)-> list:
        x_position = (point1[0]+ point2[0]) * t
        y_position = (point1[1]+ point2[1]) * t
        return(x_position, y_position)
 
    def draw_center_line(self)->None:
            center_point0to1 = self.interpolation(self.projected_poits[0],self.projected_poits[1],0.5)
            center_point0to2 = self.interpolation(self.projected_poits[3],self.projected_poits[1],0.5)
            pygame.draw.line(self.surface,(230,0,0),(center_point0to1[0], self.center[1] - center_point0to2[1]*0.5), self.center,1)
                 

    def generate_projection(self)-> None:
    
        self.projected_poits.clear()
        for point in self.cube_points:
            rotaion = np.dot(self.xrotation, point)
            rotaion = np.dot(self.yrotation, rotaion)
            rotaion = np.dot(self.zrotation, rotaion)

            projection2d = np.dot(self.projection_matrix, rotaion)

            x_point_position = -int(projection2d[0][0]* self.size) + self.center[0]
            y_point_position = -int(projection2d[1][0]* self.size) + self.center[1]
            point_position = (x_point_position, y_point_position)
            
            self.projected_poits.append(point_position)

        

    def update(self, position, x_rotation_seed, y_rotation_seed, z_rotation_seed)-> None:

        self.update_angle(x_rotation_seed, y_rotation_seed, z_rotation_seed)
        self.generate_projection()

        if self.show_center_line: self.draw_center_line()
        if self.show_corner_points: self.draw_corner_points()
        if self.show_line_to_corner: self.draw_line_to_corner()
        if self.show_out_lines: self.draw_cube_lines()

        if x_rotation_seed == y_rotation_seed == z_rotation_seed == 0: self.reset_angle()

        
        self.center = position
        
        
        
            

        
