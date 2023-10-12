from functions import *

starting_numbers = [0, 2, 4]
starting_grid = np.random.choice(starting_numbers, 16, p=[0.8, 0.15, 0.05]).reshape(4,4)
print("Grid created: \n", starting_grid)

while True:

    direction = input('Which direction to move ? Select between U, D, L, R \n')

    if direction == 'U':
        ending_grid = movementUp(starting_grid)

        # Check that there is a movement possible
        if ending_grid.all() != starting_grid.all():
            starting_grid = ending_grid
            starting_grid = addRandomToGrid(starting_grid)

    elif direction == 'D':
        ending_grid = movementDown(starting_grid)

        if ending_grid.all() != starting_grid.all():
            starting_grid = ending_grid
            starting_grid = addRandomToGrid(starting_grid)

    elif direction == 'L':
        ending_grid = movementLeft(starting_grid)

        if ending_grid.all() != starting_grid.all():
            starting_grid = ending_grid
            starting_grid = addRandomToGrid(starting_grid)

    elif direction == 'R':
        ending_grid = movementRight(starting_grid)

        if ending_grid.all() != starting_grid.all():
            starting_grid = ending_grid
            starting_grid = addRandomToGrid(starting_grid)

    else:
        break