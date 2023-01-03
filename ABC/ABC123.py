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
    from itertools import combinations
    a = []
    n = 5
    for i in range(n):
        a.append(int(input()))
    k = int(input())

    ans = True #通信可能
    for c in combinations(a, 2):
        if abs(c[0] - c[1]) > k:
            ans = False
    print("Yay!" if ans else ":(")


def B():
    a = []
    n = 5
    for i in range(n):
        t = input()
        if t[-1]=="0":
            c = 10
        else:
            c = int(t[-1])
        a.append([c, int(t)])
    a.sort(reverse=True)

    ans = 0
    for i in range(n):
        if i==n-1:
            ans += a[i][1]
        else:
            ans += a[i][1] - a[i][0] +10
    print(ans)


"""
最小値じゃないところでも分割したからずれた？
"""
def C_WA():
    import math
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())

    ans = 0
    m = n
    for v in [a, b, c, d, e]:
        if m>v:
            ans += math.ceil(m/v)
            m = v
        else:
            ans += 1
    print(ans)


def C_ans():
    import math
    n = int(input())
    a = []
    for i in range(5):
        a.append(int(input()))

    mi = min(a)
    group = math.ceil(n/mi)#ボトルネックな場所のグループ数
    ans = 5 + group-1 #元の5に含まれているから1引く
    print(ans)


# def D():

