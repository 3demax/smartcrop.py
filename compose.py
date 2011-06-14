#!/usr/bin/env python

import sys
import Image
from optparse import OptionParser
import os

parser = OptionParser(usage="Usage: " + sys.argv[0] + " [FILE ...] [-o OUTFILE]")
parser.add_option("-o", "--output", dest="output",
				 help="output file name", metavar="OUTFILE")
(options, args) = parser.parse_args()
#print(options)

if (len(args) < 1):
	parser.print_help()
	exit(1)

tmp = Image.open(args[0])

for ifile in args:
	img = Image.open(ifile)
	tmp.paste(img, (0,0), img)

#tmp.show()
if (options.output == None):
	outfile = "out.png"
	i = 1;
	while ( os.path.exists(outfile) ):
		i += 1
		outfile = "out" + str(i) + ".png"
	outfile = "out" + str(i) + ".png"
	print ("writing result to " + outfile)
else:
	outfile = options.output
	
tmp.save(outfile)
