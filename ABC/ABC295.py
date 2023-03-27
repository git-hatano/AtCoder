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
    a = list(input().split())
    w = set(["and", "not", "that", "the", "you"])
    ans = False
    for i in range(n):
        if a[i] in w:
            ans = True
    print("Yes" if ans else "No")


def B():
    h, w = map(int, input().split())
    a = [list(input()) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if a[i][j]=="." or a[i][j]=="#":
                continue
            else:
                d = int(a[i][j])
                a[i][j]="."
                for k in range(h):
                    for l in range(w):
                        if abs(i-k)+abs(j-l)<=d:
                            if a[k][l]=="." or a[k][l]=="#": 
                                a[k][l] = "."
    for i in range(h):
        print("".join(a[i]))


def C():
    from collections import Counter
    n = int(input())
    a = list(map(int, input().split()))
    counter = Counter(a)
    ans = 0
    for k in counter:
        ans += counter[k]//2
    print(ans)


"""
O(n**3) は無理
"""
def D_TLE():
    from collections import Counter
    s = [int(x) for x in list(input())]
    n = len(s)
    ans = 0
    for l in range(n):
        for r in range(l+1, n):
            cntr = Counter(s[l:r+1])
            ok = True
            for k in cntr:
                if cntr[k]%2==0:
                    continue
                else:
                    ok = False
                    break
            if ok:
                ans += 1
                print(l, r)###
    print(ans)


def D_ans():
    from collections import defaultdict
    s = input()
    n = len(s)
    """
    x[i][j]: i桁目までの0~9の個数をまとめたテーブル
    i: 与えられた数字の桁数nのインデックス
    j: 0~9までの数字の種類
    """
    x = [[0]*(10) for i in range(n+1)]

    #i桁目までで奇数個なら1, 偶数個なら0
    for i in range(n):
        c = int(s[i])
        x[i+1] = x[i].copy()
        #XOR
        x[i+1][c] += 1
        x[i+1][c] %= 2

    #2進数でi桁目の数字の分布を表現
    mp = defaultdict(int)
    for i in range(n+1):
        bit = "".join([str(y) for y in x[i]])
        mp[int(bit, 2)] += 1

    #組み合わせの個数をカウント
    ans = 0
    for k in mp:
        num = mp[k]
        ans += num*(num-1)//2 # nC2
    print(ans)
