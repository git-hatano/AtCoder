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
    s = input()
    s = s[1:] + s[0]
    print(s)


def B():
    h, w, x, y = map(int, input().split())
    x-=1;y-=1
    s = []
    for _ in range(h):
        s.append(list(input()))

    vec = [[0, -1], [1, 0], [-1, 0], [0, 1]]
    ans = 1
    for v in vec:
        i = x
        j = y
        while i+v[0]>=0 and i+v[0]<h and j+v[1]>=0 and j+v[1]<w:
            i += v[0]
            j += v[1]
            if s[i][j]==".":
                ans += 1
            else:
                break
    print(ans)


"""
勝手に2分割だけと思い込んでしまった
2分割だけではない
"""
def C_WA():
    from collections import deque
    n = int(input())
    a = list(map(int, input().split()))

    ans = float("inf")
    if n==1:
        ans = min(ans, a[0]^0)
    else:
        left = [a[0]]
        right = deque(a[1:])

        for i in range(n-1):
            or_l = 0
            for j in range(len(left)):
                if j==0:
                    or_l = left[j]
                else:
                    or_l |= left[j]
                    
            or_r = 0
            for j in range(len(right)):
                if j==0:
                    or_r = right[j]
                else:
                    or_r |= right[j]
                    
            ans = min(ans, or_l^or_r)
            left.append(right.popleft())
    print(ans)


"""
bit全探索
nが小さいから全bit探索が試せる
"""
def C_ans():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 1<<30 #=2**30
    #切り方sを回す
    #あるbitが、1:切る, 0:切らない
    for s in range(1<<(n-1)): # 1<<(n-1) = 2**(n-1)
        # print(bin(s)[2:].zfill(n-1))
        now = 0
        o =0
        for i in range(n):
            o |= a[i]
            #iとi+1の間で切るようになっているかを確認
            if (s>>i)&1:
                now ^= o
                o = 0
        now ^= o
        ans = min(ans, now)
    print(ans)


"""
任意の点(x,y)を中心点(cx,xy)周りに, 角度thetaだけ回転
サンプルは通るがWA: 誤差が大きい?
"""
def f(x, y, cx, cy, theta):
    import math
    theta = math.radians(theta)
    new_x = x*math.cos(theta) - y*math.sin(theta) + cx - cx*math.cos(theta) + cy*math.sin(theta)
    new_y = x*math.sin(theta) + y*math.cos(theta) + cy - cx*math.sin(theta) - cy*math.cos(theta)
    return new_x, new_y

def D_WA():
    n = int(input())
    x0, y0 = map(int, input().split())
    xh, yh = map(int, input().split())
    #内角の和
    deg_total = 180*(n-2)
    #二等辺三角形の底角の大きさ
    deg_bottom = deg_total//(n*2)
    #二等辺三角形の中心核の大きさ
    deg_top = 180 - deg_bottom*2
    #中心の座標
    cx = (xh+x0)/2
    cy = (yh+y0)/2

    x1, y1 = f(x0, y0, cx, cy, deg_top)
    print(f"{x1} {y1}")


def D():
    n = int(input())
    x0, y0 = map(int, input().split())
    xh, yh = map(int, input().split())
    #二等辺三角形の中心核の大きさ #WAではここで誤差を稼いでしまった
    deg_top = 360/n
    #中心の座標
    cx = (xh+x0)/2
    cy = (yh+y0)/2

    x1, y1 = f(x0, y0, cx, cy, deg_top)
    print(f"{x1} {y1}")

