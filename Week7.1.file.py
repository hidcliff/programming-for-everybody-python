# Use words.txt as the file name
fname = raw_input("Enter file name: ")
try:
	fh = open(fname)
except:
	print "The file can not be opened:", fname
	exit()

for line in fh :
	line = line.rstrip().upper()
	print line