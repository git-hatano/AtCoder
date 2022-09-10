'''
# 文字列を受け取る場合
s = input() 

# 1つの整数を入力
n = int(input())

# 複数の整数を入力
a, b = map(int, input().split())

# listで入力を受け取り
a = list(map(int, input().split()))

# Yes/Noテンプレ
if ans:
    print("Yes")
else:
    print("No")
'''


def A():
    x, y = map(int, input().split())
    diff = y-x
    ans = 0

    if diff > 0:
        ans = diff//10

        if diff%10 > 0:
            ans += 1  

    print(ans)


def B():
    l, r = map(int, input().split())
    s = input()

    l -= 1
    r -= 1

    ans = s[:l] + s[l:r+1][::-1] + s[r+1:]
    print(ans)


def C():
    """
    深さ優先探索
    """
    class DFS:
        def __init__(self):
            self.ans = 0
        
        def dfs(self, i, s):
            if i==n:
                if s==x:
                    self.ans += 1
                return 
            
            for j in range(len(a[i])):
                self.dfs(i+1, s*a[i][j]) 


    # input
    n, x = map(int, input().split())
    a = []
    # l = []
    for i in range(n):
        buf = list(map(int, input().split()))
        # l.append(buf[0])
        a.append(buf[1:])

    # dfs
    dfs = DFS()
    dfs.dfs(0, 1)
    print(dfs.ans)


def D_TLE():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    ans = 0

    for i in range(n):
        for j in range(i, n):
            if sum(a[i:j+1]) == k:
                # print(i, j)
                ans += 1

    print(ans)


def D_TLE2():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    # 累積和
    a_sum =[]
    for i in range(n):
        if i==0:
            a_sum.append(a[i])
        else:
            a_sum.append(a_sum[i-1]+a[i])

    import numpy as np
    a_sum = np.array(a_sum)

    ans = 0
    for i in range(n):
        if i > 0:
            a_sum -= a[i-1]
            a_sum = np.delete(a_sum, 0)

        ans += np.sum(a_sum==k)

    print(ans)


def D():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    s = [0]*(n+1)
    for i in range(n):
        s[i+1] = s[i]+a[i]

    # 連想配列
    from collections import defaultdict
    x = defaultdict(int)

    ans = 0

    for i in range(1, n+1):
        x[s[i-1]] += 1
        # print(i-1, s[i-1])

        ans += x[s[i]-k]
        # print(i, s[i])
        # print(i, s[i]-k)

        # print("---------------")

    print(ans)


