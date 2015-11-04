#given two string decide if one is permutation of other

def isPermutation(str1, str2):
	chars = []
	for i in str1:
		chars.append(i)

	for j in str2:
		if not j in str1: return False
		else: chars.remove(j)

	return False if chars else True
