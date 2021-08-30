import sys
sys.stdin = open("input.txt")

for tc in range(1,int(input())+1):
    list_t = []
    N = int(input())
    for _ in range(N):
        list_t.append(list(map(int,input().split())))

    list_count=[0]*(N+1)
    for i in range(N):
        count=0
        for j in range(N):
            if list_t[i][j]!=0:
                count+=1
            elif list_t[i][j]==0 and count!=0:
                list_count[count]+=1
                count=0
        if count!=0:
            list_count[count] += 1

    result= []
    for idx,x in enumerate(list_count):
        if x:
            result.append([x,idx])
    result.sort(key=lambda x:(x[0]*x[1],x[1]))
    print("#{} {}".format(tc,len(result)),end = " ")
    for i in result:
        for j in i:
            print(j,end=" ")

    print("")