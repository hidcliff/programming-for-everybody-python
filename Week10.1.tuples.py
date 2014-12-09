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
	posColon = line.find(":")
	if posColon > -1:
		hour = line[posColon-2:posColon]
		counts[hour] = counts.get(hour, 0) + 1

lst = list()
for (key,val) in counts.items():
	lst.append((key, val))

lst.sort()

for (key,val) in lst:
	print key, val