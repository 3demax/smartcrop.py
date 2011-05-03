#!/usr/bin/env python

import sys
import Image
from optparse import OptionParser
import os

parser = OptionParser(usage="Usage: " + sys.argv[0] + " [FILE ...]")
#parser.add_option("-d", "--output-directory", dest="directory",
#				 help="move files to directory after cropping", metavar="DIR")
(options, args) = parser.parse_args()
print(options)

if (len(args) < 1):
	parser.print_help()
	exit(1)

tmp = Image.open(args[0])

for ifile in args:
	img = Image.open(ifile)
	tmp.paste(img, (0,0), img)

#tmp.show()
tmp.save('out.png')
