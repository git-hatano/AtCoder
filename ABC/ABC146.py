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

def A():
    s = input()
    days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    ans = 7 - days.index(s)
    print(ans)


def B():
    n = int(input())
    s = input()
    ans = []
    for c in s:
        i = (ord(c) - ord("A") + n)%26 + ord("A")
        ans.append(chr(i))

    ans = "".join([str(x) for x in ans])
    print(ans)


def C_TLE():
    import math
    import sys
    a, b, x = map(int, input().split())

    n = 1
    x_tmp = a*n + b*(math.log10(n)+1)
    if x_tmp > x:
        print(0)
        sys.exit()

    while True:
        n += 1
        x_tmp = a*n + b*(int(math.log10(n))+1)
        
        if x_tmp > x:
            ans = n-1
            break
    print(ans)


"""
fは単調増加 → 二分探索ができる
"""
def C_ans():
    def f(n):
        return a*n + b*len(str(n))

    a, b, x = map(int, input().split())
    l = 0
    r = 10**9+1
    while r-l > 1:
        m = (l+r)//2
        if x >= f(m):
            l = m
        else:
            r = m
    print(l)
