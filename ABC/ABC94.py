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


# def D():

