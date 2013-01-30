from string import *
import re, sys, os
i = 1

inp = []
for line in sys.stdin:
	inp.append(line)
t = int(inp[0])
while (t) :
	
	input_str = inp[i]
	input_list = list(input_str)
	
	c1 = 0
	cl = 0
	op = 0
	j = 0
	prev = ""
	#i(:()()
	#(:())
	for c in input_list:
		if c == ")" and prev == ":":
			if c1 > 0:
				cl += 1
		elif c == "(" and prev == ":":
			op += 1
		elif c == "(":
			c1 += 1
		elif c == ")":
			if c1 > 0:
				c1 -= 1
			elif op > 0:
				op -= 1
			else:
				c1 -= 1
		if c1 == 0:
			cl = 0;
		#elif c1 < 0:
		#	if op > 0:
		#		op -= 1;
		if c1 < 0 and op == 0:
			break;
		j += 1
		prev = c
	
	while(c1 > 0 and cl > 0):
		c1 -= 1
		cl -= 1
	
	while(c1 < 0 and op > 0):
		c1 += 1
		op -= 1
	input_str = "".join(input_list)
	
	if c1 != 0:
		msg = "NO"
	else:
		msg = "YES"
	print "Case #"+str(i)+ ": "+msg

	t -= 1
	i += 1
