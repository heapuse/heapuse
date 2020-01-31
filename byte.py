import re

def bytestuff(data):
    esc,flag = '10100011','01111110'
    arr = [data[i:i+8] for i in range(0,len(data),8)]
    data = ''
    for i in arr:
        if i in [esc,flag]:
            data += esc
        data += i
    return data 

def bitstuff(data):
    idx = [i.start() for i in re.finditer('11111',data)]
    idx = [idx[i]+i for i in range(len(idx))]
    for i in idx:
        data = data[0:i+5] + '0' + data[i+5:]
    return data
        
def unbitstuff(data):
    idx = [i.start() for i in re.finditer('11111',data)]
    idx = [idx[i]-i for i in range(len(idx))]
    for i in idx:
        data = data[0:i+5] + data[i+6:]
    return data

def unbytestuff(data):
    esc,flag = '10100011','01111110'
    arr = [data[i:i+8] for i in range(0,len(data),8)]
    data,i = '',0
    while(True):
        print(arr[i])
        if arr[i] == esc:
            data += arr[i+1]
            i+=1
        else:
            data += arr[i]
        i+=1
        if i == len(arr):
            break
    return  data
