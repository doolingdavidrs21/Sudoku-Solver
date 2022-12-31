solved = []
n=9
def output(matrix):
    for i in range(n):
        dup = []
        for j in range(n): dup.append(matrix[i][j])
        solved.append(dup)
    return solved

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0: return (i, j)

def valid(board, pos, num):
    for i in range(9):
        if board[i][pos[1]] == num and (i, pos[1]) != pos: 
            return False
    for j in range(9):
        if board[pos[0]][j] == num and (pos[0], j) != pos:  
            return False
    si = pos[0] - pos[0] % 3 
    sj = pos[1] - pos[1] % 3
    for i in range(3):
        for j in range(3):
            if board[si + i][sj + j] == num and (si + i,sj + j) != pos:
                return False
    return True

def row_check(matrix, row):
	st = set()
	for i in range(0, 9):
		if matrix[row][i] in st:
			return False
		if matrix[row][i] != 0:
			st.add(matrix[row][i])
	return True


def col_check(matrix, col):
	st = set()
	for i in range(0, 9):
		if matrix[i][col] in st:
			return False
		if matrix[i][col] != 0:
			st.add(matrix[i][col])
	return True



def box_check(matrix, startRow, startCol):
	st = set()
	for row in range(0, 3):
		for col in range(0, 3):
			curr = matrix[row + startRow][col + startCol]
			if curr in st:
				return False
			if curr != 0:
				st.add(curr)
	return True


def isValid(matrix, row, col):
    a,b,c=row_check(matrix, row),col_check(matrix, col),box_check(matrix, row - row % 3, col - col % 3)
    if(not a and b and c): msg = "Identical numbers in row"
    elif(a and not b and c): msg = "Identical numbers in column"
    elif(a and b and not c): msg = "Identical numbers in box"
    elif(not a and not b and c): msg = "Identical numbers in row and column"
    elif(not a and b and not c): msg = "Identical numbers in row and box"
    elif(a and not b and not c): msg = "Identical numbers in column and box"
    elif(not a and not b and not c): msg = "Identical numbers in row, column and box"
    else: msg = ""
    return (msg,(a and b and c))


def input_valid(matrix):
    for i in range(0, n):
        for j in range(0, n):
            msg,check = isValid(matrix, i, j)
            if (not check):
                return (msg,False)
    return (msg,True)

def solve_sudoku_(board):
    empty = find_empty(board)
    if not empty:  
        return True
    for nums in range(9):
        if valid(board, empty, nums + 1):
            board[empty[0]][empty[1]] = nums + 1
            if solve_sudoku_(board): 
                return True
            board[empty[0]][empty[1]] = 0 
    return False

