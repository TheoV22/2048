from functions import *

starting_numbers = [0, 2, 4]
starting_grid = np.random.choice(starting_numbers, 16, p=[0.8, 0.15, 0.05]).reshape(4,4)
print("Grid created: \n", starting_grid)

while True:

    direction = input('Which direction to move ? Select between U, D, L, R \n')

    if direction == 'U':
        # Copy to not change starting_grid when changing temp_grid
        temp_grid = movementUp(starting_grid.copy())

        # Check that there is a movement possible
        if (temp_grid==starting_grid).all():
            pass
        else:
            starting_grid = addRandomToGrid(temp_grid)

    elif direction == 'D':
        temp_grid = movementDown(starting_grid.copy())

        if (temp_grid==starting_grid).all():
            pass
        else:
            starting_grid = addRandomToGrid(temp_grid)

    elif direction == 'L':
        temp_grid = movementLeft(starting_grid.copy())

        if (temp_grid==starting_grid).all():
            pass
        else:
            starting_grid = addRandomToGrid(temp_grid)

    elif direction == 'R':
        # temp_grid = starting_grid.copy()
        temp_grid = movementRight(starting_grid.copy())

        if (temp_grid==starting_grid).all():
            pass
        else:
            starting_grid = addRandomToGrid(temp_grid)

    else:
        break

