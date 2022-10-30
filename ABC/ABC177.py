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
    d, t, s = map(int, input().split())
    ans = (t >= d/s)
    print("Yes" if ans else "No")


def B():
    s = input()
    t = input() 
    len_s = len(s)
    len_t = len(t)

    same = 0
    for i in range(len_s - len_t +1):
        tmp_same = 0
        for j in range(len_t):
            if t[j] == s[i+j]:
                tmp_same += 1
        same = max(same, tmp_same)

    ans = len_t - same
    print(ans)


"""
累積和
"""
def C():
    from itertools import accumulate

    n = int(input())
    a = list(map(int, input().split()))
    s = [0] + list(accumulate(a))
    mod = 10**9 +7

    ans = 0
    for i in range(n-1):
        ans += (a[i] * (s[-1] - s[i+1]))%mod
    print(ans%mod)


# def D():

