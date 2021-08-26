import sys
sys.stdin = open("input.txt")

for tc in range(1,int(input())+1):
    N,M = map(int,input().split()) # N 화덕크기 M 피자 갯수
    pizza = list(map(int,input().split()))
    queue=[ [idx, i] for idx, i in enumerate(pizza[:N],start=1)]
    waiting=[ [idx, i] for idx, i in enumerate(pizza[N:],start=N+1)]

    while len(queue)!=1:

        if queue[0][1]//2 ==0:
            queue.pop(0)
            if waiting:
                queue.append(waiting.pop(0))
        else:
            queue[0][1]=queue[0][1]//2
            queue.append(queue.pop(0))
    print("#{} {}".format(tc,queue[0][0]))