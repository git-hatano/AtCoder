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
    n = int(input())
    x = int(1.08*n)

    if x < 206:
        print("Yay!")
    elif x==206:
        print("so-so")
    else:
        print(":(")


def B():
    n = int(input())
    stock = 0
    day = 0

    while n>stock:
        day += 1
        stock += day

    print(day)


def C_TLE():
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    from itertools import combinations
    for c in combinations(a, 2):
        if c[0]!=c[1]:
            ans += 1

    print(ans)


"""
jの方を動かすことで、それまでに被っている分を除くことができる
"""
def C_ans():
    n = int(input())
    a = list(map(int, input().split()))

    from collections import defaultdict
    d = defaultdict(int)#0で初期化

    ans = 0
    for j in range(n):
        ans += (j - d[a[j]])
        d[a[j]] += 1

    print(ans)


# def D():

