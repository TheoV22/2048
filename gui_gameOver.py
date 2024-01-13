import numpy as np
import pygame
from pygame.locals import *

from constants import *
# from functions import *
import class_grid as grid
from button import *
import menu
import class_gui as gui

class GuiGameOver(gui.Gui):
    def __init__(self,grid_):
        super.__init__(grid_)

    def game_over(self):
        while True:
            self.draw_game()
            self.draw_game_over_screen()
            pygame.display.flip()

            key = self.wait_for_key()
            if key == 'q':
                break
            elif key == "replay":
                m = menu.Menu()
                return m.launch_game()

    def wait_for_key(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return "q"
                elif event.type == KEYDOWN:
                    if event.key == K_q or event.key == K_ESCAPE:
                        return "q"
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_replay.rect.collidepoint(event.pos):
                        return "replay"
                elif event.type == pygame.MOUSEMOTION:
                    return 'mouse', self.button_replay.update_color(event.pos)






