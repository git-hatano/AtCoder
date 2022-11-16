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
    ans = (x>=30)
    print("Yes" if ans else "No")


def B():
    import math
    n, d = map(int, input().split())
    ans = 0
    for i in range(n):
        x, y = map(int, input().split())
        dist = math.sqrt(x**2 + y**2)
        if d >= dist:
            ans += 1
    print(ans)


"""
過去に同じ余りがあったら存在しない、ていう考え方は良かった。
"""
def C_TLE():
    k = int(input())
    ans = -1

    sevens = "7"*len(str(k))
    mods = set([])
    while True:
        mod = int(sevens)%k
        
        if mod in mods:
            break
        if mod == 0:
            ans = len(sevens)
            break
        
        mods.add(mod)
        sevens += "7"
    print(ans)


def C_TLE2():
    k = int(input())
    ans = -1
    sevens = 7
    mods = set([])

    while True:
        mod = sevens%k
        if mod in mods:
            break
        if mod == 0:
            ans = len(str(sevens))
            break
        
        mods.add(mod)
        sevens = 10*sevens +7
    print(ans)


"""
modの世界で考えれるとTLEを回避できた
そうすると計算量は, O(k): 0~k-1で済む
"""
def C_ans():
    k = int(input())
    x = 7%k ##ここがTLEになるかならないかの差分
    s = set()

    ans = -1
    i = 1
    while x not in s:
        if x==0:
            ans = i
            break
        
        s.add(x)
        x = (x*10+7)%k ## x(余り)の方を10倍して7足す
        i += 1
    print(ans)


def D():
    from collections import Counter
    n = int(input())
    c = list(input())

    counter = Counter(c)
    tmp_c = "R"*counter["R"] + "W"*counter["W"]

    ans = 0
    for i in range(n):
        if c[i]!=tmp_c[i]:
            ans += 1
    ans //= 2
    print(ans)
