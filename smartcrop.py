#!/usr/bin/env python

import sys
import Image
from optparse import OptionParser
import os
import shutil

parser = OptionParser(usage="Usage: smartcrop.py FILE FILE [FILE ...] [-d DIR]")
parser.add_option("-d", "--output-directory", dest="directory",
				 help="move files to directory after cropping", metavar="DIR")
(options, args) = parser.parse_args()
print(options)

if (len(args) < 1):
	parser.print_help()
	exit(1)

tmp = Image.open(args[0])

for ifile in args:
	img = Image.open(ifile)
	tmp.paste(img, (0,0), img)


common_bbox = tmp.getbbox()
print("info: common bounding box is " + str(common_bbox))
print("info: frame width " +str(common_bbox[2]-common_bbox[0]) + " height " + str(common_bbox[3]-common_bbox[1])) 
#tmp.crop(common_bbox).show()

if (options.directory == None ):
	print ("warning: no output directory chosen.")
	dirname = "."
else:
	dirname = options.directory#+"("+str(common_bbox[0])+","+str(common_bbox[1])+")"
if (not os.path.exists(dirname)):
	os.mkdir(dirname)

#create desciption file
	info_file = open(dirname+'/'+'info.txt', 'w')
	info_file.write("common bounding box is " + str(common_bbox)+'\n\n')
	info_file.write("left: " + str(common_bbox[0]) + "px; top: " + str(common_bbox[1]) + "px;\n")
	info_file.write("width: " + str(common_bbox[2]-common_bbox[0]) + "px; height: " + str(common_bbox[3]-common_bbox[1])+"px;\n")

for ofile in args:
	img = Image.open(ofile)
	img = img.crop(common_bbox)
	img.save(ofile)
	print (os.path.basename(ofile))
	shutil.move(ofile, dirname + "/" + os.path.basename(ofile))
	print ( str(dirname) + "/" + str(ofile) + " saved.")
exit(0)


