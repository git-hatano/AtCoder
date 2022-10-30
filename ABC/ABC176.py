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
    n, x, t = map(int, input().split())
    ans = math.ceil(n/x) *t
    print(ans)


def B():
    s = input()
    sum_s = 0
    for c in s:
        sum_s += int(c)

    ans = (sum_s%9==0)
    print("Yes" if ans else "No")


def C():
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    cur_max = a[0]
    for i in range(1, n):
        if cur_max > a[i]:
            ans += cur_max -a[i]
        cur_max = max(cur_max, a[i])

    print(ans)


# def D():

