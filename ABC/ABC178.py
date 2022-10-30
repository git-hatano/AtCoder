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
    ans = 1-x
    print(ans)


def B():
    a, b, c, d = map(int, input().split())
    ans = - float("inf")
    ans = max(ans, a*c)
    ans = max(ans, a*d)
    ans = max(ans, b*c)
    ans = max(ans, b*d)
    print(ans)


"""
ベン図的な考え方
s: 全体集合, 10通り(0~9) ** n桁
a: Ai=0が一つもない数列
b: Ai=9が一つもない数列
c: a & b
"""
def C_WA():
    n = int(input())
    mod = 10**9 +7

    s = pow(10, n)%mod
    a = pow(9, n)%mod
    b = pow(9, n)%mod
    c = pow(8, n)%mod
    ans = s - a - b + c
    print(ans)


"""
累乗していく段階でmodしておかないといけない
"""
def C():
    n = int(input())
    mod = 10**9 +7

    def powmod(x, y):
        res = 1
        for i in range(y):
            res = (res * x) %mod
        return res

    s = powmod(10, n)
    a = powmod(9, n)
    b = powmod(9, n)
    c = powmod(8, n)
    ans = s - a - b + c
    ans %= mod
    print(ans)


# def D():

