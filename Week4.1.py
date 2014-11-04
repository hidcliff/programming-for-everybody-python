def computepay(h,r):
	if h <= 40:
		p = h * r
	else :
		p = 40 * r + ((h - 40) * (r * 1.5))
	return p

try:
	hrs = raw_input("Enter Hours:")
	hrs = float(hrs)
	rates = raw_input("Enter Rates:")
	rates = float(rates)
except:
	print "Error, Please enter numeric input."
	quit()

p = computepay(hrs,rates)
print p