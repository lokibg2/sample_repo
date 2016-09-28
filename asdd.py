def check(j,k):
    for x in k:
        if j[1]==x[1]:
            if j[0]+x[0] > 0:
                return (j[0]+x[0],x[1])
            else:
                return False
    else:
        return (j)
def addpoly(m,n):
        l=list(filter(lambda u: u != False,map(lambda x:check(x,n),m)))
        q=list(filter(lambda u: u != False,map(lambda x:check(x,m),n)))
        r=l
        for j in q:
            if j not in r:
                r.append(j)
        return (sorted(r,key=lambda x:x[1],reverse=True))
def mul(h,i):
    l=[]
    for x in i:
        l.append((x[0]*h[0],x[1]+h[1]))
    return(l)
def multpoly(m,n):
	t=[]
	l=[]
	for u in m:
		l=mul(u,n)
		t=addpoly(t,l)
	print(t)	
multpoly([(1,1),(-1,0)],[(1,2),(1,1),(1,0)])


        