#needs generalisation

word='esc'
data='hi i am harini esc flag esc esc madhi'
data=data.split()
a=[]
for i in range(len(data)):
    if (word==data[i] or data[i]=='flag'):
        a.append(i)
for i in range(len(a)):
    data.insert(a[i]+i, word)
a=" "
data=a.join(data)
print(data)