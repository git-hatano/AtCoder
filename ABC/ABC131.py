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
    s = input() 
    ans = True
    for i in range(1, len(s)):
        if s[i]==s[i-1]:
            ans = False
    print("Good" if ans else "Bad")


def B():
    n, l = map(int, input().split())
    a = []
    for i in range(1, n+1):
        a.append([abs(l+i-1), l+i-1])
    a.sort()
    ans = 0
    for i in range(1, n):
        ans += a[i][1]

    print(ans)


def C_TLE():
    a, b, c, d = map(int, input().split())
    ans = 0
    for i in range(a, b+1):
        if i%c!=0 and i%d!=0:
            ans += 1
    print(ans)

"""
ベン図的な考え方
最小公倍数: https://note.nkmk.me/python-gcd-lcm/
"""
def C():
    import math
    def lcm(x, y):
        return (x * y) // math.gcd(x, y)

    a, b, c, d = map(int, input().split())
    # a<=x<=b となるxの個数
    u = b-a+1
    # uのうち、cで割り切れる個数
    set_c = b//c - (a-1)//c
    # uのうち、dで割り切れる個数
    set_d = b//d - (a-1)//d
    # uのうち、cとdの最小公倍数で割り切れる個数
    lcm_cd = lcm(c, d)
    set_cd = b//lcm_cd - (a-1)//lcm_cd

    ans = u - set_c - set_d + set_cd
    print(ans)


# def D():

