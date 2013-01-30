
import  sys,  time
record = 1

inp = []
for line in sys.stdin:
	inp.append(line)
t = int(inp[0])
case = 1
def func_next(li, el):
	while li[el] > 0:
		el += 1
	return el
while (t) :
	n, k = map(int, inp[record].split(" "))
	a, b, c, r = map(int, inp[record+1].split(" "))
	m = [0] * ((2*k)+1)
	m[0] = a
	l = [0] * (k+1)
	if m[0] < k+1:
		l[m[0]] += 1
	for i in xrange(1, k):
		num = (b * m[i-1] + c) % r
		#num = test[i-1]
		m[i] = num
		if num < k+1:
			l[num] += 1
	
	el = func_next(l, 0)
	for i in xrange(1, k+2):
		og = m[i-1]
		m[k+i-1] = el
		l[el] += 1
		if og < k+1:
			l[og] -= 1
		if i < k+1:
			if og <= el and l[og] < 1:
				el = og
			else:
				el = func_next(l, el+1)
	print "Case #" + str(case) + ": " + str(m[k + (n - k - 1) % (k + 1)])
	case += 1
	t -= 1
	record += 2

