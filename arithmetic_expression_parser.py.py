e = lambda s: (s[-1],s[:-1]) if len(s) and s[-1].isnumeric() else (None,s) 
o = lambda s,c: (s[-1],s[:-1]) if len(s) and s[-1]==c else (None,s) 
def b(s):
    z = ""
    g=None
    while True:
        c,s = e(s)
        if c==None: break
        z=c+z
    if len(s) >= 2 and not (s[-2].isnumeric() or s[-2]==")"): g,s=o(s,"-")    
    return (("-"+z if g else z) if z else None,s)
def p(s):
    a,s=o(s,")")
    if a==None: return b(s)
    f,s=r(s)
    z,s=o(s,"(")   
    return (f,s)
def w(e,j,h,s):
    f,s=e(s)
    z,s=o(s,h)
    if z==None: return (f,s)
    a,s=w(e,j,h,s)
    if not a: return (f,s)
    else: return (j(int(a),int(f)),s)
q = lambda e,j,h: lambda s: w(e,j,h,s)
u=q(p,lambda x,y:x*y,"*")
y=q(u,lambda x,y:x//y,"/")
t=q(y,lambda x,y:x-y,"-")
r=q(t,lambda x,y:x+y,"+")
print(r(input()))
