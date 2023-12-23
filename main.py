#from functions import *
#from gui import *
import class_grid as grid
import class_gui as c_gui
import menu

m = menu.Menu()
m.launch_game()

'''
starting_numbers = [0, 2, 4]
size = (4,4)
probability = [0.8, 0.15, 0.05]

starting_grid = grid.Grid(None,starting_numbers,size,probability)

while starting_grid.is_game_over():
    print("generating new grid")
    starting_grid = grid.Grid(None,starting_numbers,size,probability)

gui = c_gui.Gui(starting_grid)
gui.main()
'''