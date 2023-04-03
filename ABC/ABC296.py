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
    n = int(input())
    s = input()
    ans = True
    for i in range(n-1):
        if s[i]==s[i+1]:
            ans = False
    print("Yes" if ans else "No")


def B():
    s = []
    for i in range(8):
        s.append(list(input()))

    for i in range(8):
        for j in range(8):
            if s[i][j]=="*":
                ans = f"{chr(97+j)}{8-i}"
    print(ans)


def C():
    from collections import Counter
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    counter = Counter(a)
    ans = False
    for i in range(n):
        k = a[i]+x 
        if k in counter:
            ans = True
    print("Yes" if ans else "No")


def D_WA():
    import math
    n, m = map(int, input().split())
    ans = -1
    for i in range(1, 10**6+1):
        if m%i==0:
            j = m//i
        else:
            j = math.ceil(m/i)
        x = i*j
        if 1<=i<=n and 1<=j<=n and x>=m:
            ans = x
            break
    print(ans)


def D():
    import math
    n, m = map(int, input().split())
    inf = 10**18
    ans = inf
    for i in range(1, 10**6+1):
        if m%i==0:
            j = m//i
        else:
            j = math.ceil(m/i)
        x = i*j
        if 1<=i<=n and 1<=j<=n and x>=m:
            ans = min(ans, x)###ここがキーポイントだった
    if ans==inf:
        ans = -1
    print(ans)



