list1 = []

for case in range(int(input())):
    list1.append(input())

list1 = list(set(list1))

result = sorted(list1)
result = sorted(result, key=lambda x: len(x))

for i in result:
    print(i)
