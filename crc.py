def crc():
    data=list(map(int,input("Enter the data to be sent: ")))
    for i in data:
        if (i!=0 and i!=1):
            print("Wrong Data")
            return 0
    sizedata=len(data)
    generator=list(map(int,input("Enter the Generator: ")))
    for i in generator:
        if (i!=0 and i!=1):
            print("Wrong Generator")
            return 0
    sizegen=len(generator)
    if(sizegen>=sizedata):
        print("Generator should be smaller than Data")
        return(0)
#------------------------------------------------------
    for i in range(sizegen-1):
        data.append(0)
    remain=data[:sizegen-1]
    mul=1
    for j in range(sizedata):
        remain.append(data[sizegen+j-1])
        if(mul==1):
            for i in range(sizegen):
                remain[i]=remain[i]^generator[i]
        remain.pop(0)
        mul=remain[0]
    data=data[:-sizegen+1]+remain
    data=list(map(str, data))
    sep=""
    data=sep.join(data)
    print(data)

crc()
