"""Program intended to be ran inside of a python 3 programing environment"""
"""Program prompts user to enter certain data to create a Minesweeper map"""


import sys
import time


class MinesweeperMap:

    def __init__(self, row=0, column=0, num_of_mines=0, mine_locations=None):
        if mine_locations is None:
            self.mine_locations = []
        else:
            self.mine_locations = mine_locations

        self.row = row  # row of matrix
        self.column = column  # column of matrix
        self.num_of_mines = num_of_mines  # number of mines to be placed into the map
        self.mine_locations = mine_locations  # this will contain our mine locations
        self.matrix = self.create_matrix_grid()  # create matrix with given inputs

    def display_mine_map(self):
        """Function that prints out the Minesweeper Map"""

        # counts are used so whitespace isn't printed at the end of lines
        column_count = 1
        row_end = len(self.matrix)
        column_end = len(self.matrix[0])
        for row in self.matrix:
            for column in row:  # print each column in a row
                if column_count < column_end:  # if the current column isn't at the end of the map then we print with a space after
                    print(column, end=" ")  # prints a space after element
                    column_count += 1
                else:  # we are at the end of the row
                    print(column, end="\n")
                    column_count = 1  # reset the column count
        print("\n!!complete!!")

    def create_matrix_grid(self):
        '''Function that creates matrix filled with 0's'''
        '''Has rows and columns as input'''
        matrix = [[0 for x in range(self.column)] for i in range(self.row)]
        return matrix

    def plant_mine(self):
        '''Function that places mines into matrix'''
        for (x, y) in self.mine_locations:  # goes into the each  x, y mine coordinate and plants the mine ("*") into the matrix locations
            self.matrix[x][y] = "*"
        self.check_neighboring_mines()

    def check_neighboring_mines(self):
        '''Function that checks mines neighboring cells'''
        '''Increments the value in neighboring cells if content is not a mine'''
        self.inc_west()
        self.inc_north_west()
        self.inc_north()
        self.inc_north_east()
        self.inc_east()
        self.inc_south_east()
        self.inc_south()
        self.inc_south_west()

    '''These are the functions to check and increment the neighboring cells to the mines---------------------------------------------------------------------------------'''

    def inc_west(self):
        """Check west of each mine location, increment if not a mine"""
        for (x, y) in self.mine_locations:
            if (y != 0):
                if (self.matrix[x][y - 1] != '*'):
                    self.matrix[x][y - 1] += 1

    """Check north west of each mine location, increment if not a mine"""

    def inc_north_west(self):
        for (x, y) in self.mine_locations:
            if (y != 0 and x != 0):
                if (self.matrix[x - 1][y - 1] != '*'):
                    self.matrix[x - 1][y - 1] += 1

    def inc_north(self):
        """Check north of each mine location, increment if not a mine"""
        for (x, y) in self.mine_locations:
            if x != 0:
                if self.matrix[x - 1][y] != '*':
                    self.matrix[x - 1][y] += 1

    def inc_north_east(self):
        """Check north east of each mine location, increment if not a mine"""
        for (x, y) in self.mine_locations:
            if (x != 0) and (y != len(self.matrix[0]) - 1):
                if self.matrix[x - 1][y + 1] != '*':
                    self.matrix[x - 1][y + 1] += 1

    def inc_east(self):
        """Check east of each mine location, increment if not a mine"""
        for (x, y) in self.mine_locations:
            if y != len(self.matrix[0]) - 1:
                if self.matrix[x][y + 1] != '*':
                    self.matrix[x][y + 1] += 1

    def inc_south_east(self):
        """Check south east of each mine location, increment if not a mine"""
        for (x, y) in self.mine_locations:
            if (x != len(self.matrix) - 1) and (
                    y != len(self.matrix[0]) - 1):  # cannot check in the last column or last row of matrix
                if self.matrix[x + 1][y + 1] != '*':
                    self.matrix[x + 1][y + 1] += 1

    def inc_south(self):
        """Check south east of each mine location, increment if not a mine"""
        for (x, y) in self.mine_locations:
            if (x != len(self.matrix) - 1):
                if self.matrix[x + 1][y] != '*':
                    self.matrix[x + 1][y] += 1

    def inc_south_west(self):
        """Check south west of each mine location, increment if not a mine"""
        for (x, y) in self.mine_locations:
            if x != len(self.matrix) - 1 and y != 0:
                if self.matrix[x + 1][y - 1] != '*':
                    self.matrix[x + 1][y - 1] += 1

    '''------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


if __name__ == "__main__":
    def get_mine_locations(num_mines):
        '''Function that returns mine locations as a list of tuples'''
        mine_loc = []
        print("(location start at x and y coordinates (0, 0)")
        for num in range(num_mines):
            r_c = input(
                "{}. mine coordinates (Separated by a space): ".format(num + 1)).strip()  # add one to start at one
            mine_row_and_column = r_c.split(" ")  # string representation of row and column
            mine_row = int(mine_row_and_column[0])  # mine row variable
            mine_column = int(mine_row_and_column[1])  # mine column variable

            location = (mine_row, mine_column)  # this contains the tuple of row, and column of the mine location

            mine_loc.append(location)
        return mine_loc


    def take_input():
        """Takes the input provided by the user and creates a minsweeper map object"""
        """Also implements and prints out an action list for the user to be able to perform certain functions"""

        def print_action_list(mine_grid):
            """Function prints action list for the user to visualize what to type"""
            print("!!Action list!!")
            print("Enter (p) or (print) to print out matrix map with mines")
            print("Enter (m) or (mines) to print out mine locations")
            print("Enter (r) or (restart) to make a new mine map")
            print("Enter (q) or (quit) to exit:")

            while True:
                user_in = input("\nAction: ").strip().lower()

                if user_in == "p" or user_in == "print":
                    mine_grid.display_mine_map()  # print out the minesweeper map

                elif user_in == "m" or user_in == "mines":
                    print("Mine Locations: ", mine_grid.mine_locations)  # print out mine locations

                elif user_in == "r" or user_in == "restart":
                    print("ok lets restart")
                    take_input()  # restarts the process of making a minesweeper map

                elif user_in == "q" or user_in == "quit":
                    print(
                        "Gracias, arigato, thank you! Have a great day! BYE!")  # exits out of the loop which exits program
                    break
                else:
                    print("What was that? please try again...")
                    print_action_list(mine_grid)


        try:
            user_input = input(
                "Enter rows and columns of Minesweeper grid (Separated by a space): ")  # Row and column variable

            row_and_column = user_input.split()  # Splits the input ito a list
            row = int(row_and_column[0])  # Row variable
            column = int(row_and_column[1])  # Column variable
            amount_of_mines = int(input("Enter amount of mines to plant: "))  # mine Variable
            print("\nmax coordinate is one less than the matrix size you specified so ({}, {})".format(row - 1,
                                                                                                         column - 1))
            mines_loc = get_mine_locations(amount_of_mines)
            mine_map = MinesweeperMap(row=row, column=column, num_of_mines=amount_of_mines, mine_locations=mines_loc)
            mine_map.plant_mine()  # calls the minesweeper objects function to plant and create the minesweeper map

            print("\nMinsweeper map loading...")
            time.sleep(1)
            print("....")
            time.sleep(.5)
            print("..")
            print(".")
            time.sleep(1)
            print("Minesweeper map complete\n")
            print_action_list(mine_map)

        except:
            print("Invalid, please try again...")
            take_input()


    def print_program_list():
        print("!!MINESWEEPER MAP PROGRAM!!")
        print("Enter (y) or (yes) to continue")
        print("Enter (q) or (quit) to exit")
        user_input = input().strip().lower()
        if user_input == "y" or user_input == "yes":
            take_input()
        elif user_input == "q" or user_input == "quit":
            print("Thank you, come again!")
            sys.exit()
        else:
            print("Sorry I couldn't understand that, pleas try again")
            print_program_list()


    print_program_list()
