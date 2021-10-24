import sys
sys.stdin = open('input.txt')


for tc in range(1,int(input())+1):

    N = int(input())
    board = [[i for i in map(int,input().split())] for _ in range(N)]
    listc = []
    for task in board:

        if len(task)>=3:
            listc.append(task[2:])
        else:
            listc.append([0])
    print(listc)