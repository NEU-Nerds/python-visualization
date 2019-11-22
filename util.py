import pickle

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
