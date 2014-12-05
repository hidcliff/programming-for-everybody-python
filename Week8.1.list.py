fname = raw_input("Enter file name: ")
try:
	fh = open(fname)
except:
	print "The file can not be opened:", fname
	exit()

lst = list()
for line in fh:
	words = line.split()

	for word in words:
		if word in lst : continue
		lst.append(word)

lst.sort()
print lst