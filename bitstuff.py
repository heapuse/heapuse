flag='01111110'
data='011111011111011011111100'
count=0
a=[]
for i in range(len(data)-1):
    if( data[i]=='1' and data[i+1]=='1'):
        count+=1;
        if(count==4):
            a.append(i+2)
            count=0
    else:
        count=0
print(a)
for i in range(len(a)):
    data=data[:a[i]+i]+'0'+data[a[i]+i:]
print(data)