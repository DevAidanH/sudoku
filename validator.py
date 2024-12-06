# Test cases
goodSudo = [
      [7,8,4, 1,5,9, 3,2,6],
      [5,3,9, 6,7,2, 8,4,1],
      [6,1,2, 4,3,8, 7,5,9],
    
      [9,2,8, 7,1,5, 4,6,3],
      [3,5,7, 8,4,6, 1,9,2],
      [4,6,1, 9,2,3, 5,8,7],
      
      [8,7,6, 3,9,4, 2,1,5],
      [2,4,3, 5,6,1, 9,7,8],
      [1,9,5, 2,8,7, 6,3,4]
    ]

smallGoodSudo = [
      [1,4, 2,3],
      [3,2, 4,1],
    
      [4,1, 3,2],
      [2,3, 1,4]
    ]

smallBadSudo = [
      [1,4, 4,3],
      [3,2, 4,1],
    
      [4,1, 3,2],
      [2,3, 1,4]
    ]

badSudo = [
      [0,2,3, 4,5,6, 7,8,9],
      [1,2,3, 4,5,6, 7,8,9],
      [1,2,3, 4,5,6, 7,8,9],
      
      [1,2,3, 4,5,6, 7,8,9],
      [1,2,3, 4,5,6, 7,8,9],
      [1,2,3, 4,5,6, 7,8,9],
      
      [1,2,3, 4,5,6, 7,8,9],
      [1,2,3, 4,5,6, 7,8,9],
      [1,2,3, 4,5,6, 7,8,9]
    ]

missSizedSudo = [
      [1,2,3,4,5],
      [1,2,3,4],
      [1,2,3,4],  
      [1]
    ]

def isValid(row, col, puzzle, rangeRow, rangeCol):
    rowVal = puzzle [row]
    if rowVal.count(puzzle[row][col]) != 1:
        return False
    
    colVal = [puzzle[i][col] for i in range(rangeCol)]
    if colVal.count(puzzle[row][col]) != 1:
        return False
    
    squareSize = rangeRow // rangeCol
    rowStart = (row // squareSize) * squareSize
    colStart = (col // squareSize) * squareSize
    
    squVal = []
    for r in range(rowStart, rowStart + squareSize):
        for c in range(colStart, colStart + squareSize):
            squVal.append(puzzle[r][c])
    if squVal.count(puzzle[row][col]) != 1:
        return False

    return True

def sudoValidation(puzzle):
    count = 0
    rangeRow = len(puzzle)
    rangeCol = len(puzzle[0]) # ISSUE This only works as it assumes all collums are the same size, This is not the case in the test cases so will need to find a way to check all 
    if rangeCol != rangeRow:
        return False
    for r in range (rangeRow):
        for c in range(rangeCol):
            if isValid(r,c,puzzle, rangeRow, rangeCol):
                count += 1
    if count == (len(puzzle)*len(puzzle)):
        return True
    return False
            
    


#Test cases
print(sudoValidation(goodSudo))
print(sudoValidation(smallGoodSudo))
print(sudoValidation(smallBadSudo))
print(sudoValidation(badSudo))
print(sudoValidation(missSizedSudo))