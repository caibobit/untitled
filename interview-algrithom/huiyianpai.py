import sys

number = int(sys.stdin.readline().strip())

allproduct = []

for i in range(number):
    line = sys.stdin.readline().strip()
    allproduct.append(list(map(int,line.split())))

result = [0 for _ in range(number)]

for i in range(number):
    if result[i]:
        continue
    for j in range(number):
        if result[j]:
            continue
        if all([allproduct[i][k]>allproduct[j][k] for k in range(3)]):
            result[j]=1
        if all([allproduct[i][k]<allproduct[j][k] for k in range(3)]):
            result[i]=1
            break
print(sum(result))

# allproduct =[[7,8,9],[1, 4, 2], [4, 3, 2], [2, 5, 3],[5,4,3],[7,7,7]]
# number = 6