
import pygame
from pygame.constants import MOUSEBUTTONDOWN,MOUSEBUTTONUP

class Slider:
    def __init__(self, surface:pygame.Surface, position:tuple, size:tuple, color:tuple, start_position:float, label:str) -> None:
      super().__init__()

      self.surface = surface

      #out_line
      self.out_line_position = position 
      self.out_line_size = size 
      self.out_line_rect = (self.out_line_position, self.out_line_size)
      self.out_line_color = color

      #swiper
      self.swiper_percentage = start_position
      self.swiper_radis = size[1] 
      self.swiper_position = (self.out_line_position[0] - self.swiper_radis + self.out_line_size[0] * self.swiper_percentage, 
                              self.out_line_position[1] + self.out_line_size[1] / 2)
      self.swiper_color = (255,255,255)
     

      #fill
      self.fill_position = self.out_line_position
      self.fill_size = (-self.out_line_position[0] + self.swiper_position[0], self.out_line_size[1])
      self.fill_rect = (self.fill_position, self.fill_size)
      self.fill_color = (255,255,255)
      
      #label 
      self.label = label
      self.label_is_visibel = True
      self.font = "monospace"
      self.font_size = 25
      self.font_color = (255,255,255)
      
      #state
      self.over = False
      self.on_focus = False

    def mouse_trigger(self, event) -> None:
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
           if self.on_focus: self.over = True
          
        if event.type == MOUSEBUTTONUP and event.button == 1:
             self.over = False
            
     
    def is_on_focus(self, position) -> bool:
        deltaX = (self.swiper_position[0] - position[0])**2
        deltaY = (self.swiper_position[1] - position[1])**2
        self.on_focus = self.swiper_radis > (deltaX + deltaY)**0.5

    def set_swiper_position(self, position) -> None:
        if self.over:
          if position[0] <= self.out_line_position[0] + self.out_line_size[0] and position[0] >= self.out_line_position[0]:

            self.swiper_position = (position[0],self.swiper_position[1])
            self.fill_size = (-self.out_line_position[0] + self.swiper_position[0], self.out_line_size[1])
            self.fill_rect = (self.fill_position, self.fill_size) 

    def draw_label(self) -> None:
        text_font = pygame.font.SysFont(self.font, self. font_size)
        text = text_font.render(self.label + f"{self.swiper_percentage}" ,1, self.font_color)
        text_rect = text.get_rect()
        text_rect.topleft = (self.out_line_position[0] + self.out_line_size[0] + 15, self.out_line_position[1] - self.font_size / 2)
        self.surface.blit(text,text_rect)

    def draw(self) -> None:
      self.swiper_color = (0,255,0) if self.over else (255,255,255)

      if self.label_is_visibel: self.draw_label()
      radius = self.swiper_radis + 2 if self.on_focus  else self.swiper_radis 

      pygame.draw.rect(self.surface, self.out_line_color, self.out_line_rect, 1, 3)
      pygame.draw.rect(self.surface, self.fill_color,self.fill_rect , 0, 3)
      pygame.draw.circle(self.surface, self.swiper_color, self.swiper_position, radius)

    def get_swiper_percentage(self) -> float:
      return self.swiper_percentage  

    def update(self, mouse_position) -> None:
     self.set_swiper_position(mouse_position)
     self.draw()
     self.is_on_focus(mouse_position)
     self.swiper_percentage = (self.swiper_position [0] - self.out_line_position[0] - self.out_line_size[0]  / self.out_line_size[0] ) / self.out_line_size[0] 
     self.swiper_percentage = 1 if self.swiper_percentage > 0.940 else  self.swiper_percentage
     self.swiper_percentage = 0 if self.swiper_percentage < 0.05 else  self.swiper_percentage
      
     


                       
        
