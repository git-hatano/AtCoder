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
    n, a, b = map(int, input().split())
    ans = min(a*n, b)
    print(ans)


def B():
    from itertools import combinations
    import math
    n, d = map(int, input().split())
    x = []
    for i in range(n):
        x.append(list(map(int, input().split())))

    ans = 0
    for c in combinations(range(n), 2):
        p1 = x[c[0]]
        p2 = x[c[1]]
        dist = 0
        for j in range(d):
            dist += (p1[j]-p2[j])**2
        
        if math.sqrt(dist).is_integer():
            ans += 1
    print(ans)


"""
WA x1
探索範囲が足りてなさそう
"""
def C_WA():
    l, r = map(int, input().split())
    mod = 2019

    lm = min(l%mod, r%mod)
    rm = max(l%mod, r%mod)
    ans = float("inf")
    for i in range(lm, rm):
        for j in range(i+1, rm+1):
            ans = min(ans, (i*j)%mod)
    print(ans)

def C_ans():
    l, r = map(int, input().split())
    mod = 2019

    if r-l >= mod:
        ans = 0
    else:
        ans = 2018
        for i in range(l, r):
            for j in range(i+1, r+1):
                ans = min(ans, (i*j)%mod)
    print(ans)


# def D():

