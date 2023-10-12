import numpy as np
import random

# ================================ #
#        Grid generation           #
# ================================ #
starting_numbers = [0, 2, 4]
starting_grid = np.random.choice(starting_numbers, 16, p=[0.8, 0.15, 0.05]).reshape(4,4)

starting_grid[0:1,:] # --> lines
starting_grid[:,0:1] # --> Columns

#starting_grid = np.random.randint(0, 5, (4,4))
#starting_grid[starting_grid == 3] = 0
#starting_grid[starting_grid == 1] = 0



# ================================ #
#     Replace one 0 by random      #
# ================================ #

def addRandomToGrid(starting_grid):

    print('Replacing a random 0')

    number_to_add = random.choice((2,2,4))
    counter = 0

    while counter == 0:

        # Select a random row 
        row_number = random.randint(0, 3)
        random_row = starting_grid[row_number] 

        if 0 in random_row:
            while True:
                # Select a random element from the row
                column_number = random.randint(0, 3)
                random_column = random_row[column_number]

                # If 0, replace by random and end the loops
                if random_column == 0:
                    starting_grid[row_number][column_number] = number_to_add
                    counter += 1
                break

    return starting_grid


# ================================ #
#           Movements              #
# ================================ #

def movementDown(starting_grid):

    print('Starting grid: \n', starting_grid)

    for c in range(0, 4):
        column = starting_grid[:,c:c+1]

        # Reorder the numbers to have all the 0 up:
        for _ in range(0,3):
            for j in range(3,0,-1):
                if column[j] == 0:
                    column[j] = column[j-1]
                    column[j-1] = 0

        # Add numbers that are the same
        for j in range(2,-1,-1): # We need to start from the bottom
            if column[j] == column[j+1]:
                column[j+1] += column[j+1]
                column[j] = 0

        # Reorder the numbers to have all the 0 up:
        for _ in range(0,3):
            for j in range(3,0,-1):
                if column[j] == 0:
                    column[j] = column[j-1]
                    column[j-1] = 0

        # print('Final Column: \n',test_column) 
        starting_grid[:,c:c+1] = column

    ending_grid = addRandomToGrid(starting_grid)
    print('Ending grid: \n', ending_grid)

    return ending_grid


def movementUp(starting_grid):

    print('Starting grid: \n', starting_grid)

    for c in range(0, 4):
        column = starting_grid[:,c:c+1]

        # Reorder the numbers to have all the 0 down:
        for _ in range(0,3):
            for j in range(0,3,1):
                if column[j] == 0:
                    column[j] = column[j+1]
                    column[j+1] = 0

        # Add numbers that are the same
        for j in range(0,2,1): # We need to start from the top
            if column[j] == column[j+1]:
                column[j] += column[j]
                column[j+1] = 0

        # Reorder the numbers to have all the 0 down:
        for _ in range(0,3):
            for j in range(0,3,1):
                if column[j] == 0:
                    column[j] = column[j+1]
                    column[j+1] = 0

        # print('Final Column: \n',test_column) 
        starting_grid[:,c:c+1] = column

    ending_grid = addRandomToGrid(starting_grid)
    print('Ending grid: \n', ending_grid)

    return ending_grid


def movementRight(starting_grid):

    print('Starting grid: \n', starting_grid)

    for c in range(0, 4):
        row = starting_grid[c:c+1,:].reshape(4,1)

        # Reorder the numbers to have all the 0 up:
        for _ in range(0,3):
            for j in range(3,0,-1):
                if row[j] == 0:
                    row[j] = row[j-1]
                    row[j-1] = 0

        # Add numbers that are the same
        for j in range(2,-1,-1): # We need to start from the bottom
            if row[j] == row[j+1]:
                row[j+1] += row[j+1]
                row[j] = 0

        # Reorder the numbers to have all the 0 up:
        for _ in range(0,3):
            for j in range(3,0,-1):
                if row[j] == 0:
                    row[j] = row[j-1]
                    row[j-1] = 0

    ending_grid = addRandomToGrid(starting_grid)
    print('Ending grid: \n', ending_grid)

    return ending_grid


def movementLeft(starting_grid):

    print('Starting grid: \n', starting_grid)

    for c in range(0, 4):
        row = starting_grid[c:c+1,:].reshape(4,1)

    # Reorder the numbers to have all the 0 down:
        for _ in range(0,3):
            for j in range(0,3,1):
                if row[j] == 0:
                    row[j] = row[j+1]
                    row[j+1] = 0

        # Add numbers that are the same
        for j in range(0,2,1): # We need to start from the top
            if row[j] == row[j+1]:
                row[j] += row[j]
                row[j+1] = 0

        # Reorder the numbers to have all the 0 down:
        for _ in range(0,3):
            for j in range(0,3,1):
                if row[j] == 0:
                    row[j] = row[j+1]
                    row[j+1] = 0

    ending_grid = addRandomToGrid(starting_grid)
    print('Ending grid: \n', ending_grid)

    return ending_grid

#movementLeft(starting_grid)
#movementRight(starting_grid)
#movementUp(starting_grid)
#movementDown(starting_grid)
