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
    a = int(input())
    ans = a + a**2 + a**3
    print(ans)


def B():
    s = input()
    t = input()
    len_s = len(s)

    ans = 0
    for i in range(len_s):
        if s[i] != t[i]:
            ans += 1
    print(ans)

"""
最小時間のものから読んでいけば良い？
"""
# def C():
n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


# def D():

