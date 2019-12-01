import pickle, json

def load(fileName):
	with open (fileName, 'rb') as f:
		return pickle.load(f)

def listToString(arr):
        rstr = ""
        for x in range(len(arr)):
                rstr += str(arr[x])
                if x+1!=len(arr):
                        rstr+=", "
        return rstr

def loadOldEvens(fileName):
	evens = []
	with open (fileName, 'rb') as f:
		jData = f.read()
		data = json.loads(jData)
		dict = data[1]

		for key in dict.keys():
			# print(dict[key][1])
			if dict[key][1] % 2 == 0:
				# print(dKeyToIRF(key))
				evens.append(dKeyToIRF(key))
	return evens


def dKeyToIRF(board):
	iRF = []

	i = 0

	while i < len(board):
		row = 0
		while i < len(board) and board[i] != "/":
			if board[i] == "0":
				row += 1
			i += 1
		iRF = [row] + iRF
		i += 1
	return tuple(mirror(clean(iRF)))

def clean(b):
	nB = []
	for r in b:
		if r == 0:
			return nB
		nB.append(r)
	return nB
# def reduceToRF(board):
# 	#print(board)
# 	#display(board)
# 	rowFiles = [0]*len(board)
# 	for i in range(len(board)):
# 		for j in range(len(board[i])):
# 			if board[i][j]:
# 				rowFiles[i] = (len(board[i])-j)
# 				break
# 	return rowFiles

def dKey(board):
	key = ""
	for row in board:
		key += "/"
		for s in row:
			key += str(int(s))
	return key[1:]

def mirror(board):
	# [ for i in range(len(board))]
	mirrored = [0] * board[0] #initialize the mirrored rectangular board
	for i in range(board[0]):
		for j in range(len(board)):
			if board[j] > i:
				mirrored[i] += 1
	return mirrored

def revDKey(key):
	i = 0
	b = []
	while i < len(key):
		row = []
		while i < len(key) and key[i] != "/":
			row.append(bool(int(key[i])))
			i += 1
		b.append(row)
		i += 1
	return b
