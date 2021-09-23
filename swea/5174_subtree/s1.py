import sys
sys.stdin = open("input.txt")

def func1(n):
    global count
    if list_c[n]:
        for i in list_c[n]:
            count += 1
            func1(i)



for tc in range(1, int(input())+1):
    E,N = map(int,input().split())
    list_n=list(map(int,input().split()))
    n=max(list_n)
    list_c=[[] for i in range(n+1)]
    for num in range(0,E*2,2):
        list_c[list_n[num]].append(list_n[num+1])
    count=1

    func1(N)
    print("#{} {}".format(tc,count))

