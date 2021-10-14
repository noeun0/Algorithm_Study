N,M = map(int,input().split())
print(N,M)
# 123456
# 123456
# 123456


def func(x,arr):
    if len(arr) == N:
        print(" ".join([str(i) for i in arr]))
        return

    for i in range(1,7):
        arr.append(i)
        func(x+1,arr)
        arr.remove(i)


def func2(x,arr):
    if len(arr) == N:
        if arr not in used:
            print(used)
            used.append(arr)
            print(" ".join([str(i) for i in arr]))
        return


    for i in range(1,7):
        arr.append(i)
        func2(x+1,arr)
        arr.remove(i)

def func3(x,arr): # 1 ,[]

    if len(arr)==N:
        print(" ".join([str(i) for i in arr]))
        return

    for i in range(1,7):
        if i not in used:
            arr.append(i)
            used.append(i)
            func3(x+1,arr)
            arr.remove(i)
            used.remove(i)




if M == 1:
    arr =[]
    func(1,arr)


elif M == 2:
    arr = []
    used = []
    func2(1,arr)

elif M == 3:
    arr = []
    used = []
    func3(1,arr)