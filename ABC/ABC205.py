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
    ans = b/100*a
    print(ans)


def B():
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(a)
    b = [x+1 for x in range(n)]

    ans = True
    for i in range(n):
        if a[i]!=b[i]:
            ans = False
            break
    print("Yes" if ans else "No")


def C():
    a, b, c = map(int, input().split())
    if c==0:
        a = 1
        b = 1
    elif c%2==0:
        if a<0:
            a *= -1
        if b<0:
            b *= -1
    if a<b:
        print("<")
    elif a>b:
        print(">")
    else:
        print("=")


"""
二分探索?
うまく実装できない
"""
def D_WA_TLE():
    from bisect import bisect_left
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    set_a = set(a)

    for i in range(q):
        k = int(input())
        #kより小さな個数をカウント
        less_than_x_count = bisect_left(a, k)
        if less_than_x_count==n:
            less_than_x_count -= 1
        #カウントの分だけ追加で探索
        cnt = a[less_than_x_count] - less_than_x_count
        if a[less_than_x_count]==k:
            cnt -= 1
        j = a[less_than_x_count]
        while True:
            if cnt==k:
                ans = j-1
                break
            if j not in set_a:
                cnt += 1
            j += 1
        print(ans)


def D_ans():
    from bisect import bisect_left
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    #a[i]より前に幾つ数かあるかを計算
    c = [0]*n
    for i in range(n):
        c[i] = a[i]-i-1

    for i in range(q):
        k = int(input())
        r = bisect_left(c, k)
        ans = -1
        if r==0:
            ans = k
        else:
            ans = a[r-1] + (k - c[r-1])
        print(ans)
