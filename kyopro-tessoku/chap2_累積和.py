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

"""
累積和
"""
def A06():
    from itertools import accumulate
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    s = [0] + list(accumulate(a))
    for j in range(q):
        l, r = map(int, input().split())
        ans = s[r] - s[l-1]
        print(ans)


def B06():
    from itertools import accumulate
    n = int(input())
    a = list(map(int, input().split()))

    s = [0] + list(accumulate(a))
    m = [0] + list(accumulate([x^1 for x in a]))

    q = int(input())
    for j in range(q):
        l, r = map(int, input().split())
        strike = s[r] - s[l-1]
        miss = m[r] - m[l-1]
        
        if strike > miss:
            print("win")
        elif miss > strike:
            print("lose")
        else:
            print("draw")


"""
累積和 & 差分を管理
"""
def A07():
    from itertools import accumulate
    d = int(input())
    n = int(input())

    #前日比を記録
    a = [0]*(d+2)#0日目と(d+1)日目を追加
    for i in range(n):
        l, r = map(int, input().split())
        a[l] += 1
        a[r+1] -= 1

    #前日比の累積和でその日の参加人数が出る
    s = list(accumulate(a))
    for i in range(d):
        print(s[i+1])


def B07():
    from itertools import accumulate
    t = int(input())
    n = int(input())

    a = [0]*(t+1)
    for i in range(n):
        l, r = map(int, input().split())
        a[l] += 1
        a[r] -= 1

    s = list(accumulate(a))
    for i in range(t):
        print(s[i])

"""
2次元の累積和
"""
def A08():
    h, w = map(int, input().split())
    #0行目と0列目に0パディングすると後で簡単になる
    pad = 1
    max_h = h+pad
    max_w = w+pad
    
    x = [[0]*(max_w) for i in range(max_h)]
    for i in range(h):
        row = list(map(int, input().split()))
        for j in range(w):
            x[i+1][j+1] = row[j]

    #2次元の累積和
    z = [[0]*(max_w) for i in range(max_h)]

    #横方向の累積和
    for i in range(1, h+1):
        for j in range(1, w+1):
            z[i][j] += z[i][j-1] + x[i][j]

    #縦方向の累積和
    for j in range(1, w+1):
        for i in range(1, h+1):
            z[i][j] += z[i-1][j]

    q = int(input())
    for k in range(q):
        a, b, c, d = map(int, input().split())
        ans = z[c][d] + z[a-1][b-1] - z[c][b-1] - z[a-1][d] 
        print(ans)


def B08():
    n = int(input())
    max_x = 1509
    max_y = 1509

    a = [[0]*(max_x) for i in range(max_y)]
    for i in range(n):
        x, y = map(int, input().split())
        a[y][x] += 1

    #2次元の累積和
    z = [[0]*(max_x) for i in range(max_y)]

    #横方向の累積和
    for i in range(1, max_y):
        for j in range(1, max_x):
            z[i][j] += z[i][j-1] + a[i][j]

    #縦方向の累積和
    for j in range(1, max_x):
        for i in range(1, max_y):
            z[i][j] += z[i-1][j]

    q = int(input())
    for k in range(q):
        a, b, c, d = map(int, input().split())
        ans = z[d][c] + z[b-1][a-1] - z[d][a-1] - z[b-1][c] 
        print(ans)


"""
2次元の累積和 & 差分を管理
"""
def A09():
    h, w, n = map(int, input().split())
    max_h = h+2
    max_w = w+2
    x = [[0]*(max_w) for i in range(max_h)]

    for i in range(n):
        a, b, c, d = map(int, input().split())
        x[a][b] += 1
        x[a][d+1] -= 1
        x[c+1][b] -= 1
        x[c+1][d+1] += 1

    #2次元の累積和
    z = [[0]*(max_w) for i in range(max_h)]

    #横方向の累積和
    for i in range(1, h+1):
        for j in range(1, w+1):
            z[i][j] += z[i][j-1] + x[i][j]

    #縦方向の累積和
    for j in range(1, w+1):
        for i in range(1, h+1):
            z[i][j] += z[i-1][j]

    for i in range(1, h+1):
        print(" ".join([str(v) for v in z[i][1:-1]]))


def B09():
    n = int(input())
    max_x = 1509
    max_y = 1509
    p = [[0]*(max_x) for i in range(max_y)]

    #差分を記録
    for i in range(n):
        a, b, c, d = map(int, input().split())
        a += 1
        b += 1
        c += 1
        d += 1
        p[a][b] += 1
        p[c][d] += 1
        p[a][d] -= 1
        p[c][b] -= 1

    #2次元の累積和
    z = [[0]*(max_x) for i in range(max_y)]

    #横方向
    for i in range(1, max_y):
        for j in range(1, max_x):
            z[i][j] = z[i][j-1] + p[i][j]
    #縦方向
    for j in range(1, max_x):
        for i in range(1, max_y):
            z[i][j] += z[i-1][j]

    ans = 0
    for i in range(1, max_y):
        for j in range(1, max_x):
            if z[i][j] > 0:
                ans += 1
    print(ans)


def A10_TLE():
    n = int(input())
    a = list(map(int, input().split()))
    d = int(input())

    for i in range(d):
        l, r = map(int, input().split())
        l -= 1
        r -= 1
        ans = 0
        for j in range(n):
            if l<=j<=r:
                continue
            else:
                ans = max(ans, a[j])
        print(ans)


def A10_ans():
    n = int(input())
    a = list(map(int, input().split()))
    #l用の左から見た最大値
    l_max = [0]
    for i in range(n):
        l_max.append(max(a[i], l_max[i]))

    #r用の右から見た最大値
    r_max = [0]
    for i in range(n):
        r_max.append(max(a[n-1-i], r_max[i]))
    r_max = r_max[::-1]

    d = int(input())
    for i in range(d):
        l, r = map(int, input().split())
        ans = max(l_max[l-1], r_max[r])
        print(ans)
