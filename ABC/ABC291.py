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
ans = True #ans = False
print("Yes" if ans else "No")

# リストの中身を文字列に
ans = " ".join([str(x) for x in a])
'''

def A():
    s = input()
    n = len(s)
    for i in range(n):
        if s[i].isupper():
            print(i+1)
            break


def B():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = sum(a[n:-n]) / (3*n)
    print(ans)


def C():
    n = int(input())
    s = input()
    d = {"R":[0,1], "L":[0,-1], "U":[-1,0], "D":[1,0]}
    visit = set()
    cur = [0, 0]
    visit.add((cur[0], cur[1]))
    ans = False
    for i in range(n):
        cur[0] += d[s[i]][0]
        cur[1] += d[s[i]][1]
        nex = (cur[0], cur[1])
        if nex in visit:
            ans = True
        visit.add(nex)
    print("Yes" if ans else "No")


"""
dp[i][j]
i番目までのカードを並べて条件を満たす方法のうち、
最後のカードが j=(表0/裏1) になる場合の数
"""
def D_ans():
    mod = 998244353
    n = int(input())
    a = [None]*n
    b = [None]*n
    for i in range(n):
        a[i], b[i] = map(int, input().split())

    dp = [[0]*2 for i in range(n)]
    dp[0] = [1, 1]
    for i in range(1, n):
        #表の更新
        if a[i]!=a[i-1]:
            dp[i][0] += dp[i-1][0]
        if a[i]!=b[i-1]:
            dp[i][0] += dp[i-1][1]
        #裏の更新
        if b[i]!=a[i-1]:
            dp[i][1] += dp[i-1][0]
        if b[i]!=b[i-1]:
            dp[i][1] += dp[i-1][1]
        
        dp[i][0] %= mod
        dp[i][1] %= mod

    ans = sum(dp[n-1])%mod
    print(ans)
