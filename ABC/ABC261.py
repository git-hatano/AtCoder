'''
# 文字列を受け取る場合
S = input() 

# 1つの整数を入力
n = int(input())

# 複数の整数を入力
A, B = map(int, input().split())

# listで入力を受け取り
a = list(map(int, input().split()))

# 文字列の反転
rev_S = S[::-1]

# 2次元配列
dp = [[0]*(K) for i in range(N)]
'''

def A():
    l1, r1, l2, r2 = map(int, input().split())
    map1 = [i for i in range(l1, r1+1)]
    map2 = [i for i in range(l2, r2+1)]

    res = []
    for i in range(100+1):
        if i in map1 and i in map2:
            res.append(i)

    if len(res) > 0:
        print(max(res) - min(res))
    else:
        print(0)


def B():
    n = int(input())
    a = []
    for i in range(n):
        s = input() 
        a.append(list(s))

    ans = True
    for i in range(n):
        for j in range(i+1, n):
            if a[i][j]=="W" and a[j][i]!="L":
                ans = False
            elif a[i][j]=="L" and a[j][i]!="W":
                ans = False
            elif a[i][j]=="D" and a[j][i]!="D":
                ans = False

    if ans:
        print("correct")
    else:
        print("incorrect")


def C():
    n = int(input())

    name = {}
    res = []
    for i in range(n):
        s = input()

        if s not in name:
            res.append(s)
            name[s] = 1
        else:
            s_re = "{}({})".format(s, name[s])
            res.append(s_re)
            name[s] += 1

    for i in range(n):
        print(res[i])


# def D():
