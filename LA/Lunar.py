# Lunar Arithmetic, Here we go boys
def addition(a, b):
	a_string, b_string = str(a), str(b)
	
	length_of_longest_str = max(len(a_string), len(b_string))
	
	list_to_be_converted_to_string = []
	index_to_be_viewed = -1
	the_variable_that_makes_sure_we_do_not_mess_up = 0
	while the_variable_that_makes_sure_we_do_not_mess_up < length_of_longest_str:
		a_integer, b_string = int(a_string[index_to_be_viewed]), int(b_string[index_to_be_viewed])
		
		a_length = len(a_string)
		b_length = len(b_string)
		if a_length > b_length:
			b_string += "0" * (a_length - b_length)
		elif b_length > a_length:
			a_string += "0" * (b_length - a_length)
		
		out = str(min(a_integer, b_string))
		list_to_be_converted_to_string.insert(0, out)
		
		the_variable_that_makes_sure_we_do_not_mess_up += 1
		index_to_be_viewed -= 1
	
	output = int(''.join(list_to_be_converted_to_string))
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
			a_zeros = (10 ** a_step) * b_zeros
			
			ab_max = max(int(a_item), int(b_item))
			
			out = str(ab_max * a_zeros)
			a_list.insert(0, out)
			a_step += 1
		b_step += 1
		
		a_list_string = 0
		for the_thing in a_list:
			a_list_string += int(the_thing)
		
		compiled_list.insert(0, str(a_list_string))
	
	total = int(compiled_list[0])
	for the_thing in range(1, len(compiled_list)):
		memory_int = addition(total, compiled_list[the_thing])
		total *= 0
		total += memory_int
	
	return total


test = multiply(12, 12)
print(test)

# https://youtu.be/QH2-TGUlwu4
