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
    c = a+b
    if c>=15 and b>=8:
        ans = 1
    elif c>=10 and b>=3:
        ans = 2
    elif c>=3:
        ans = 3
    else:
        ans =4
    print(ans)


def B():
    n = int(input())
    a = []
    b = []
    sum_ab = []
    for i in range(n):
        x, y = map(int, input().split())
        a.append([x, i])
        b.append([y, i])
        sum_ab.append([x+y, i])

    a.sort()
    b.sort()
    sum_ab.sort()

    if a[0][1]==b[0][1]:
        tmp = min(max(a[0][0], b[1][0]), max(a[1][0], b[0][0]))
        ans = min(tmp, sum_ab[0][0])
    else:
        tmp = max(a[0][0], b[0][0])
        ans = min(tmp, sum_ab[0][0])

    print(ans)


def C_TLE():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            ans += (a[i]-a[j])**2
    print(ans)


def C_TLE2():
    n = int(input())
    a = list(map(int, input().split()))

    squared = sum([x**2 for x in a])

    comb = 0
    from itertools import combinations
    for c in combinations(a, 2):
        comb += c[0]*c[1]
        
    ans = (n-1)*squared -2*comb
    print(ans)


"""
N は大きくても出現する値の種類数は小さいので、同じ値の要素をまとめて処理
"""
def C_ans():
    from collections import Counter
    from itertools import combinations

    n = int(input())
    a = list(map(int, input().split()))

    counter = Counter(a)
    ans = 0
    for c in combinations(counter.keys(), 2):
        ans += counter[c[0]] * counter[c[1]] * (c[0]-c[1])**2
    print(ans)


# def D():

