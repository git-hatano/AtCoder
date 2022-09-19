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
ans = True
ans = False
print("Yes" if ans else "No")
'''

def A():
    a, b = map(int, input().split())
    c = (a-b)/3 +b
    print(c)


def B():
    s = []
    for _ in range(4):
        s.append(input())
    s = set(s)

    if len(s)==4:
        ans = True
    else:
        ans = False
    print("Yes" if ans else "No") 


"""
もらうDP
"""
def C_ans1():
    s = input()
    mod = 10**9+7

    n = len(s)
    dp = [[0]*(9) for i in range(n+1)]
    dp[0][0] = 1

    t = "chokudai"
    for i in range(n):
        for j in range(9):
            dp[i+1][j] = (dp[i+1][j]+dp[i][j])%mod
            if j<8 and s[i]==t[j]:
                dp[i+1][j+1] = (dp[i+1][j+1]+dp[i][j])%mod

    print(dp[n][8])


"""
配るDP
"""
def C_ans2():
    s = input()
    mod = 10**9+7

    n = len(s)
    dp = [[0]*(9) for i in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1

    t = "chokudai"
    for i in range(n):
        for j in range(8): #8=len(t)
            if s[i]!=t[j]:
                dp[i+1][j+1] = dp[i][j+1]
            else:
                dp[i+1][j+1] = (dp[i][j+1] + dp[i][j])%mod
    print(dp[n][8])


# def D():

