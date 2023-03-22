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
    a, b = map(int, input().split())
    ans = 0
    for i in range(2):
        if a>b:
            ans += a
            a -= 1
        else:
            ans += b
            b -= 1
    print(ans)


def B():
    n = int(input())
    h = list(map(int, input().split()))

    ans = 1
    m = h[0]
    for i in range(1, n):
        if h[i] >= m:
            ans += 1
            m = h[i]
    print(ans)


def C():
    s = input()
    n = len(s)
    ans = 10**6

    for i in range(2):
        t = []
        for j in range(n):
            t.append(str((i+j)%2))
        cnt = 0
        t = "".join(t)
        for j in range(n):
            if s[j]!=t[j]:
                cnt += 1
        ans = min(ans, cnt)
    print(ans)


# def D():
import sys
from collections import Counter
n, k = map(int, input().split())
s = [int(x) for x in input()]
counter = Counter(s)

if 1 in counter and counter[1]==n:
    ans = n
    print(ans)
    sys.exit()


