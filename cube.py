
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


    def update_angle(self)-> None:
        self.z_angle += 0.01
        self.y_angle += 0.01
        self.x_angle += 0.01


        self.xrotation = [[1, 0, 0],[0, cos(self.x_angle), -sin(self.x_angle)], [0, sin(self.x_angle), cos(self.x_angle)]]

        self.yrotation = [[cos(self.y_angle), 0, sin(self.y_angle)],[0, 1, 0], [-sin(self.y_angle), 0, cos(self.y_angle)]]

        self.zrotation = [[cos(self.z_angle), -sin(self.z_angle), 0],[sin(self.z_angle), cos(self.z_angle),0], [0,0,1]]


    def draw_line(self, start_point, end_point)-> None:
            pygame.draw.line(self.surface, self.line_color, self.projected_poits[start_point], self.projected_poits[end_point], 1)
        
    def draw_cube_lines(self)-> None:
        number_of_face = int(len(self.projected_poits) / 2)
        for point_index in range(number_of_face):
        
             self.draw_line(point_index, (point_index + 1) % number_of_face)
             self.draw_line(point_index + number_of_face, (point_index + 1) % number_of_face + number_of_face)
             self.draw_line(point_index, point_index + number_of_face)
            

        for point in self.projected_poits:
            pygame.draw.line(self.surface,(230,0,0), point, self.center,1)
            

    def draw(self)-> None:
        self.draw_cube_lines()

        self.projected_poits.clear()
        for point in self.cube_points:
            rotaion = np.dot(self.zrotation, point)
            rotaion = np.dot(self.yrotation, rotaion)
            rotaion = np.dot(self.xrotation, rotaion)

            projection2d = np.dot(self.projection_matrix, rotaion)

            x_point_position = -int(projection2d[0][0]* self.size) + self.center[0]
            y_point_position = -int(projection2d[1][0]* self.size) + self.center[1]
            point_position = (x_point_position, y_point_position)
            
            self.projected_poits.append(point_position)

            pygame.draw.circle(self.surface,(0,255,0),point_position,3)
        pygame.draw.circle(self.surface,(255,0,0),self.center,5)
        
        
            

        
