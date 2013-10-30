
a = [2,3,2,54,56,46,47,57,5,745,745,7457]
n = len(a)

# Finds a single peak in a list

def peak(a,n):
	if a[n/2] < a[n/2+1]:
		return peak(a[n/2:],n/4)
	else if a[n/2] < a[n/2 - 1]:
		return peak(a[:n/2],n/4)
	else:
		return a[n]
