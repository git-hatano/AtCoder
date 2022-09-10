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
print("Yes" if ans else "No")
'''

def A():
    a, b, c = map(int, input().split())
    n = 1000

    ans = -1
    for i in range(1, n+1):
        if a<=c*i and c*i<=b:
            ans = c*i
            break
    print(ans)


def B():
    k = int(input())
    a, b = input().split()

    a = int(a, k)
    b = int(b, k)
    print(a*b)


def C():
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())

    ans = (x//sum(a))*n
    x %= sum(a)

    from itertools import accumulate
    s = [0] + list(accumulate(a))

    for i in range(n+1):
        if s[i]>x:
            ans += i
            break
        
    print(ans)


def D():
    n = int(input())
    a = list(map(int, input().split()))
    m = 998244353

    dp = [[0]*10 for i in range(n)]
    dp[0][a[0]] = 1

    for i in range(n-1):
        for j in range(10):
            if dp[i][j]>0:
                #F
                dp[i+1][(j+a[i+1])%10] += dp[i][j]
                dp[i+1][(j+a[i+1])%10] %= m
                #G
                dp[i+1][(j*a[i+1])%10] += dp[i][j]
                dp[i+1][(j*a[i+1])%10] %= m

    for j in range(10):
        print(dp[n-1][j])

