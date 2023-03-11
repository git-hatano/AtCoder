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

# def A():



def B():
    n, m, x, y = map(int, input().split())
    xs = list(map(int, input().split()))
    ys = list(map(int, input().split()))

    xs.sort()
    ys.sort()
    ans = False
    for i in range(101):
        if x<i<=y and xs[-1]<i and i<=ys[0]:
            ans = True
    print("No War" if ans else "War")


"""
19AC, 5WA
意外と通ったが手詰まり
"""
def C_WA():
    s = list(input())
    t = list(input())
    n = len(s)
    d = {}
    for i in range(n):
        if s[i]!=t[i]:
            if s[i] in d:
                d[d[s[i]]] = t[i]
            d[s[i]] = t[i]
            
            if t[i] in d:
                d[d[t[i]]] = s[i]
            d[t[i]] = s[i]

    new_s = []
    for i in range(n):
        if s[i] in d:
            new_s.append(d[s[i]])
        else:
            new_s.append(s[i])

    ans = True
    for i in range(n):
        if new_s[i]!=t[i]:
            ans = False
    print("Yes" if ans else "No")


"""
文字列を元に「f[i][j] := 文字iを文字jに変換するか」

「ある文字について複数の変換先があってはいけない」
「ある文字について複数の変換元があってはいけない」
というルールをチェックして判定
"""
def C_ans():
    import sys
    s = list(input())
    t = list(input())
    n = len(s)
    f = [[0]*26 for i in range(26)]
    for i in range(n):
        a = ord(s[i]) - ord("a")
        b = ord(t[i]) - ord("a")
        f[a][b] = 1

    #横方向に見る
    for i in range(26):
        cnt = 0
        for j in range(26):
            if f[i][j]>0:
                cnt += 1
        if cnt>=2:
            print("No")
            sys.exit()

    #縦方向に見る
    for j in range(26):
        cnt = 0
        for i in range(26):
            if f[i][j]>0:
                cnt += 1
        if cnt>=2:
            print("No")
            sys.exit()
    print("Yes")


# def D():

