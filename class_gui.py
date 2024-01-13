from pygame.locals import *

import class_grid as grid
from button import *
import menu


class Gui(object):

    def __init__(self, grid_):

        """
        in: Grid object
        Initialize the GUI object with the provided grid.
        out: None
        """

        pygame.init()
        pygame.display.set_caption(GUI["title"])

        pygame.font.init()
        self.game_font = pygame.font.SysFont(GUI["font_type"], GUI["grid_font_size"])

        self.screen = pygame.display.set_mode((GUI["W"], GUI["H"]))

        self.grid_ = grid_

        self.button_replay = Button(GUI["W"] * GUI["replay"]["button"]["pos"][0],
                                    GUI["H"] * GUI["replay"]["button"]["pos"][1],
                                    GUI["replay"]["button"]["width"],
                                    GUI["replay"]["button"]["height"],
                                    GUI["replay"]["button"]["color"],
                                    GUI["replay"]["text"],
                                    GUI["replay"]["font_size"],
                                    GUI["replay"]["button"]["hover_color"]
                                    )

    def draw_game(self):
        """
        in: None
        Draw the current state of the grid.
        out: None
        """
        self.screen.fill(CP["back"])

        for i in range(GUI["N"]):
            for j in range(GUI["N"]):
                n = self.grid_.array[i][j]

                rect_x = j * GUI["W"] // GUI["N"] + GUI["SPACING"]
                rect_y = i * GUI["H"] // GUI["N"] + GUI["SPACING"]
                rect_w = GUI["W"] // GUI["N"] - 2 * GUI["SPACING"]
                rect_h = GUI["H"] // GUI["N"] - 2 * GUI["SPACING"]

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
        """
        in: None
        Draw the game over screen on the GUI.
        out: None
        """

        transparency = 25
        self.screen.fill((transparency, transparency, transparency), special_flags=pygame.BLEND_RGB_ADD)

        game_over_font = pygame.font.SysFont(GUI["font_type"], GUI["game_over"]["font_size"], bold=True)
        game_over_surface = game_over_font.render(GUI["game_over"]["text"],True, (0,0,0))
        game_over_rect = game_over_surface.get_rect(
            center=(GUI["W"] * GUI["game_over"]["pos"][0], GUI["H"] * GUI["game_over"]["pos"][1])
        )
        self.screen.blit(game_over_surface, game_over_rect)

        self.button_replay.draw(self.screen)

    def wait_for_key(self):
        """
        in: None
        Wait for a mouse motion, a key or button press and returns the corresponding action.
        out: string
        """

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return "q"
                elif event.type == KEYDOWN:
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
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_replay.rect.collidepoint(event.pos):
                        return "replay"
                elif event.type == pygame.MOUSEMOTION:
                    return self.button_replay.update_color(event.pos)

    def running(self):
        """
        in: None
        Manage the main game loop, handling user input and updating the game state.
        out: None, or game_over() method
        """

        while True:
            self.draw_game()
            pygame.display.flip()
            if self.grid_.is_game_over():
                print("game over")
                return self.game_over()
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
        """
        in: None
        Manage the game over screen, handling user input.
        out: None (exit the game), or Menu.launch_game() (replay)
        """

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

    def main(self):
        """
        in: None
        Main method to start and run the game.
        out: None
        """
        self.running()
