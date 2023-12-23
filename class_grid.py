import numpy as np
import random


class Grid(object):

    column = None
    row = None

    def __init__(self, array, starting_numbers, size, numbers_probability):
        self.array = array if array is not None else self.create(starting_numbers, size, numbers_probability)

    def create(self, starting_numbers, size, numbers_probability):
        return np.random.choice(starting_numbers, size, p=numbers_probability)

    def is_game_over(self):

        copy_ = Grid(self.array.copy(),None,None,None)
        copy_.movement_down().movement_up().movement_left().movement_right().add_random_to_grid()

        return self.is_grid_equal(copy_.array)

    def is_grid_equal(self, grid):
        return np.array_equal(self.array, grid)

    def reorder_up(self, column):
        """
        in : numpy array
        Put all numbers == 0 up
        out: numpy array
        """
        l = [i for i in column if i != 0]
        l2 = [i for i in column if i == 0]

        return np.array(l2 + l)

    def reorder_down(self, column):
        """
        in : numpy array
        Put all numbers == 0 down
        out: numpy array
        """
        l = [i for i in column if i != 0]
        l2 = [i for i in column if i == 0]

        return np.array(l + l2)

    def add_from_top(self, column):
        """
        in : numpy array
        Add adjacent numbers that are the same, starting from top
        out: numpy array
        """
        for j in range(0, 3, 1):
            if column[j] == column[j + 1]:
                column[j] += column[j]
                column[j + 1] = 0
        return column

    def add_from_bottom(self, column):
        """
        in : numpy array
        Add adjacent numbers that are the same, starting from bottom
        out: numpy array
        """
        for j in range(2, -1, -1):
            if column[j] == column[j + 1]:
                column[j + 1] += column[j + 1]
                column[j] = 0
        return column

    def add_random_to_grid(self):
        """
        in : numpy array
        Replace one 0 by 2 or 4
        out: numpy array
        """
        zero_positions = np.argwhere(self.array == 0)

        if zero_positions.size > 0:
            position = random.choice(zero_positions)
            number_to_add = random.choice([2, 2, 4])
            self.array[position[0]][position[1]] = number_to_add

        return self

    # ================================ #
    #           Movements              #
    # ================================ #

    def movement_down(self):
        """
        in: numpy array
        Takes the in grid and moves all numbers dows, applying the additions if possible.
        out: numpy array
        """
        copy_down = self.array.copy()

        for c in range(0, 4):
            column = self.array[:, c:c + 1]

            column = self.reorder_up(column)
            column = self.add_from_bottom(column)
            column = self.reorder_up(column)

            copy_down[:, c:c + 1] = column
        self.array = copy_down

        return self

    def movement_up(self):
        """
        in: numpy array
        Takes the in grid and moves all numbers up, applying the additions if possible.
        out: numpy array
        """
        copy_up = self.array.copy()
        for c in range(0, 4):
            column = self.array[:, c:c + 1]

            column = self.reorder_down(column)
            column = self.add_from_top(column)
            column = self.reorder_down(column)

            copy_up[:, c:c + 1] = column

        self.array = copy_up
        return self

    def movement_right(self):
        """
        in: numpy array
        Takes the in grid and moves all numbers right, applying the additions if possible.
        out: numpy array
        """
        copy_right = self.array.copy()
        for c in range(0, 4):
            row = self.array[c:c + 1, :].reshape(4, 1)

            row = self.reorder_up(row)
            row = self.add_from_bottom(row)
            row = self.reorder_up(row)

            copy_right[c:c + 1, :] = row.reshape(1, 4)
        self.array = copy_right
        return self

    def movement_left(self):
        """
        in: numpy array
        Takes the in grid and moves all numbers left, applying the additions if possible.
        out: numpy array
        """
        copy_left = self.array.copy()
        for c in range(0, 4):
            row = self.array[c:c + 1, :].reshape(4, 1)

            row = self.reorder_down(row)
            row = self.add_from_top(row)
            row = self.reorder_down(row)

            copy_left[c:c + 1, :] = row.reshape(1, 4)
        self.array = copy_left
        return self

