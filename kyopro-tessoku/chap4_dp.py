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

def A16():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    dp = [0]*n
    dp[0] = 0
    for i in range(1, n):
        if i==1:
            dp[i] = dp[i-1]+a[i-1]
        else:
            dp[i] = min(dp[i-1]+a[i-1], dp[i-2]+b[i-2])
    print(dp[n-1])


def B16():
    n = int(input())
    h = list(map(int, input().split()))

    dp = [0]*n
    dp[0] = 0
    for i in range(1, n):
        if i==1:
            dp[i] = dp[i-1]+abs(h[i]-h[i-1])
        else:
            dp[i] = min(dp[i-1]+abs(h[i]-h[i-1]), dp[i-2]+abs(h[i]-h[i-2]))
    print(dp[n-1])


# def C():



# def D():

