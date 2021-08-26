import sys
sys.stdin = open("input.txt")

for tc in range(1,int(input())+1):
    A,B = map(int,input().split())
    queue = list(map(int,input().split()))
    for _ in range(B):
        queue.append(queue.pop(0))

    print("#{} {}".format(tc,queue[0]))