import numpy as np
import pygame
from pygame.locals import *

from constants import CP
# from functions import *
import class_grid as grid
from button import *


class Gui(object):

    ''' put all those constants in constants.py '''
    N = 4
    W = 600
    H = 600
    SPACING = 10
    title = "2048"
    font_type = "Comic Sans MS"
    font_size = 30
    game_over_font_size = 60
    game_over_text = "Game Over"
    replay_text = "replay"

    def __init__(self, grid_):
        pygame.init()
        pygame.display.set_caption(self.title)

        pygame.font.init()
        self.game_font = pygame.font.SysFont(self.font_type, self.font_size)

        self.screen = pygame.display.set_mode((self.W, self.H))

        self.grid_ = grid_

    def draw_game(self):
        self.screen.fill(CP["back"])

        for i in range(self.N):
            for j in range(self.N):
                n = self.grid_.array[i][j]

                rect_x = j * self.W // self.N + self.SPACING
                rect_y = i * self.H // self.N + self.SPACING
                rect_w = self.W // self.N - 2 * self.SPACING
                rect_h = self.H // self.N - 2 * self.SPACING

                pygame.draw.rect(
                    self.screen,
                    CP[n],
                    pygame.Rect(rect_x, rect_y, rect_w, rect_h),
                    border_radius=8,
                )
                if n:  # we don't want zeros to be displayed
                    text_surface = self.game_font.render(f"{n}", True, (0, 0, 0))
                    text_rect = text_surface.get_rect(
                        center=(rect_x + rect_w / 2, rect_y + rect_h / 2)
                    )
                    self.screen.blit(text_surface, text_rect)

    def draw_game_over_screen(self):
        transparency = 25
        self.screen.fill((transparency, transparency, transparency), special_flags=pygame.BLEND_RGB_ADD)

        game_over_font = pygame.font.SysFont(self.font_type, self.game_over_font_size, bold=True)
        game_over_surface = game_over_font.render(self.game_over_text,True, (0,0,0))
        game_over_rect = game_over_surface.get_rect(
            center=(self.W / 2, self.H / 2)
        )
        self.screen.blit(game_over_surface, game_over_rect)

        #pygame.draw.rect(self.screen, (0,0,0), pygame.Rect(300, 500, 100, 40))
        #replay_font = pygame.font.SysFont(self.font_type, self.font_size)
        #replay_surface = replay_font.render(self.replay_text, True, (255,255,255))
        #replay_rect = replay_surface.get_rect(center=(300+50, 500+20))
        #self.screen.blit(replay_surface, replay_rect)



    def wait_for_key(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return "q"
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        return "u"
                    elif event.key == K_RIGHT:
                        return "r"
                    elif event.key == K_LEFT:
                        return "l"
                    elif event.key == K_DOWN:
                        return "d"
                    elif event.key == K_q or event.key == K_ESCAPE:
                        return "q"

    def running(self):
        while True:
            self.draw_game()
            pygame.display.flip()
            if self.grid_.is_game_over():
                print("game over")
                break
            key = self.wait_for_key()
            temp_grid = grid.Grid(self.grid_.array.copy(), None, None, None)
            if key == 'q':
                break
            elif key == 'u':
                self.grid_.movement_up()
            elif key == 'd':
                self.grid_.movement_down()
            elif key == 'l':
                self.grid_.movement_left()
            elif key == 'r':
                self.grid_.movement_right()
            if not self.grid_.is_grid_equal(temp_grid.array):
                self.grid_.add_random_to_grid()

    def game_over(self):
        while True:
            self.draw_game()
            self.draw_game_over_screen()
            #button = Button(300, 500, 100, 40, (0, 0, 0), self.replay_text)
            #button.draw(self.screen)

            pygame.display.flip()

            key = self.wait_for_key()
            if key == 'q':
                break

            """
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if button.rect.collidepoint(event.pos):
                        return 
            """

    def main(self):
        self.running()
        self.game_over()


