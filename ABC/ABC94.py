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

# def A():



# def B():



"""
二分探索
"""
def C():
    from bisect import bisect_left
    import math
    n = int(input())
    x = list(map(int, input().split()))
    a = sorted(x)
    mid = (n-1)/2 #中央値のインデックス
    for i in range(n):
        l = bisect_left(a, x[i])
        if l < mid:
            j = math.ceil(mid)
        else:
            j = int(mid)
        print(a[j])


def D_TLE():
    import math
    def combinations_count(n, r):
        return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

    n = int(input())
    a = list(map(int, input().split()))
    ans = []
    ma = 0
    for i in range(n):
        for j in range(n):
            if i!=j and a[i]>a[j]:
                tmp = combinations_count(a[i], a[j])
                if tmp > ma:
                    ma = tmp
                    ans = [a[i], a[j]]
    print(f"{ans[0]} {ans[1]}")


"""
aiはできるだけ大きいものを
ajはai//2に近いものを
"""
def D():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ai = a[n-1]
    aj = a[0]
    for i in range(n-1):
        if abs(a[i] - ai//2) <= abs(aj - ai//2):
            aj = a[i]
    print(f"{ai} {aj}")

