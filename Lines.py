# by Kristin Henry, 2013 @KristinHenry
#
# Generative Art doodle
# quick and dirty experiment: generate color and line patterns
#

import random, math

import PIL
from PIL import Image, ImageFont, ImageDraw


maxGen = 2
imgSizeX = imgSizeY = 5000	# set default size of image
backgroundColor = "white"
backgroundColorAlpha = "white"

baseColor = [random.randrange(0,255), random.randrange(0,255), random.randrange(0,255), 100]

boxes = [[0, 0, imgSizeX, imgSizeY, baseColor]]


def drawBoxes(draw):
	for box in boxes:

		x1 = box[0]
		y1 = box[1]
		x2 = box[2]
		y2 = box[3]
		c = box[4]

		draw.polygon([(x1,y1), (x2,y1), (x2,y2), (x1,y2)], fill=tuple(c))
		list(c)
		

def getColor(color):

	cmin = -50 
	cmax = 50 
	c1 = [0,0,0,0]
	c1[0] = color[0] + random.randrange(cmin, cmax)  
	c1[1] = color[1] + random.randrange(cmin, cmax) 
	c1[2] = color[2] + random.randrange(cmin, cmax) 
	c1[3] = color[3]
	return list(c1)


def divideBoxes():

	temp = []

	for box in boxes:
		
		c1 = getColor(box[4])
		c2 = getColor(box[4])

		x1 = box[0]
		y1 = box[1]
		x2 = box[2]
		y2 = box[3]

		dx = x2 - x1 
		dy = y2 - y1 

		b1 = [x1, y1, x2, (y2 - dy/2), c1]
		b2 = [x1, (y2 + dy/2), x2, y2, c2]

		temp.append(b1)
		temp.append(b2)

	# clear last generation and save this gen	
	del boxes[:]
	for box in temp:
		boxes.append(box)

	return dy
	

		

# create background 
bkg = Image.new("RGB", (imgSizeX, imgSizeY), backgroundColor)

# create new image to draw into
im = Image.new("RGBA", (imgSizeX, imgSizeY), backgroundColorAlpha)

# Do the drawing
draw = ImageDraw.Draw(im)

drawBoxes(draw)
for i in range(10):
	dy = divideBoxes()
	
	if math.fabs(dy) > 4:
		print len(boxes)
		drawBoxes(draw)


bkg.paste(im, (0,0), im)

# save image with png suffix
bkg.save("lines.png")