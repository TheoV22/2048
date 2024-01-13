import class_grid as grid
import class_gui as c_gui
import constants


class Menu(object):

    starting_numbers = constants.GRID["starting_numbers"]
    size = constants.GRID["size"]
    probability = constants.GRID["probability"]

    def __init__(self):
        pass

    def launch_game(self):
        """
        in: None
        Initialise a Grid object and launch the game
        out: None
        """
        starting_grid = grid.Grid(None,self.starting_numbers,self.size,self.probability)

        while starting_grid.is_game_over():  # in case the random grid is only composed of zeros
            print("generating new grid")
            starting_grid = grid.Grid(None,self.starting_numbers,self.size,self.probability)

        gui = c_gui.Gui(starting_grid)
        gui.main()
