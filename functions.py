import numpy as np
import random


def reorder_up(column):
    """
    in : numpy array
    Put all numbers == 0 up
    out: numpy array
    """
    l = [i for i in column if i != 0]
    l2 = [i for i in column if i == 0]
    return np.array(l2+l)


def reorder_down(column):
    """
    in : numpy array
    Put all numbers == 0 down
    out: numpy array
    """
    l = [i for i in column if i != 0]
    l2 = [i for i in column if i == 0]
    return np.array(l+l2)


def add_from_top(column):
    """
    in : numpy array
    Add adjacent numbers that are the same, starting from top
    out: numpy array
    """
    for j in range(0,3,1):
                    if column[j] == column[j+1]:
                        column[j] += column[j]
                        column[j+1] = 0
    return column


def add_from_bottom(column):
    """
    in : numpy array
    Add adjacent numbers that are the same, starting from bottom
    out: numpy array
    """
    for j in range(2,-1,-1):
        if column[j] == column[j+1]:
            column[j+1] += column[j+1]
            column[j] = 0
    return column


def addRandomToGrid(starting_grid):
    """
    in : numpy array
    Replace one 0 by 2 or 4
    out: numpy array
    """
    zero_positions = np.argwhere(starting_grid == 0)
    
    if zero_positions.size > 0:
        position = random.choice(zero_positions)
        number_to_add = random.choice([2, 2, 4])
        starting_grid[position[0]][position[1]] = number_to_add

        print('Ending grid: \n', starting_grid)
    
    return starting_grid


# ================================ #
#           Movements              #
# ================================ #

def movementDown(starting_grid):
    """
    in: numpy array
    Takes the in grid and moves all numbers dows, applying the additions if possible.
    out: numpy array
    """

    print('Starting grid: \n', starting_grid)

    for c in range(0, 4):

            column = starting_grid[:,c:c+1] 

            column = reorder_up(column)
            column = add_from_bottom(column)
            column = reorder_up(column)

            starting_grid[:,c:c+1] = column

    print('Ending grid:\n', starting_grid)

    return starting_grid


def movementUp(starting_grid):
    """
    in: numpy array
    Takes the in grid and moves all numbers up, applying the additions if possible.
    out: numpy array
    """

    print('Starting grid: \n', starting_grid)

    for c in range(0, 4):
            
            column = starting_grid[:,c:c+1]

            column = reorder_down(column)
            column = add_from_top(column)
            column = reorder_down(column)

            starting_grid[:,c:c+1] = column

    print('Ending grid:\n', starting_grid)

    return starting_grid


def movementRight(starting_grid):
    """
    in: numpy array
    Takes the in grid and moves all numbers right, applying the additions if possible.
    out: numpy array
    """
    
    print('Starting grid: \n', starting_grid)

    for c in range(0, 4):
            
            row = starting_grid[c:c+1,:].reshape(4,1)

            row = reorder_up(row)
            row = add_from_bottom(row)
            row = reorder_up(row)

            starting_grid[c:c+1,:] = row.reshape(1,4)

    return starting_grid


def movementLeft(starting_grid):
    """
    in: numpy array
    Takes the in grid and moves all numbers left, applying the additions if possible.
    out: numpy array
    """

    print('Starting grid: \n', starting_grid)

    for c in range(0, 4):
            
            row = starting_grid[c:c+1,:].reshape(4,1)

            row = reorder_down(row)
            row = add_from_top(row)
            row = reorder_down(row)
            
            starting_grid[c:c+1,:] = row.reshape(1,4)

    return starting_grid






# ===================== ANCIENNES FONCTIONS ===================== #

def reorder_upNonOpti(column):
    for _ in range(0,3):
        for j in range(3,0,-1): # We need to start from the bottom
            if column[j] == 0:
                column[j] = column[j-1]
                column[j-1] = 0

def reorder_downNonOpti(column):  
    for _ in range(0,3):
        for j in range(0,3,1): # We need to start from the top
            if column[j] == 0:
                column[j] = column[j+1]
                column[j+1] = 0


def add_bottomNonOpti(row):
     for j in range(2,-1,-1): # We need to start from the bottom
                if row[j] == row[j+1]:
                    row[j+1] += row[j+1]
                    row[j] = 0


def add_topNonOpti(row):
    for j in range(0,3,1): # We need to start from the top
                if row[j] == row[j+1]:
                    row[j] += row[j]
                    row[j+1] = 0
    
def addRandomToGridNonOpti(starting_grid):
        # Check that we can add a number to the grid
        if 0 in starting_grid:

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
                
            print('Ending grid: \n', starting_grid)

            return starting_grid
