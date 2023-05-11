import os

'''
Atcoderのインデントは、スペース2

# 文字列を受け取る場合
S = input() 

# 1つの整数を入力
n = int(input())

# 複数の整数を入力
A, B = map(int, input().split())
A, B, C, D = map(int, input().split())

# listで入力を受け取り
a = list(map(int, input().split()))
'''

def test1():
    A, B, C, D = map(int, input().split())

    if A < C:
        print("Takahashi")
    elif A==C and B<=D:
        print("Takahashi")
    else:
        print("Aoki")

def test2():
    N = int(input())
    A = list(map(int, input().split()))
    

def C():
    # 動的計画法
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    dp = [False]*n
    ep = [False]*n

    dp[0] = True
    ep[0] = True

    for i in range(1, n):
        if dp[i-1]:
            if abs(a[i-1] - a[i])<=k:
                dp[i] = True
            if abs(a[i-1] - b[i])<=k:
                ep[i] = True
        
        if ep[i-1]:
            if abs(b[i-1] - a[i])<=k:
                dp[i] = True
            if abs(b[i-1] - b[i])<=k:
                ep[i] = True

    if dp[n-1] or ep[n-1]:
        print("Yes")
    else:
        print("No")


def C_TLE():
    n = int(input())
    xy = []
    for i in range(n):
        x, y = map(int, input().split())
        xy.append([x, y])

    s = input()
    can = False

    if s=="R"*n or s=="L"*n:
        can = False

    else:
        for i in range(n):
            for j in range(i+1, n):
                if xy[i][1] == xy[j][1]:

                    if xy[i][0] < xy[j][0] and s[i]=="R" and s[j]=="L":
                        can = True
                    if xy[i][0] > xy[j][0] and s[i]=="L" and s[j]=="R":
                        can = True

                    if can:
                        break
            if can:
                break

    if can:
        print("Yes")
    else:
        print("No")


def D_ans():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))
    b = [0]*(m+1)
    for i in reversed(range(m+1)):
        b[i] = c[i+n] // a[n]
        for j in range(n+1):
            c[i+j] -= b[i] * a[j]

    print(" ".join([str(x) for x in b]))
