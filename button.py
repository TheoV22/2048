import pygame
from constants import *


class Button:
    def __init__(self, center_x, center_y, width, height, color, text, font_size, hover_color):
        self.rect = pygame.Rect(center_x-width/2, center_y - height/2, width, height)
        self.color = color
        self.text = text
        self.font = pygame.font.SysFont(GUI["font_type"], font_size)
        self.hover_color = hover_color
        self.current_color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.current_color, self.rect, border_radius=8)
        text_surface = self.font.render(self.text, True, (255,255,255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def update_color(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.current_color = self.hover_color
        else:
            self.current_color = self.color
