import sys

allinput = []

while True:
    line = sys.stdin.readline().strip()
    if not line:
        break
    else:
        allinput.append(line)
# allinput=[
#     '1111111111',
#     '0000000000',
#     '0000111110',
#     '0000100000',
#     '0000101111',
#     '0000101111',
#     '0000101111',
#     '0111111111',
#     '0111111111',
#     '0111111111',
#     '5',
#     '4'
# ]
m = int(allinput[-1])
n = int(allinput[-2])
qipan = []
for i in range(10):
    tmp = list(map(int,allinput[i]))
    qipan.append(tmp)

isvisited=[[0]*10 for _ in range(10)]
result =0
def isvalid(i,j):
    if 0<=i<10 and 0<=j<10:
        return True
    else:
        return False
def issuccess(i,j):
    if i==0 or i==9 or j==0 or j==9:
        return True
def dfs(isvisited,m,n):
    global result
    if  result or not isvalid(m,n) or qipan[m][n]==1 or isvisited[m][n]: return
    isvisited[m][n]=1
    if issuccess(m,n):
        result = 1
    # print(result)
    dfs(isvisited,m-1,n)
    dfs(isvisited,m+1,n)
    dfs(isvisited,m,n-1)
    dfs(isvisited,m,n+1)

dfs(isvisited,m,n)

print (result)
