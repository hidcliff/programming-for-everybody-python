fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

try:
	fh = open(fname)
except:
	print "The file can not be opened:", fname
	exit()

lst = list()
for line in fh:
	if not line.startswith("From "): continue
	word = line.split()
	lst.append(word[1])
	print word[1]

print "There were", len(lst), "lines in the file with From as the first word"