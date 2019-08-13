# Lunar Arithmetic, Here we go boys
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


def multiply(a, b):
	a_string, b_string = str(a), str(b)
	
	compiled_list = []
	
	b_step = 0
	for b_item in b_string:
		b_zeros = 10 ** b_step
		
		a_list = []
		
		a_step = 0
		for a_item in a_string:
			a_zeros = (10 ** a_step) * (b_zeros)
			
			ab_max = max(int(a_item), int(b_item))
			
			out = str(ab_max * a_zeros)
			a_list.insert(0, out)
			a_step += 1
		b_step += 1
		
		a_list_string = 0
		for i in a_list:
			a_list_string += int(i)
		
		compiled_list.insert(0, str(a_list_string))
	
	# TODO Finish Lunar Multiply
	total = 0
	for i in range(0, len(compiled_list)):
		total = add(total, compiled_list[i])
	
	return total


test = multiply(1111, 1111)
print(test)

# https://youtu.be/QH2-TGUlwu4
