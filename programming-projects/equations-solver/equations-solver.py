#Fawaz Shah 2016
import fractions
import sys

def GenerateMatrixValues(mat):
    row = []
    for x in range(0, 3, 1):
        lst = ['A', 'B', 'C', 'D']
        for y in range(0, 4, 1):
            column = float(input("equation " + str(x+1) + ": " + lst[y] + " = ")) #takes user input for each column
            row.append(column)
        print("")
        mat[x] = row
        row = []
    CheckSolutions(mat)

def SwapRowsIfNeeded1(mat):
    if mat[0][0] == 0:
        solution_is_possible = False
        for x in range(1, 3, 1): #compares element [0,0] (pivot) with [1,0] and [2,0]
            if mat[x][0] != 0:
                for y in range(0, 4, 1):
                    temp = mat[0][y]
                    mat[0][y] = mat[x][y]
                    mat[x][y] = temp
                solution_is_possible = True
        if solution_is_possible == False:
            print("\nThere are no solutions.")
            sys.exit()
    CheckSolutions(mat)
    return mat

def SwapRowsIfNeeded2(mat):
    if mat[1][1] == 0:
        solution_is_possible = False
        if mat[2][1] != 0: #compares element [1,1] (pivot) with [2,1]
            for y in range(0, 4, 1):
                temp = mat[1][y]
                mat[1][y] = mat[2][y]
                mat[2][y] = temp
            solution_is_possible = True
        if solution_is_possible == False:
            print("\nThere are no solutions.")
            sys.exit()
    CheckSolutions(mat)
    return mat

def SwapRowsIfNeeded3(mat):            
    if mat[2][2] == 0:
        print("There are infinite solutions.") #by this point if [2,2] is 0 then last row is [0, 0, 0, 0] -> this is the RREF criteria for infinite solutions
        sys.exit()
    CheckSolutions(mat)
    return mat
                
def PivotRow(mat, dividend_row): 
    row = []
    divisor = mat[dividend_row][dividend_row]
    for x in mat[dividend_row]: #reduces row so that first element is 1
        column = float(x / divisor)
        row.append(column)
    mat[dividend_row] = row
    CheckSolutions(mat)
    return mat

def SubtractRows(mat, minuend_row, pivot_row):
    row, i = [], 0
    multiple = mat[minuend_row][pivot_row]
    for x in mat[minuend_row]: #reduces row by multiple of a pivot row (Gaussian elimination)
        column = float(x - multiple * mat[pivot_row][i])
        row.append(column)
        i += 1
    mat[minuend_row] = row
    CheckSolutions(mat)
    return mat

def CheckSolutions(mat): #checks if matrix fulfils the RREF criteria for infinite/no solutions
    if mat[2][0] == 0 and mat[2][1] == 0 and mat[2][2] == 0 and mat[2][3] == 0: #if last row is [0, 0, 0, 0], there are infinite solutions
        print("\nThere are infinite solutions.")
        sys.exit()
    elif mat[2][0] == 0 and mat[2][1] == 0 and mat[2][2] == 0 and mat[2][3] != 0: #if last row is [0, 0, 0, *] where * is a constant, there are no solutions
        print("\nThere are no solutions.")
        sys.exit()

print("""this program solves 3 simultaneous equations with 3 unknowns (x, y, z)
equations must be given in the form Ax + By + Cz = D\n """)
original = [[], [], []] #matrix with 3 rows defined    
GenerateMatrixValues(original)
RREF = original #contents of original copied to RREF
RREF = SwapRowsIfNeeded1(RREF)
RREF = PivotRow(RREF, 0)
for x in range(1, 3, 1):
    RREF = SubtractRows(RREF, x, 0)
RREF = SwapRowsIfNeeded2(RREF)
RREF = PivotRow(RREF, 1)
RREF = SubtractRows(RREF, 2, 1)
RREF = SwapRowsIfNeeded3(RREF)
RREF = PivotRow(RREF, 2)
for x in range(1, -1, -1):
    RREF = SubtractRows(RREF, x, 2)
RREF = SubtractRows(RREF, 0, 1)
print("\nThere is a unique solution: ") #if conditions for infinite/no solutions aren't met by now then there must be a unique solution
print("\nx = " + str(fractions.Fraction(RREF[0][3]).limit_denominator()))
print("y = " + str(fractions.Fraction(RREF[1][3]).limit_denominator()))
print("z = " + str(fractions.Fraction(RREF[2][3]).limit_denominator()))
