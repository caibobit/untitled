# coding=utf-8
def move(m, n, k):
    """
    m: m行
    n：n列
    k：位数之和k
    :param m:
    :param n:
    :param k:
    :return:所有的可能
    """

    def isvalid(x, y):
        if x >= 0 and x < m and y >= 0 and y < n:
            return True
        else:
            return False

    def isvalid_sum(x, y):
        return (sum([int(i) for i in x]) + sum([int(i) for i in y])) <= k

    # print (isvalid_sum('45','21'))
    isvisited = [[False for _ in range(n)] for _ in range(m)]
    # isvisited[0][0] = True
    # print (isvisited)
    global count
    count = 0
    def dfs(x, y, isvisited):
        global count
        if isvalid(x, y) and isvalid_sum(str(x), str(y)) and not isvisited[x][y]:
            isvisited[x][y] = True
            count += 1
            dfs(x - 1, y , isvisited)
            dfs(x + 1, y , isvisited)
            dfs(x , y - 1, isvisited)
            dfs(x , y + 1, isvisited)
        else:
            return

    start = 0
    end = 0
    dfs(start, end, isvisited)
    return count


if __name__ == "__main__":
    print(move(10, 10, 5))
