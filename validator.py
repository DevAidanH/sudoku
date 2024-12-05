# Test cases, one good and one bad
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

def isValid(row, col, puzzle):
    rowVal = puzzle [row]
    if rowVal.count(puzzle[row][col]) != 1:
        return False
    
    colVal = [puzzle[i][col] for i in range(9)] #again modify for sizes
    if colVal.count(puzzle[row][col]) != 1:
        return False
    
    #Need to fix for smaller sized puzzles
    rowStart = (row // 3) * 3
    colStart = (col // 3) * 3
    
    squVal = []
    for r in range(rowStart, rowStart + 3):
        for c in range(colStart, colStart + 3):
            squVal.append(puzzle[r][c])
    if squVal.count(puzzle[row][col]) != 1:
        return False

    return True

def sudoValidation(puzzle):
    #modify range for sizes
    count = 0
    for r in range (9):
        for c in range(9):
            if isValid(r,c,puzzle):
                count += 1
    if count == (len(puzzle)*len(puzzle)):
        return True
    return False
            
    


print(sudoValidation(goodSudo))
print(sudoValidation(badSudo))