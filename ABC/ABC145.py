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
    r = int(input())
    print(r**2)


def B():
    n = int(input())
    s = input()

    ans = False
    if n%2 == 0:
        t1 = s[:n//2]
        t2 = s[n//2:]
        if t1 == t2:
            ans = True
    print("Yes" if ans else "No")


# def C():
from itertools import permutations
import math
n = int(input())
xs = []
ys = []
for i in range(n):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)

dists = []
for p in permutations(range(n)):
    dist = 0
    for i in range(n-1):
        town1 = p[i]
        town2 = p[i+1]
        dist += math.sqrt((xs[town1] - xs[town2])**2 + (ys[town1] - ys[town2])**2)
    dists.append(dist)

ans = sum(dists) / len(dists)
print(ans)


# def D():

