try:
	input = raw_input("Enter Your Score:")
	score = float(input)
except:
	print "Error, Please enter numeric input."
	quit()

if score >= 1.0 or score < 0.0:
	print "Error, please enter numeric input between 0.0 and 1.0"
elif score >= 0.9:
	print  "A"
elif score >= 0.8:
	print  "B"
elif score >= 0.7:
	print  "C"
elif score >= 0.6:
	print "D"
else:
	print "F"
