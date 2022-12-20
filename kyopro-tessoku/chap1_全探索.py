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

def A01():
    n = int(input())
    print(n**2)


def B01():
    a, b = map(int, input().split())
    print(a+b)


def A02():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    a = set(a)
    if x in a:
        ans = True
    else:
        ans = False
    print("Yes" if ans else "No")


def B02():
    a, b = map(int, input().split())
    n = 100
    ans = False
    for i in range(a, b+1):
        if 100%i == 0:
            ans = True
            break
    print("Yes" if ans else "No")


def A03():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    set_q = set(q)

    ans = False
    for i in range(n):
        if k-p[i] in set_q:
            ans = True
            break
    print("Yes" if ans else "No")


def B03():
    from itertools import combinations
    n = int(input())
    a = list(map(int, input().split()))
    k = 1000
    ans = False
    for c in combinations(a, 3):
        if sum(c) == k:
            ans = True
            break
    print("Yes" if ans else "No")


def A04():
    n = int(input())
    b = []
    while n > 0:
        b.append(n%2)
        n //= 2

    b = b[::-1]
    b = "".join([str(x) for x in b])

    ans = "0"*(10-len(b)) + b
    print(ans)


def B04():
    n = input()
    ans = int(n, 2)
    print(ans)


def A05():
    n, k = map(int, input().split())
    ans = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if 0 < k-i-j <= n:
                ans += 1
    print(ans)
