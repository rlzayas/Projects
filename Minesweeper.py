bomb_locations: list = [] #Global list with bomb locations

def create_matrix_grid(row, column):
    '''Function that creates matrix filled with 0's'''
    '''Has rows and columns as input'''
    matrix = [[0 for x in range(column)] for i in range(row)]
    return matrix

def get_bomb_locations(bombs):
    '''Function that gets bomb locations and places them into a list of tuples'''
    global bomb_locations
    bomb_count = 0
    while bomb_count < bombs:
        b_r = input("{}. bomb coordinates (Separated by a space): ".format(bomb_count + 1))
        bomb_row_and_column = b_r.split()
        bomb_row = int(bomb_row_and_column[0])
        bomb_column = int(bomb_row_and_column[1])
        bomb_locations.append(tuple([bomb_row, bomb_column]))
        bomb_count += 1

def plant_mine(matrix):
    '''Function that places bombs into matrix'''
    global bomb_locations
    for element in bomb_locations:
        matrix[element[0]][element[1]] = "*"


def check_neighboring_mines(matrix):
    '''Function that checks bomb neighboring cells'''
    '''Increments the value in neighboring cells if they are not a bomb'''
    global bomb_locations
    inc_west(bomb_locations,matrix)
    inc_north_west(bomb_locations,matrix)
    inc_north(bomb_locations,matrix)
    inc_north_east(bomb_locations,matrix)
    inc_east(bomb_locations,matrix)
    inc_south_east(bomb_locations,matrix)
    inc_south(bomb_locations,matrix)
    inc_south_west(bomb_locations,matrix)

'''These are the functions to check and increment the neighboring cells to the bombs'''
'''---------------------------------------------------------------------------------'''
def inc_west(bomb_locations,matrix):
    for elements in bomb_locations:
        if(elements[1] != 0):
            if(matrix[elements[0]][elements[1] - 1] != '*'):
                matrix[elements[0]][elements[1] - 1] += 1

def inc_north_west(bomb_locations,matrix):
    for elements in bomb_locations:
        if(elements[1] != 0 and elements[0] != 0):
            if(matrix[elements[0]-1][elements[1] - 1] != '*'):
                matrix[elements[0]-1][elements[1] - 1] += 1

def inc_north(bomb_locations,matrix):
    for elements in bomb_locations:
        if(elements[0] != 0):
            if(matrix[elements[0] - 1][elements[1]] != '*'):
                matrix[elements[0] - 1][elements[1]] += 1

def inc_north_east(bomb_locations,matrix):
    for elements in bomb_locations:
        if(elements[0] != 0 and elements[1] != len(matrix[0]) - 1 ):
            if(matrix[elements[0] - 1][elements[1] + 1] != '*'):
                matrix[elements[0] - 1][elements[1] + 1] += 1

def inc_east(bomb_locations,matrix):
    for elements in bomb_locations:
        if(elements[1] != len(matrix[0]) - 1 ):
            if (matrix[elements[0]][elements[1] + 1] != '*'):
                matrix[elements[0]][elements[1] + 1] += 1

def inc_south_east(bomb_locations,matrix):
    for elements in bomb_locations:
        if (elements[0] != (len(matrix) - 1) and elements[1] != len(matrix[0]) - 1):
            if (matrix[elements[0] + 1][elements[1] + 1] != '*'):
                matrix[elements[0] + 1][elements[1] + 1] += 1

def inc_south(bomb_locations,matrix):
    for elements in bomb_locations:
        if (elements[0] != len(matrix) - 1):
            if (matrix[elements[0] + 1][elements[1]] != '*'):
                matrix[elements[0] + 1][elements[1]] += 1

def inc_south_west(bomb_locations,matrix):
    for elements in bomb_locations:
        if (elements[0] != len(matrix) - 1 and elements[1] != 0):
            if (matrix[elements[0] + 1][elements[1] - 1] != '*'):
                matrix[elements[0] + 1][elements[1] - 1] += 1
'''---------------------------------------------------------------------------------'''

def print_mine_map(matrix):
    '''Function that prints out the Minesweeper Map'''
    '''Counts for rows and columns being printed'''
    '''So no extra white-space is printed'''
    row_count = 1
    column_count = 1
    row_end = len(matrix)
    column_end = len(matrix[0])
    for elements in matrix:
        for rows in elements:
            if (column_count < column_end):
                print(rows, end=(" "))
                column_count += 1
            else:
                print(rows, end =(""))
                column_count = 1

        if(row_count < row_end):
            print('\n', end =(""))
            row_count += 1
        else:
            pass



r_c = input("Enter rows and columns of Minesweeper grid (Seperated by a space): ") #Row and column variable
row_and_column = r_c.split() #Splits the input ito a list
row = int(row_and_column[0]) #Row variable
column = int(row_and_column[1]) #Column variable

mine_matrix = create_matrix_grid(row, column) #Create matrix with zeros filling it

amount_of_bombs = int(input("Enter amount of bombs to plant: ")) #Bomb Variable

get_bomb_locations(amount_of_bombs) #Gets rows and column of bomb locations

plant_mine(mine_matrix) #Places bombs into Matrix

check_neighboring_mines(mine_matrix)

print("Bomb locations: ", bomb_locations) #Prints list of bomb coordinates

print("Minesweeper Map:")
print_mine_map(mine_matrix) #Prints the Minesweeper Map
