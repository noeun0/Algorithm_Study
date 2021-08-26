import sys
sys.stdin = open("input.txt")

for tc in range(1,11):
    N = int(input())
    table = []
    count = 0
    for _ in range(N):
        table.append(list(map(int,input().split())))
        #1 은 N극 : 아래로 내려가야함
        #2 는 s극 : 위로 올라가야함
    for i in range(N):
        queue=[]

        for j in range(N):
            if table[j][i]==1 or table[j][i]==2:
                queue.append(table[j][i])

        for _ in range(len(queue)):
            if queue[0]==2:
                queue.pop(0)
            if queue[-1]==1:
                queue.pop(-1)
        print(queue)

        for i in range(len(queue)-1):
            if queue[i]!=queue[i+1] and queue[i]==1:
                count+=1
    print("#{} {}".format(tc, count))
