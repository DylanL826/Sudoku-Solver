def Display(sudoku):
    for i in range(9):
        print(" ")
        if(i%3 == 0):
            print("-" * 75)
        for j in range(9):
            if(j%3 == 0):
                print("|", end="")
            print(sudoku[i][j], end="\t")
        print("|", end="")
    return

"""Iterate through i'th row, cull known values from row_nums[]"""
# TODO: Implement w/ list comprehension
# TODO: Don't need to pass hole row_nums matrix to this function.
def Check_Row(sudoku, row_nums, i):    
    # Iterate through ea/ cell in i'th row to get all known 
    for j in range(9):
        # If value in row_nums[i] already in sudoku, remove from list.        
        if sudoku[i][j] in row_nums[i]:
            row_nums[i].remove(sudoku[i][j])
    return

"""Cull known values for j'th col_nums"""
# TODO: Implement w/ list comprehension
# TODO: Don't need to pass hole row_nums matrix to this function.
def Check_Column(sudoku, col_nums, j):
    for i in range(9):
        # If value in col_nums[j] alrdady in sudoku, remove from list.        
        if sudoku[i][j] in col_nums[i]:
            col_nums[j].remove(sudoku[i][j])
    return

"""Cull possible sqr_num values"""
# TODO: Implement w/ list comprehension
# TODO: Don't need to pass hole row_nums matrix to this function.
def Check_Square(sudoku, sqr_nums, k):
    # Map k value to (x,y) coordinates.
    for i in range(9):
        x_val = (k//3)*3 + (i//3)
        y_val = (k%3)*3 + (i%3)
        #print(f"({x_val},{y_val})")
        if(sudoku[x_val][y_val] in sqr_nums[k]):
            sqr_nums[k].remove(sudoku[x_val][y_val])
    return

"""Return square num for the (i,j) cell"""
def Get_Sqr_Num(i, j):

    return

"""Check possible nums for cell. If only 1 option, update sudoku and it's lists."""
def Check_Cell(sudoku, i, j):
    #TODO: get references to row, col, sqr lists corresponding to (i,j) cell
    intersect_nums = [x for x in sqr if (x in list2 and x in list3)]
    print("\n", instersect_nums)
    return


def main():
    
    # sudoku to be solved
    row1 = [8,  None,   1,  3,  None,   None,   9,  None,   None]
    row2 = [None,  4,  9,  None,   None,   None,   None,   5,  1]
    row3 = [2,  5,  6,  8,  9,  None,   4,  None,   None]
    row4 = [None,   1,  5,  6,  8,  None,   None,   4,  None]
    row5 = [4,  None,   None,   None,   None,   None,   None,   None,   8]
    row6 = [None,   8,  None,   None,   None,   4,  1,  9,  7]
    row7 = [1,  None,   2,  None,   7,  9,  None,   None,   None]
    row8 = [None,   6,  None,   5,  3,  8,  None,   None,   None]
    row9 = [None,   None,   8,  None,   6,  None,   None,   3,  4]

    sudoku = [row1, row2, row3, row4, row5, row6, row7, row8, row9]

    # List of unknown nums for each row, column, & square
    # E.G. row_nums[i] = unknown numbers of i'th row
    row_nums = []
    col_nums = []
    sqr_nums = []
    for i in range(9):
        row_nums.append([1,2,3,4,5,6,7,8,9])
        col_nums.append([1,2,3,4,5,6,7,8,9])
        sqr_nums.append([1,2,3,4,5,6,7,8,9])
        
    Display(sudoku)
    Check_Cell(sudoku, 0, 0)
    for i in range(9):
        #print("\n\tk:", i)
        Check_Square(sudoku, sqr_nums, i)
        Check_Row(sudoku, row_nums, i)
        Check_Column(sudoku, col_nums, i)
    
    
                
# # Create 2x2x2 matrix
#     my_matrix = []
#     for i in range(2):
#         my_matrix.append([])
#         for j in range(2):
#             my_matrix[i].append([])
#             for k in range(2):
#                 my_matrix[i][j].append([])

#     print(my_matrix)
    return            

    

if __name__ == '__main__':
    main()