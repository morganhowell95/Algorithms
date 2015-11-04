#determines if all characters are unique
def isUnique(string):
	occur = []
	for letter in string:
		if letter in occur: return False
		occur.append(letter)
	return True

#does this in place
def isUniqueMinimal(string):
	for i in range(string):
		for j in range(string):
			if i!=j and string[i] == string[j]:
				return False

	return True
