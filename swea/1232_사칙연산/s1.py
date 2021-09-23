import sys
sys.stdin = open("input.txt")

def cal(n):
    if n<=N:
        if tree[n]=='-':
            return cal(tree_l[n][0])-cal(tree_l[n][1])
        elif tree[n]=='/':
            return cal(tree_l[n][0])//cal(tree_l[n][1])
        elif tree[n]=='*':
            return cal(tree_l[n][0])*cal(tree_l[n][1])
        elif tree[n]=='+':
            return cal(tree_l[n][0])+cal(tree_l[n][1])
        else:
            return int(tree[n])

for tc in range(1, 10+1):
    N= int(input())
    tree = [0 for i in range(N+1)]
    tree_l = [0 for i in range(N + 1)]
    for i in range(1,N+1):
        list_m =(input().split())
        tree[i]=list_m[1]
        tree_l[i]=[int(i) for i in list_m[2:]]
    result=0
    print("#{} {}".format(tc,cal(1)))

