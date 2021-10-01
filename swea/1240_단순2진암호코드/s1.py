import sys
sys.stdin = open("input.txt")

dict1={'0001101':0,'0011001':1,'0010011':2,'0111101':3,'0100011':4,'0110001':5,
       '0101111':6,'0111011':7,'0110111':8,'0001011':9}

for tc in range(1,int(input())+1):
    code=""
    N,M = map(int,input().split())
    for _ in range(N):
        chr = input()
        if '1' in chr:
            code=chr.rstrip('0')
    code = code[-56:]
    num=""
    sum1=0
    for i in range(0,len(code),7):
        num+=str(dict1[code[i:i+7]])
    result=0
    for i in range(len(num)-1):
        sum1+=int(num[i])
        if i%2==0:
            result += int(num[i])*3
        else:
            result += int(num[i])
    sum1+=int(num[-1])
    result+=int(num[-1])
    if result%10==0:
        print("#{} {}".format(tc, sum1))
    else:
        print("#{} 0".format(tc))