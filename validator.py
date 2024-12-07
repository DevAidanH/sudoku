#Sudoku Validtor for a complete sudoku. Works with NxN grids
#Aidan Humpidge
#07/12/2024

#Sub function which check each number is correct across the row, column and sqaure
def isValid(row, col, puzzle, rangeRow, rangeCol):
    #Checks the number is correct across the row by counting the number of times the number appears in the row, returning true if 1
    rowVal = puzzle [row]
    if rowVal.count(puzzle[row][col]) != 1:
        return False
    
    #Checks the number is correct across the column by first creating a 2d array with all the column values and then counting the number os times the number appears in the row, returning true if 1
    colVal = [puzzle[i][col] for i in range(rangeCol)]
    if colVal.count(puzzle[row][col]) != 1:
        return False
    
    #Generates the correct square size, i.e. if 9x9 grid then each square is 3x3 or a 4x4 grid will be 2x2 
    squareSize = rangeRow // rangeCol
    rowStart = (row // squareSize) * squareSize
    colStart = (col // squareSize) * squareSize
    
    #Checks the number is correct within its square. First it adds all the values in the square to a 2d array and then counts the occurances of the number, if there is only one it will return true
    squVal = []
    for r in range(rowStart, rowStart + squareSize):
        for c in range(colStart, colStart + squareSize):
            squVal.append(puzzle[r][c])
    if squVal.count(puzzle[row][col]) != 1:
        return False

    return True

#Main function to call and pass in the puzzle 
def sudoValidation(puzzle):
    count = 0 #Creating a count var, the puzzle will be ran through isValid() and this function will count the number of true values returned, for example if count = 81 for 9*9 we know all 81 values are correct and the solution is valid

    #Input validation on the puzzle. This assumes it only contains ints and only validates the grid sizes. 
    rangeRow = len(puzzle)
    for i in range (rangeRow): 
        rangeCol = len(puzzle[i]) 
        if rangeCol * rangeRow != rangeRow * rangeRow: #This makes sure the puzzle submitted creates a valid square
            return False
    
    #If input validation is passed then this loop runs and interates through the puzzle, running each number through isValid() and adding one to the count if true is return
    for r in range (rangeRow):
        for c in range(rangeCol):
            if isValid(r,c,puzzle, rangeRow, rangeCol):
                count += 1
    if count == (len(puzzle)*len(puzzle)): #Count for the final output
        return True
    return False