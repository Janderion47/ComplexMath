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
	return output


def mult(a, b):
	sa, sb = str(a), str(b)
	
	lista = []
	indexa = -1
	powera = 0
	while powera < len(sa):
		number = str(int(sa[indexa]) * (10 ** powera))
		lista.insert(0, number)
		indexa -= 1
		powera += 1
	
	listb = []
	indexb = -1
	powerb = 0
	while powerb < len(sb):
		number = str(int(sb[indexb]) * (10 ** powerb))
		listb.insert(0, number)
		indexb -= 1
		powerb += 1
	
	compiled_list = []
	for ai in lista:
		for bi in listb:
			out = str(max(ai[0], bi[0]))
			
			compiled_list.insert(0, out)


mult(1234, 12345)
# https://youtu.be/QH2-TGUlwu4
