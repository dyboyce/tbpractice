def funnel(word, cword):
	pos = 0
	retbo = False
	for position in word:
		check = str(word[:int(pos)]) + str(word[int(pos+1):])
		#print(check)
		if check == cword:
			retbo = True
			return retbo
		pos += 1
		#print(retbo)
	return retbo


def splitster(word1, word2):
	retval = word1[:0]
	pos = 1
	retval2 = word1[:pos]
	print(retval, retval2)

#splitster('colds', 'cold')

retcheck = funnel('colds', 'bold')
print retcheck