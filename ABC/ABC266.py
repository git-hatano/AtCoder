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
print("Yes" if ans else "No")
'''

def A():
    s = input() 
    i = (len(s)-1+1)//2
    print(s[i])

def B():
    v = 998244353
    n = int(input())

    i = n//v
    x = n - v*i
    print(x)

def C():
    """
    三角形の符号付き面積
        角v0-v1-v2 のなす角の大きさを判定
        https://qiita.com/NULLchar/items/aef3c133ee7a98410039
    [in]
        v0: [x0, y0]
        v1: [x1, y1]
        v2: [x2, y2]
    [return]
        s>0: 180度未満
        s<0: 180を超える
    """
    def func(v0, v1, v2):
        s = 1/2*(v0[0]*v1[1] + v1[0]*v2[1] + v2[0]*v0[1] - v0[1]*v1[0] - v1[1]*v2[0] - v2[1]*v0[0])
        return s

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    d = list(map(int, input().split()))

    ans = True
    #A
    s = func(d, a, b)
    if s<0:
        ans = False
    #B
    s = func(a, b, c)
    if s<0:
        ans = False
    #C
    s = func(b, c, d)
    if s<0:
        ans = False
    #D
    s = func(c, d, a)
    if s<0:
        ans = False
        
    print("Yes" if ans else "No")


# def D():
n = int(input())

pos = 0
point = 0
for i in range(n):
    t, x, a = map(int, input().split())
    #移動できる
    if abs(t-pos)>x:
        pos = x
        point += a
    
print()
