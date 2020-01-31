a="11001111"
b=len(a)
c=int(0)
d=[]
for i in range(0,b+1):
    d.append(int(2**i)-1)
    if 2**i >= i+b+1:
        c=i
        break
e=[0]*int(c+b)
i,j=[0,0]
while(i<c+b):
    if i in d:
        i+=1
    else:
        e[i]=int(a[j])
        j+=1
        i+=1
#print(e)
d.pop()
e1,e2,e3=[0,0,0]
for i in range(len(d)):
    j=(2**(d.index(d[i])))
    e1=0
    g=int(0)
    f=e[d[i]:len(e)]
    e2=0
    while (e1<len(f)):
        e2%=2
        if e2==0:
            for l in range(e1,e1+j):
                if l<len(f):
#                    print(l,e1-j,f[l])
                    g+=f[l]
        e2+=1
        e1+=j
#    print(f,g,e)
    if g%2 == 1:
        e[d[i]]=1
h="".join(str(o) for o in e ) 
print(h)    







a="011010001111"
#print(a)
b=len(a)
c=int(0)
d=[]
e=[int(i) for i in a]
fin=[]
for i in range(0,b):
    if 2**i<=b:
        d.append(int(2**i)-1)
        c+=1
    else:
        break
for i in range(len(d)):
    j=(2**(d.index(d[i])))
    e1=0
    g=int(0)
    f=e[d[i]:len(e)]
    e2=0
    while (e1<len(f)):
        e2%=2
        if e2==0:
            for l in range(e1,e1+j):
                if l<len(f):
#                    print(l,e1-j,f[l])
                    g+=int(f[l])
        e2+=1
        e1+=j
#    print(f,g)
    if g%2 == 1:
        fin.append(int(1))
    else:
        fin.append(int(0))
print(fin)
res=int(0)
pow1=int(0)
for i in range(len(fin)):
    res+=fin[i]*(2**pow1)
    pow1+=1
print(res)
if res!=0:
    print("Error")
    if res%2==0:
        print("Can't find")
    else:
        if e[res-1]==0:
            e[res-1]=1
        else:
            e[res-1]=0
h="".join(str(o) for o in e )
print(h)    
