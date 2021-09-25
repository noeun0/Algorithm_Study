import sys
sys.stdin = open("input.txt")

def pay(month,result):
    global min
    if month<=11:
        if result<y:
            pay(month + 1, result + plan[month] * d)
            pay(month + 1, result + m)
            pay(month + 3, result + tm)
    elif min>result:
        min=result

for tc in range(1,int(input())+1):
    d, m, tm, y = map(int,input().split())
    plan=[i for i in map(int,input().split())]
    result=0
    min=y
    pay(0,0)
    print("#{} {}".format(tc,min))