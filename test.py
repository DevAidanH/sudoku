puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

def findEmpty(puzzle):
    # finds the next empty square 
    for r in range (9):
        for c in range(9):
            if puzzle[r][c] == 0:
                return r, c
    return None, None

def isValid(puzzle, guess, row, col):
    #Return true if valid, return false if not
    rowVal = puzzle [row]
    if guess in rowVal:
        return False
    
    colVal = [puzzle[i][col] for i in range(9)]
    if guess in colVal:
        return False
    
    rowStart = (row // 3) * 3
    colStart = (col // 3) * 3

    for r in range(rowStart, rowStart + 3):
        for c in range(colStart, colStart + 3):
            if puzzle[r][c] == guess:
                return False
            
    return True


def sudoku(puzzle):
    """return the solved puzzle as a 2d array of 9 x 9"""
    row, col = findEmpty(puzzle)

    #Validation if puzzle solved
    if row is None:
        return puzzle

    for guess in range (1, 10):
        if isValid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            if sudoku(puzzle):
                return True
        
        puzzle[row][col] = 0
    
    return False

sudoku(puzzle) 