import os

'''
A, B = map(int, input().split())

n = int(input())
a = list(map(int, input().split()))
'''

def test1():
    A, B, C, X = map(int, input().split())

    if 0 < X and X <= A:
        print(1)
    elif A+1 <= X and X <= B:
        print(C/(B-A))
    else:
        print(0)

def test2():
    # 文字列を受け取る場合
    S = input() 
    str_list = sorted(S)
    print("".join(str_list))

def test3():
    N = int(input())

    list_x = []
    for X in range(10**(N-1), 10**N):
        if "0" not in str(X):
            for n in range(len(str(X)) -1):
                x_i = int(str(X)[n])
                x_i1 = int(str(X)[n+1])

                if abs(x_i - x_i1) >1:
                    break
                
                if n == len(str(X))-2:
                    list_x.append(X)
            
    print(len(list_x)%998244353)


def trans(x):
    if x==1:
        return range(x, x+2)
    elif x==9:
        return range(x-1, x+1)
    else:
        return range(x-1, x+2)


'''
ゴリ押し全探索ver
'''
def C_TLE():
    n = int(input())
    start = 10**(n-1)
    stop = 10**n
    cnt = 0

    for i in range(start, stop):
        tmp = i
        for j in range(n):
            x = tmp//(10**(n-j-1))

            if j==0:
                old_x = x
                tmp -= old_x*(10**(n-j-1))
            else:
                if x!=0 and abs(x-old_x)<=1:
                    old_x = x
                    tmp -= old_x*(10**(n-j-1))
                else:
                    break
            
            if j==(n-1):
                cnt += 1
                cnt %= 998244353

    print(cnt)


mod = 998244353
def add(x, y):
    x += y
    x %= mod
    return x

n = int(input())
dp = [[0]*10 for i in range(1000005)]

for d in range(1, 10):
    dp[1][d] = 1

for i in range(2, n+1):
    for d in range(1, 10):
        if d-1>=1:
            dp[i][d] = add(dp[i][d], dp[i-1][d-1])
        dp[i][d] = add(dp[i][d], dp[i-1][d])
        if d+1<=9:
            dp[i][d] = add(dp[i][d], dp[i-1][d+1])

ans = 0
for d in range(1, 10):
    ans = add(ans, dp[n][d])

print(ans)
