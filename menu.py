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
        print(self.starting_numbers)
        print(self.size)
        print(self.probability)
        starting_grid = grid.Grid(starting_numbers=self.starting_numbers,size=self.size,probability=self.probability)

        while starting_grid.is_game_over():
            print("generating new grid")
            starting_grid = grid.Grid(starting_numbers=self.starting_numbers,size=self.size,probability=self.probability)

        gui = c_gui.Gui(starting_grid)
        gui.main()
