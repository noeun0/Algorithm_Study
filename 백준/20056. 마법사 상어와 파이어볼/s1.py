import sys
sys.stdin = open("input.txt")

N,M,K = map(int,input().split())

ball = [[i for i in map(int,input().split())] for i in range(M)]
print(ball)


