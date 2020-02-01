from math import log, ceil, floor
def encode(n):
    k=len(n)
    for r in range(ceil(log(k,2)+3)):
        if(2**r>=k+r+1):
            break
        j=2**r-1
        n=n[:j]+'x'+n[j:]
    k=len(n)
    for i in range(r):
        j=2**i-1
        count=0
        while(j<k):
            for l in range(2**i):
                if(j+l<k):
                    if(not(n[j+l]=='x')):
                        count=(count+int(n[j+l]))%2
            j=j+2**(i+1)
        l=2**i-1
        n=n[:l]+str(count)+n[l+1:]
    return n

def decode(n):
    k=len(n)
    r=floor(log(k,2)+1)
    a=[]
    for i in range(r):
        j=2**i-1
        count=0
        while(j<k):
            for l in range(2**i):
                if(j+l<k):
                    print(i, j, l, k)
                    count=(count+int(n[j+l]))%2
            j=j+2**(i+1)
        a.append(count)
    if(sum(a)==0):
        for i in range(r):
            l=2**(i)-i-1
            n=n[:l]+n[l+1:]
    b=[n,a]
    return b
n=input()
h=encode(n)
k=decode(h)
