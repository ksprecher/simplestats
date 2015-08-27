def mean(vals):
	total = sum(vals)
	length = len(vals)
	return total/length

def std(vals):
	n = len(vals)
	if n == 0:
		return 0.0
	mu = mean(vals)
	var = 0.0
	for val in vals:
		val = var + (val-mu)**2
	return (var/n)**0.5

# print mean([2,4])
