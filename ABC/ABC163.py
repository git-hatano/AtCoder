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
    import math
    r = int(input())
    ans = 2*math.pi*r
    print(ans)


def B():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    sum_a = sum(a)
    if sum_a > n:
        ans = -1
    else:
        ans = n - sum_a
    print(ans)


def C():
    from collections import Counter
    n = int(input())
    a = list(map(int, input().split()))
    counter = Counter(a)

    for i in range(n):
        if i+1 in counter.keys():
            ans = counter[i+1]
        else:
            ans = 0
        print(ans)


# def D():

