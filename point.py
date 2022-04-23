
import pygame


class Point:
    def __init__(self,surface: pygame.Surface, position: tuple, color: tuple, radius: int) -> None:
        super().__init__()
        self.position_x, self.position_y = position
        self.position = position
        self.radius = radius

        self.surface = surface

        self.color = color
        self.defaut_color = color
        self.seleced_color = (0,255,0)
        self.over_color = (255,0,0)

        self.over = False
        self.on_focus = False


    def toggle_over_state(self) -> None:
        self.over = not self.over 

    def set_over_color(self) -> None:
        self.color = self.over_color

    def set_seleced_color(self) -> None:
        self.color =  self.seleced_color

    def set_defaut_color(self) -> None:
        self.color = self.defaut_color  

    def set_position(self, position) -> None:
        self.position = position 
        self.position_x,self.position_y =  self.position 

    def is_on_focus(self, position) -> bool:
        deltaX = (self.position_x - position[0]) ** 2
        deltaY = (self.position_y - position[1]) ** 2

        self.on_focus = self.radius > (deltaX + deltaY) ** 0.5

    def mouse_trigger(self, event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.on_focus : self.toggle_over_state()
        
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if self.on_focus : self.toggle_over_state()

    def update_state(self, mouse_position)-> None:
        if self.on_focus and not self.over:
            self.set_seleced_color()    
        elif self.over:
            self.set_over_color()
            self.set_position(mouse_position)
        else:
            self.set_defaut_color() 
        

    def update(self, mouse_position, show_dots = True):
        if show_dots: pygame.draw.circle(self.surface, self.color,(self.position), self.radius)
        self.is_on_focus(mouse_position)
        self.update_state(mouse_position)
        
    