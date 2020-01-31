def get_checksum(data,divisor):
    quotient = []
    curr = data[:len(divisor)]
    n = len(divisor)
    for i in range(n,len(data)+1):
        if curr[0] == 0:
            subtr = [0]*n
            quotient.append(0)
        else: 
            subtr = [j for j in divisor]
            quotient.append(1)
        curr = [curr[j]^subtr[j] for j in range(n)]
        if i == len(data):
            curr = curr[1:]
        else:
            curr = curr[1:] + [data[i]]
    return curr


choice = int(input("1.Send\n2.Check error\n"))
if choice == 1:
    data = [ord(i)-48 for i in input("Enter input to send : ")]
    divisor = [ord(i)-48 for i in input("Enter divisor : ")]
    data = data + [0]*(len(divisor)-1)
    n = len(divisor)
    data = data[:-4] + get_checksum(data,divisor)
    ret = ''
    for i in data:
        ret += str(i)
    print(ret)
    
else:
    data = [ord(i)-48 for i in input("Enter input to check : ")]
    divisor = [ord(i)-48 for i in input("Enter divisor : ")]
    if get_checksum(data,divisor) == [0]*4 :
        print('Data Correct ')
    else: 
        print('Data Incorrect')
