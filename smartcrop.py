#!/usr/bin/env python

import sys
import Image

print(sys.argv)

if (len(sys.argv) < 3):
	print("Usage: manipulate.py image_1.png ... image_n.png")
	exit(1)

tmp = Image.open(sys.argv[1])

for i in range(1,len(sys.argv)):
	img = Image.open(sys.argv[i])
	tmp.paste(img, (0,0), img)


common_bbox = tmp.getbbox()
print(common_bbox)
tmp.crop(common_bbox).show()

for i in range(1,len(sys.argv)):
	img = Image.open(sys.argv[i])
	img = img.crop(common_bbox)
	print (img.size)
	print "Saving "+ sys.argv[i] +" ..."
	img.save(sys.argv[i])
	print "Done."
#happy = Image.open("Magician_Scene_WOMAN_SHOWHEAD_HAPPY.png")

#happy.paste(leg, (0,0), leg)

#happy.show()

#happy.getbbox()

#happy.crop(happy.getbbox()).show()

#happy.save('out.png')
