
import sys
sys.stdin = open('input.txt')


def btod(num):
    result = 0
    for j in range(len(num) - 1, -1, -1):
        if num[j] == '1':
            result += 2 ** (len(num) - 1 - j)
    return result


for tc in range(1,int(input())+1):
    num1 = list(input())
    num2 = list(input())
    numlist=[]


    for i in range(1,len(num1)):
        cnum = [i for i in num1]
        cnum[i] = str((int(num1[i])+1)%2)
        rnum = "".join(cnum)
        numlist.append(int(rnum,2))

    for i in range(0,len(num2)):
        for pl in range(1,3):
            cnum =[i for i in num2]
            cnum[i] = str((int(num2[i])+pl)%3)
            rnum = "".join(cnum)
            if int(rnum,3) in numlist:
                print("#{} {}".format(tc,int(rnum,3)))


    # int(2진수,2) 2진수를 10진수로 바꿔준다. 이때 2진수는 앞에 0b가 있어야 함... 아니면 문자열로 받아도됨!!
    # int('n진수', n) -> n 진수를 10진수로 바꿔준다!!!!