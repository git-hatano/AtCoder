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
    n = int(input())
    for i in reversed(range(0, n+1)):
        print(i)


"""
こんなの解けないのいい加減にしてほしい
"""
def B_WA_RE():
    s = input()
    a = [chr(ord("A")+i) for i in range(26)]

    ans = True
    if len(s)>=8:
        if s[0] in a:
            if s[1] in a:
                ans = False
        else:
            ans = False

        if s[-1] in a:
            if s[-2] in a:
                ans = False
        else:
            ans = False

        if list(s[1:-1]) in a:
            ans = False
        elif len(s[1:-1])!=6:
            ans = False
        elif 10**5<=int(s[1:-1])<=999999:
            ans = False
    else:
        ans =False
    print("Yes" if ans else "No")


"""
str.isdigit()
文字列の中が数字のみかを判定
"""
def B_ans():
    s = input()
    if len(s)!=8 or s[0].isdigit() or s[-1].isdigit():
        print("No")
    elif s[1]=="0" or not s[1:-1].isdecimal():
        print("No")
    else:
        print("Yes")


def C():
    from itertools import accumulate
    from bisect import bisect_left

    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    t %= sum(a)
    s = [0] + list(accumulate(a))
    less_than_x_count = bisect_left(s, t)
    time = t - s[less_than_x_count-1]
    print(less_than_x_count, time)


def D_TLE():
    from itertools import combinations
    n, k, d = map(int, input().split())
    a = list(map(int, input().split()))

    sums = set()
    for c in combinations(a, k):
        s = sum(c)
        if s%d==0:
            sums.add(s)

    if len(sums)==0:
        print(-1)
    else:
        print(max(sums))


# n, k, d = map(int, input().split())
# a = list(map(int, input().split()))

