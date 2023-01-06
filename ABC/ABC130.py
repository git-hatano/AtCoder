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
    x, a = map(int, input().split())
    if x<a:
        print(0)
    else:
        print(10)


def B():
    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    d = 0
    ans = 1
    for i in range(1, n+1):
        if d+l[i-1]<=x:
            ans += 1
        d = d + l[i-1]
    print(ans)


"""
割り算, 小数は信用できない
WA: w//2==x and h//2==x
AC: 2*x==w and 2*y==h
"""
def C():
    w, h, x, y = map(int, input().split())
    num = 0
    s = w*h/2
    if 2*x==w and 2*y==h:
        num = 1
    print(s, num)


def D_TLE():
    from itertools import accumulate
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0] + list(accumulate(a))

    ans = 0
    for i in range(n+1):
        for j in range(i+1, n+1):
            if s[j]-s[i]>=k:
                ans += 1
    print(ans)


"""
しゃくとり方もどき
"""
def D():
    from itertools import accumulate
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    #累積和
    s = [0] + list(accumulate(a))
    #スタート地点を管理
    r = [-1]*(n+1)
    ans = 0
    for i in range(n+1):
        #スタート地点を決める
        if i==0:
            r[i] = 0
        else:
            r[i] = r[i-1]
        #既に右端まで到達していたら終了
        if r[i]==n:
            break
        #スタートから合計がk未満のとこまで進む、k以上になったらそれ以降はずっとk以上
        while True:
            if r[i]<n and s[r[i]+1]-s[i]<k:
                r[i] += 1
            elif r[i]<n and s[r[i]+1]-s[i]>=k:
                ans += n - r[i]
                break
            else:
                break
    print(ans)
