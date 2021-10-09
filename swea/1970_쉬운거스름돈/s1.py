import sys
sys.stdin = open("input.txt")



for tc in range(1,int(input())+1):

    money = int(input())

    units = [50000,10000,5000,1000,500,100,50,10]
    result= [0,0,0,0,0,0,0,0]
    for i in range(len(units)):
        while money>=units[i]:

            money-=units[i]
            result[i]+=1
    print("#{}".format(tc))
    print(' '.join([str(i) for i in result]))