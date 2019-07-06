import sys


def is_reducedEchelon_form(matrix, row, col):
	# your code here 
	
	count = 0
	for i in range(row):
		for j in range(col):
			if(i==j and matrix[i][j] == 1):
				pass
			elif(i!=j and matrix[i][j]==0):
				pass
			else:
				count = 1


	if count == 0:	
		print("Yes,this matrix is in echelon form")
		return True
	else:
		print("No,this matrix isn't in echelon form")
		
		return False

if __name__ == '__main__':
    
	matrix = []
	in_ = open("in.txt",'r')
	
	tmatrix = int(in_.readline())
	for m in range(tmatrix):
		row = int(in_.readline())
		col = int(in_.readline())
		for r in range(row):
			matrix.append(list(map(int,in_.readline().strip().split())))
		
		is_reducedEchelon_form(matrix, row, col)
		matrix = []