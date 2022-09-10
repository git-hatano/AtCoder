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
print("Yes" if ans else "No")
'''

from re import T
from tkinter import E


def A():
    n = input()

    from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
    print(Decimal(str(n)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))


def B():
    n = int(input())

    from collections import defaultdict
    d = defaultdict(int)

    for i in range(n):
        a = list(map(int, input().split()))
        del a[0]
        key = ",".join([str(x) for x in a])
        d[key] += 1
        
    ans = len(d)
    print(ans)


def B_ans():
    n = int(input())
    la = []
    for i in range(n):
        # 文字列で格納すれば、二重リストにならないので、後段でset()が使える
        la.append(input())
        
    ans = len(set(la))
    print(ans)


#最小値を求められる形になっていない
def C_WA():
    n = int(input())
    x = []
    for i in range(n):
        a = list(map(int, input().split()))
        x.append(a)

    #技iを習得したら, i:1
    from collections import defaultdict
    d = defaultdict(int)

    t = 0
    for i in range(a[1]):
        if d[a[i+2]]==1 or x[a[i+2]-1][1]==0:
            d[a[i+2]] += 1
            t += x[a[i+2]-1][0]

    t += a[0]
    print(t)


def C():
    n = int(input())

    t = []
    k = []
    a = []
    for i in range(n):
        tmp = list(map(int, input().split()))
        t.append(tmp[0])
        k.append(tmp[1])
        a.append([x-1 for x in tmp[2:]])

    need = [False]*n
    need[n-1] = True
    for i in reversed(range(n)):
        if need[i]:
            for j in a[i]:
                need[j] =True

    ans = 0
    for i in range(n):
        if need[i]:
            ans += t[i]
            
    print(ans)



def D():
    n = int(input())
    points = []
    for i in range(n):
        points.append(list(map(int, input().split())))

    vec = set()

    from itertools import combinations
    import math
    for c in combinations(points, 2):
        # print(c)
        a = c[1][0] - c[0][0]
        b = c[1][1] - c[0][1]
        
        #最大公約数で割る
        gcd = math.gcd(a, b)
        a = a//gcd
        b = b//gcd
        
        vec.add(f"{a},{b}")
        vec.add(f"{-a},{-b}")

    print(len(vec))
