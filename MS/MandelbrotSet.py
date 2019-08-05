# Python code for Mandelbrot Fractal


import colorsys
import csv
import time as t
from PIL import Image
from numpy import complex, array

ImageSideLength = int(input("Side length: "))

name = input('What will the file we called?: ')
csv_name = (name + '_log.csv')
png_name = (name + '.png')

start = t.time()


# a function to return a tuple of colors as integer value of rgb
def rgb_conv(i):
	color = 255 * array(colorsys.hsv_to_rgb(1.0, i / 255.0, 0.5))
	return tuple(color.astype(int))


# function defining a mandelbrot
def mandelbrot(x, y):
	c0 = complex(x, y)
	c = 0
	for i in range(1, 1000):
		if abs(c) > 2:
			return rgb_conv(i)
		c = c * c + c0
	return 0, 0, 0


csv_log = open(csv_name, mode = 'w')
header = ['TimePassed', 'Percentage']
write = csv.DictWriter(csv_log,
					   fieldnames = header)
write.writeheader()

img = Image.new('RGB', (ImageSideLength,
						ImageSideLength))
pixels = img.load()

print("Size: " + str(ImageSideLength))
print("Attempt: " + name)
for x in range(img.size[0]):
	
	# displaying the progress as percentage
	
	how_long = float((t.time()) - start)
	percent = "%.7f %%" % (x / ImageSideLength * 100.0)
	print(percent + " Time since start: " + str(how_long) + "s")
	w_tp = str(how_long)
	write.writerow({'TimePassed': w_tp,
					'Percentage': percent})
	for y in range(img.size[1]):
		pixels[x, y] = mandelbrot((x - (0.75 * ImageSideLength)) / (ImageSideLength / 3),
								  (y - (0.50 * ImageSideLength)) / (ImageSideLength / 3))

img.save(png_name)

end = t.time()

total_seconds = float(end - start)  # Total time Seconds etc
total_minutes = 0
total_hours = 0
total_days = 0
total_weeks = 0
tt = {
	'w': None,
	'd': None,
	'h': None,
	'm': None,
	's': None
	}

total_weeks += int(total_seconds // 604_800)
total_seconds = total_seconds % 604_800
total_days += int(total_seconds // 86_400)
total_seconds = total_seconds % 86_400
total_hours += int(total_seconds // 3600)
total_seconds = total_seconds % 3600
total_minutes += int(total_seconds // 60)
total_seconds = total_seconds % 60

tt['w'] = '{:02}'.format(total_weeks)
tt['d'] = '{:02}'.format(total_days)
tt['h'] = '{:02}'.format(total_hours)
tt['m'] = '{:02}'.format(total_minutes)
if (str(total_seconds))[1] == '.':
	tt['s'] = ('0' + str(total_seconds))
else:
	tt['s'] = str(total_seconds)


print("100%")
print("Total Processing time was: " + str(tt['w']) + ':' + str(tt['d']) + ':' + str(tt['h']) + ':' + str(
	tt['m']) + ':' + str(tt['s']))
print('The time is written weeks, days, hours, minutes, and seconds.')
write.writerow({'TimePassed': total_seconds,
				'Percentage': "100 %"})
