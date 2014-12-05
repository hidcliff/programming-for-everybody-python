# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
try:
	fh = open(fname)
except:
	print "The file can not be opened:", fname
	exit()

count = 0
avg = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue

    count = count + 1
    avg = avg + float(line[line.find(":")+1:].strip())
    
print "Average spam confidence:", avg / count