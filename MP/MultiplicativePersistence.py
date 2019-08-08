# This code was converted to Python3 from the Python2 code from the Youtube channel "Numberphile".
# the two videos: https://youtu.be/Wim9WJeDTHQ & https://youtu.be/E4mrC39sEOQ


def per(n, steps = 0):
	if len(str(n)) == 1:
		print(n)
		print('Total Steps ' + str(steps))
		return 'DONE'
	
	steps += 1
	digits = [int(i) for i in str(n)]
	
	result = 1
	for j in digits:
		result *= j
	if len(str(n)) != 1:
		print(result)
	per(result, steps)
