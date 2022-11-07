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
    a, b = map(int, input().split())
    print(a*b)


# import sys
# print(sys.maxsize)
# #92233 72036 85477 5807

def B():
    n = int(input())
    a = list(map(int, input().split()))

    thresh = 10**18
    a.sort()
    ans = 1
    for i in range(n):
        ans *= a[i]
        if ans > thresh:
            ans = -1
            break
    print(ans)


"""
小数の誤差でWAが出るようになっている問題
Decimalを使うと誤差を回避できる
https://qiita.com/papi_tokei/items/37a4e31949ba8efb6897
"""
def C_WA():
    a, b = map(float, input().split())
    ans = int(a*b)
    print(ans)


def C():
    from decimal import Decimal
    a, b = input().split()
    ans = int(Decimal(a)*Decimal(b))
    print(ans)


# def D():

