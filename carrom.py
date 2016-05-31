def lineeq(coord,pcoord):
	lines=[]
	for i in coord:
		m=(pcoord[1]-i[1])/(pcoord[0]-i[0])
		c=pcoord[1]-m*pcoord[0]
		lines.append(m,c)
	return lines

def check(lines):
	for i in lines:
		if ():
			
