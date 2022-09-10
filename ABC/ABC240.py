'''
# 文字列を受け取る場合
S = input() 

# 1つの整数を入力
n = int(input())

# 複数の整数を入力
A, B = map(int, input().split())

# listで入力を受け取り
a = list(map(int, input().split()))

# 文字列の反転
rev_S = S[::-1]

# 2次元配列
dp = [[0]*(K) for i in range(N)]
'''

'''
安易に全bit探索しない
2**10は流石に無理
'''
def C_TLE():
    n, x= map(int, input().split())
    A = []
    B = []

    for i in range(n):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    ans = False
    for bit in range(1 << n):
        combination = [] 
        for i in range(n):
            shift_i = 1 << i

            if bit & shift_i > 0:
                combination.append(A[i])
            else:
                combination.append(B[i])
        
        if x==sum(combination):
            ans = True
            break

    if ans:
        print("Yes")
    else:
        print("No")


def C_WA():
    n, x= map(int, input().split())
    A = []
    B = []

    for i in range(n):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    big = []
    little = []
    diff = []

    for i in range(n):
        if A[i] > B[i]:
            big.append(A[i])
            little.append(B[i])
            diff.append(A[i]-B[i])
        else:
            big.append(B[i])
            little.append(A[i])
            diff.append(B[i]-A[i])

    diff = sorted(diff)
    ans = False
    if x <= sum(big):
        diff_x = x-sum(little)
        diff_sum = 0

        for i in range(n):
            if diff_sum == diff_x:
                ans = True
                break
            elif diff_sum > diff_x:
                break
            diff_sum += diff[i]
        
    if ans:
        print("Yes")
    else:
        print("No")


"""
dpの基本的な問題
全探索でTLE時はdp?
"""
def C():
    n, x = map(int, input().split())

    a = []
    b = []
    for i in range(n):
        tmp_a, tmp_b = map(int, input().split())
        a.append(tmp_a)
        b.append(tmp_b)

    dp = [[0]*(x+101) for i in range(n+1)]
    dp[0][0] = True

    for i in range(n):
        for j in range(x+1):
            if dp[i][j]:
                dp[i+1][j+a[i]] = True
                dp[i+1][j+b[i]] = True

    if dp[n][x]:
        print("Yes")
    else:
        print("No")


def A():
    a, b = map(int, input().split())
    ans = False

    if abs(a-b)==1:
        ans = True
    elif (a==1 and b==10) or (a==10 and b==1):
        ans = True

    if ans:
        print("Yes")
    else:
        print("No")


def B():
    n = int(input())
    a = list(map(int, input().split()))

    a = list(set(a))
    print(len(a))


def D():
    n = int(input())
    a = list(map(int, input().split()))

    buf = []
    num = []

    for i in range(n):
        buf.append(a[i])
        
        if len(num)==0:
            num.append([a[i], 1])

        elif num[-1][0]==a[i]:
            num[-1][1] += 1
        
        else:
            num.append([a[i], 1])

        if num[-1][1]==a[i]:
            del buf[-a[i]:]
            del num[-1:]

        print(len(buf))


