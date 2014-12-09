fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

try:
	fh = open(fname)
except:
	print "The file can not be opened:", fname
	exit()

counts = dict()
for line in fh:
	if not line.startswith("From "): continue
	word = line.split()
	counts[word[1]] = counts.get(word[1], 0) + 1
	
bigcount = None
bigword = None
for word,count in counts.items() :
	if bigcount is None or count > bigcount:
		bigword = word
		bigcount = count

print bigword, bigcount
