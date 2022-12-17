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
    a = list(map(int, input().split()))
    a.sort()
    ans = sum(a[:2])
    print(ans)


def B():
    n = int(input())
    w = list(map(int, input().split()))
    sumw = sum(w)
    ans = 10**9
    s1 = 0
    s2 = sumw
    for i in range(n):
        s1 += w[i]
        s2 -= w[i]
        ans = min(ans, abs(s1-s2))
    print(ans)


def C():
    n, m = map(int, input().split())
    a = []
    for i in range(m):
        a.append(int(input()))
    mod = 10**9+7

    dp = [0]*(n+1)
    dp[0] = 1
    for i in range(m):
        dp[a[i]] = -1
    for i in range(n):
        if dp[i]>=0:
            if i+1<=n and dp[i+1]>=0:
                dp[i+1] += dp[i]%mod
            if i+2<=n and dp[i+2]>=0:
                dp[i+2] += dp[i]%mod
    print(dp[n]%mod)


# def D():

