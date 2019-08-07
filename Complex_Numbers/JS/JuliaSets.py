# Python code for Julia Fractal
from PIL import Image
from time import time
import csv

# driver function
if __name__ == "__main__":
	
	start = time()  # Time to start measuring how much time it takes for the chaos to finish
	
	# Setting the width, height and zoom of the image to be created
	width, height, zoom = 1920, 1080, 1  # Standard is 1920, 1080, 1
	
	img = Image.new("RGB", (width, height), "white")  # creating the new image in RGB mode
	pixel = img.load()  # Allocating the storage for the image and loading the pixel data.
	
	# Setting up the variables according to the chaotic Julia Sets equation to create the fractal
	cX, cY = 1, 1
	moveX, moveY = 0.0, 0.0
	maxIter = 255
	
	# Preparing stuff
	name = ('w' + str(width) + 'h' + str(height) + 'z' + str(zoom) + 'mI' + str(maxIter) + '_L_[' + str(cX) + ',' + str(
		cY) + ']')
	csv_name = (name + '_log.csv')
	png_name = (name + '.png')
	
	# Creating and preparing the cursed CSV file
	csv_log = open(csv_name, mode = 'w')
	header = ['Time Passed', 'Percentage']
	write = csv.DictWriter(csv_log, fieldnames = header)
	write.writeheader()
	
	for x in range(img.size[0]):
		# displaying the progress as percentage
		how_long = float((time()) - start)
		percent = "%.9f %%" % (x / img.size[0] * 100.0)
		print(percent + " Time since start: " + str(how_long) + "s")  # Displayed progress as percentage and
		w_tp = str(how_long)  # how long it has been so far
		write.writerow({'Time Passed': w_tp, 'Percentage': percent})
		
		for y in range(img.size[1]):
			# Actual math
			zx = 1.5 * (x - width / 2) / (0.5 * zoom * width) + moveX
			zy = 1.0 * (y - height / 2) / (0.5 * zoom * height) + moveY
			i = maxIter
			while (zx ** 2) + zy * zy < 4 and i > 1:
				tmp = (zx ** 2) - (zy ** 2) + cX
				zy, zx = 2.0 * zx * zy + cY, tmp
				i -= 1
			
			# convert byte to RGB (3 bytes), kinda magic to get nice colors
			pixel[x, y] = (i << 21) + (i << 10) + i * 8
	
	# to display the created fractal of a mess
	img.show()
	img.save(png_name)
	end = time()
	
	# Stole the time processing code from the Mandelbrot Set code
	total_seconds = float(end - start)  # Total time Seconds etc
	total_minutes = 0
	total_hours = 0
	total_days = 0
	total_weeks = 0
	tt = {}
	
	total_weeks += int(total_seconds // 604_800)
	total_seconds = total_seconds % 604_800
	total_days += int(total_seconds // 86_400)
	total_seconds = total_seconds % 86_400
	total_hours += int(total_seconds // 3600)
	total_seconds = total_seconds % 3600
	total_minutes += int(total_seconds // 60)
	total_seconds = total_seconds % 60
	
	tt['width'] = '{:02}'.format(total_weeks)
	tt['d'] = '{:02}'.format(total_days)
	tt['height'] = '{:02}'.format(total_hours)
	tt['m'] = '{:02}'.format(total_minutes)
	if (str(total_seconds))[1] == '.':
		tt['s'] = ('0' + str(total_seconds))
	else:
		tt['s'] = str(total_seconds)
	
	print("100.00 % Total Processing time was: " + str(tt['width']) + ':' + str(tt['d']) + ':' + str(
		tt['height']) + ':' + str(
		tt['m']) + ':' + str(tt['s']))
	print('The time is written weeks, days, hours, minutes, and seconds.')
	write.writerow({'Time Passed': total_seconds, 'Percentage': "100 %"})
