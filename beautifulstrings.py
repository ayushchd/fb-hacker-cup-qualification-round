import sys
i = 1

inp = []
for line in sys.stdin:
	inp.append(line)
t = int(inp[0])
while (t) :
	
	p = [0] * 26
	d = 0
	s = inp[i].lower()
	for c in s:
		asc = ord(c)
		if asc >= 97 and asc <= 122:
			p[asc-97] += 1
	l = sorted(list(p), reverse=True)
	m = 26
	beauty = 0
	for c in l:
		beauty += m*c
		m -= 1
	print "Case #"+str(i)+ ": "+str(beauty)

	t -= 1
	i += 1
