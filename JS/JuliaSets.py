# Python code for Julia Fractal
from PIL import Image
from time import time
import csv

# driver function
if __name__ == "__main__":
	
	name = input('What will the file we called?: ')
	csv_name = (name + '_log.csv')
	png_name = (name + '.png')
	
	start = time()
	
	# setting the width, height and zoom
	# of the image to be created
	width, height, zoom = 1920, 1080, 1
	
	# creating the new image in RGB mode
	img = Image.new("RGB", (width, height), "white")
	
	# Allocating the storage for the image and
	# loading the pixel data.
	pixel = img.load()
	
	# setting up the variables according to
	# the equation to create the fractal
	cX, cY = -0.7, 0.27015
	moveX, moveY = 0.0, 0.0
	maxIter = 255
	
	for x in range(img.size[0]):
		percent = "%.7f %%" % (x / img.size[0] * 100.0)
		print(percent)
		for y in range(img.size[1]):
			zx = 1.5 * (x - width / 2) / (0.5 * zoom * width) + moveX
			zy = 1.0 * (y - height / 2) / (0.5 * zoom * height) + moveY
			i = maxIter
			while zx * zx + zy * zy < 4 and i > 1:
				tmp = zx * zx - zy * zy + cX
				zy, zx = 2.0 * zx * zy + cY, tmp
				i -= 1
			
			# convert byte to RGB (3 bytes), kinda
			# magic to get nice colors
			pixel[x, y] = (i << 21) + (i << 10) + i * 8
	
	# to display the created fractal
	img.show()
	img.save(png_name)
	end = time()
	total_time = float(end - start)
	print(total_time)
