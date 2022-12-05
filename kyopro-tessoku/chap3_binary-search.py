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
二分探索をするときは予めソートが必要
探索範囲の狭め方を正確にしないとTLEになる恐れ
"""
def A11_ans():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    l = 0
    r = n-1
    ans = -1
    while l <= r:
        i = (l+r)//2
        if x == a[i]:
            ans = i+1
            break
        if x < a[i]:
            r = i-1
        elif a[i] < x:
            l = i+1
            
    print(ans)


def A11_another():
    from bisect import bisect_left
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    pos = bisect_left(a, x)
    ans = pos+1
    print(ans)



def B11():
    from bisect import bisect_left
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()

    q = int(input())
    for i in range(q):
        x = int(input())
        pos = bisect_left(a, x)
        ans = pos
        print(ans)


"""
2分探索を使って答えの範囲を絞っていく
"""
def A12_ans():
    def check(x, k):
        s = 0
        for i in range(len(a)):
            s += x//a[i]
        if s >= k:
            return True
        else:
            return False
            
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    l = 0
    r = 10**9
    while l < r:
        mid = (l+r)//2
        chk = check(mid, k)
        if chk:
            r = mid
        else:
            l = mid+1
    print(l)


"""
短調増加関数の方程式を二分探索で解く
"""
def B12():
    def f(x):
        return x**3 + x
        
    n = int(input())
    l = 0
    r = 10**2
    thresh = 0.001

    m = (l+r)/2
    z = f(m)
    while l < r:
        #絶対誤差
        if abs(n-z) <= thresh:
            ans = m
            break
        #相対誤差
        if abs((n-z)/n) <= thresh:
            ans = m
            break
        
        m = (l+r)/2
        z = f(m)
        if z >= n:
            r = m
        else:
            l = m
    print(ans)


"""
しゃくとり法
"""
def A13():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    #ある要素から差がk以内の要素数を格納
    r = [0]*n
    for i in range(n-1):
        #しゃくとりのスタート地点
        if i==0:
            r[0] = 0
        else:
            r[i] = r[i-1]
        #スタート地点から差がk以下のところまで進む
        while r[i]<n-1 and a[r[i]+1] - a[i] <= k:
            r[i] += 1

    ans = 0
    for i in range(n-1):
        ans += r[i]-i
    print(ans)


"""
しゃくとり法 + 累積和
"""
def B13():
    from itertools import accumulate
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    s = [0] + list(accumulate(a))
    r = [0]*(n+1)
    for i in range(n):
        if i==0:
            r[i] = 0
        else:
            r[i] = r[i-1]
        while r[i]<n and s[r[i]+1]-s[i]<=k:
            r[i] += 1

    ans = 0
    for i in range(n):
        ans += r[i]-i
    print(ans)


"""
半分全探索
"""
def A14():
    from bisect import bisect_left
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    d = list(map(int, input().split()))

    #配列pを作成
    p = []
    for i in range(n):
        for j in range(n):
            p.append(a[i]+b[j])

    #配列qを作成
    q = []
    for i in range(n):
        for j in range(n):
            q.append(c[i]+d[j])

    #qに、k-p[i]が存在するかを確認
    #setが楽そうだが、今回は2分探索
    q.sort()
    ans = False
    for i in range(n*n):
        x = k-p[i]
        pos = bisect_left(q, x)
        if pos<n*n and q[pos]==x:
            ans = True
    print("Yes" if ans else "No")


"""
今まで使ってきた全bit探索は、len(a)=1の時、漏れが発生する
多分、zfillあたりが良くない
"""
def B14():
    from bisect import bisect_left
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    ans = False
    if n==1:#全bit探索の漏れ対策
        if a[0]==k:
            ans = True
        if k==0:
            ans = True
    else:
        #aの前半で実現可能な合計
        s_f = []
        bit_size = n//2
        for bit in range(2**bit_size):
            bit = bin(bit)[2:].zfill(bit_size)
            tmp = 0
            for i, b in enumerate(bit):
                if b=="1":
                    tmp += a[i]
            s_f.append(tmp)

        #aの後半で実現可能な合計
        s_b = []
        for bit in range(2**bit_size):
            bit = bin(bit)[2:].zfill(bit_size)
            tmp = 0
            for i, b in enumerate(bit):
                if b=="1":
                    tmp += a[n//2+i]
            s_b.append(tmp)

        s_b.sort()
        for i in range(2**bit_size):
            x = k-s_f[i]
            pos = bisect_left(s_b, x)
            if pos<2**bit_size and s_b[pos]==x:
                ans = True
        
    print("Yes" if ans else "No")


def B14_ans():
    import bisect
    import sys
    # 「配列 A にあるカードからいくつか選んだときの合計」として考えられるものを列挙
    # ビット全探索を使う
    def bitsearch(a):
        res = []
        for i in range(2 ** len(a)):#bitのパターン
            sum = 0 # 現在の合計値
            for j in range(len(a)):
                wari = (2 ** j)
                if (i // wari) % 2 == 1:#bitが1の要素を抽出して計算
                    sum += a[j]
            res.append(sum)
        return res

    # 入力
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    # カードを半分ずつに分ける
    L1 = A[0:(N//2)]
    L2 = A[(N//2):N]

    # それぞれについて、「あり得るカードの合計」を全列挙
    Sum1 = bitsearch(L1)
    Sum2 = bitsearch(L2)
    Sum1.sort()
    Sum2.sort()

    # 二分探索で Sum1[i] + Sum2[j] = K となるものが存在するかを見つける
    for i in range(len(Sum1)):
        pos = bisect.bisect_left(Sum2, K-Sum1[i])
        if pos<len(Sum2) and Sum2[pos]==K-Sum1[i]:
            print("Yes")
            sys.exit(0)

    # 見つからなかった場合
    print("No")


"""
dict版
"""
def A15():
    n = int(input())
    a = list(map(int, input().split()))

    sort_a = sorted(set(a))
    d = {}
    cnt = 0
    for x in sort_a:
        d[x] = cnt+1
        cnt += 1

    b = []
    for i in range(n):
        b.append(d[a[i]])
    ans = " ".join([str(x) for x in b])
    print(ans)


"""
二分探索版
"""
def A15_ans():
    from bisect import bisect_left
    n = int(input())
    a = list(map(int, input().split()))

    t = sorted(set(a))
    b = []
    for i in range(n):
        pos = bisect_left(t, a[i])
        b.append(pos+1)

    ans = " ".join([str(x) for x in b])
    print(ans)
