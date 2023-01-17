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
    x = int(input())
    if x>=0:
        ans = x
    else:
        ans = 0
    print(ans)


def B():
    sx, sy, gx, gy = map(int, input().split())
    points = [
        [sx, sy],
        [gx, gy]
    ]
    points = sorted(points)

    w = abs(points[1][0] - points[0][0])
    w *= points[0][1]/(points[0][1]+points[1][1])

    ans = points[0][0]+w
    print(ans)


def C():
    from itertools import permutations
    n, k = map(int, input().split())
    ts = [list(map(int, input().split())) for _ in range(n)]

    ans = 0
    for p in permutations(range(n)):
        cur = 0
        tmp = 0
        if p[0]==cur:
            for t in p:
                tmp += ts[cur][t]
                cur = t
            tmp += ts[cur][0]
            if tmp==k:
                ans += 1
        else:
            break
    print(ans)


"""
いもす法
"""
def D():
    from itertools import accumulate
    n, w = map(int, input().split())
    max_t = 2*(10**5)+1

    #変化量を記録
    a = [0]*max_t
    for i in range(n):
        s, t, p = map(int, input().split())
        a[s] += p
        a[t] -= p

    #累積和を取る: その時間の必要な量が求められる
    s = list(accumulate(a))
    ans = (w >= max(s))
    print("Yes" if ans else "No")
