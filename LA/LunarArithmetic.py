def add(a, b):
	sa, sb = str(a), str(b)
	
	length_of_longest_str = max(len(sa), len(sb))
	
	outout = []
	index = -1
	n = 0
	while n < length_of_longest_str:
		ai, bi = int(sa[index]), int(sb[index])
		
		out = str(min(ai, bi))
		outout.insert(0, out)
		
		n += 1
		index -= 1
	
	output = int(''.join(outout))
	print(output)


def mult(a, b):
	sa, sb = str(a), str(b)
	
	length_of_longest_str = max(len(sa), len(sb))
	
	outout = []
	index = -1
	n = 0
	while n < length_of_longest_str:
		ai = 0
		bi = 0
		try:
			ai += int(sa[index])
		except IndexError:
			ai += 0
		finally:
			try:
				bi += int(sb[index])
			except IndexError:
				bi += 0
		
		out = str(max(ai, bi))
		outout.insert(0, out)
		
		n += 1
		index -= 1
	
	output = int(''.join(outout))
	print(output)
