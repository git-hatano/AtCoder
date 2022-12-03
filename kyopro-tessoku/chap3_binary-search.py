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


