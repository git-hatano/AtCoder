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

def A():
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    s = "atcoder"
    print(s[l:r+1])


def B():
    r, c = map(int, input().split())
    r -= 1
    c -= 1

    import numpy as np
    arr = np.zeros((15, 15))
    #横線
    arr[0, :] = 1
    arr[2, 2:-2] = 1
    arr[4, 4:-4] = 1
    arr[6, 6:-6] = 1
    arr[8, 6:-6] = 1
    arr[10, 4:-4] = 1
    arr[12, 2:-2] = 1
    arr[14, :] = 1
    #縦線
    arr[:, 0] = 1
    arr[2:-2, 2] = 1
    arr[4:-4, 4] = 1
    arr[6:-6, 6] = 1
    arr[6:-6, 8] = 1
    arr[4:-4, 10] = 1
    arr[2:-2, 12] = 1
    arr[:, 14] = 1

    if arr[r, c]:
        print("black")
    else:
        print("white")



def C_RE_WA():
    import itertools
    from collections import defaultdict

    ah, aw = map(int, input().split())
    a = []
    for i in range(ah):
        a.append(list(map(int, input().split())))

    bh, bw = map(int, input().split())
    b = []
    for i in range(bh):
        b.append(list(map(int, input().split())))

    arr = [[0]*aw for i in range(ah)]
    for i in range(bh):
        for j in range(bw):
            for k in range(ah):
                for l in range(aw):
                    if b[i][j]==a[k][l]:
                        arr[k][l] = 1

    # d = defaultdict(list)
    d = {}
    for i in range(ah):
        for j in range(aw):
            if arr[i][j]==1:
                if i not in d.keys():
                    d[i] = []
                d[i].append(j)


    # ここから下が悪そう
    if len(d.keys()) >0:
        for key in d.keys():
            if len(d[key])!=bw:
                del d[key]
                # continue

    ans = True
    if bh != len(d.keys()):
        ans = False
    else:
        comb = list(itertools.combinations(d.keys(), 2))
        for t in comb:
            if d[t[0]] != d[t[1]]:
                ans = False
                break

    print("Yes" if ans else "No")



def C_WA():
    import itertools
    from collections import defaultdict

    ah, aw = map(int, input().split())
    a = []
    for i in range(ah):
        a.append(list(map(int, input().split())))

    bh, bw = map(int, input().split())
    b = []
    for i in range(bh):
        b.append(list(map(int, input().split())))

    arr = [[0]*aw for i in range(ah)]
    for i in range(bh):
        for j in range(bw):
            for k in range(ah):
                for l in range(aw):
                    if b[i][j]==a[k][l]:
                        arr[k][l] = 1

    # d = defaultdict(list)
    d = {}
    for i in range(ah):
        for j in range(aw):
            if arr[i][j]==1:
                if i not in d.keys():
                    d[i] = []
                d[i].append(j)

    ans = True
    if bh != len(d.keys()):
        ans = False
    else:
        for key in d.keys():
            if len(d[key]) != bw:
                ans = False
                break

        comb = list(itertools.combinations(d.keys(), 2))
        for t in comb:
            if d[t[0]] != d[t[1]]:
                ans = False
                break

    print("Yes" if ans else "No")



"""
bit 探索バージョン
"""
def C_ans_bitSearch():
    def solve():
        def judge(bit_r, bit_c):
            A2 = []
            for row in range(H1):
                if not (bit_r >> row & 1):
                    continue
                V = []
                for col in range(W1):
                    if bit_c >> col & 1:
                        V.append(A[row][col])
                A2.append(V)
            return A2 == B
        
        H1, W1 = map(int, input().split())
        A = [list(map(int, input().split())) for _ in range(H1)]
        
        H2, W2 = map(int, input().split())
        B = [list(map(int, input().split())) for _ in range(H2)]
        
        for bit_r in range(1 << H1):
            for bit_c in range(1 << W1):
                if judge(bit_r, bit_c):
                    return True
        return False

    print("Yes" if solve() else "No")



"""
itertools.combinations
で解く方法
こっちで書けるようになりたい
"""
def C_ans_com():
    from itertools import combinations
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]

    h, w = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(h)]

    def check(hidx, widx):
        for i in range(h):
            for j in range(w):
                if A[hidx[i]][widx[j]] != B[i][j]:
                    return False
        return True

    for hidx in combinations(range(H), h):
        for widx in combinations(range(W), w):
            if check(hidx, widx):
                print("Yes")
                exit()
    print("No")


"""
itertools.combinations + numpy
で解く方法
すっきりしていて美しい
"""
def C_ans_comb2():
    import numpy as np
    from itertools import combinations

    H, W = map(int, input().split())
    A = np.array([list(map(int, input().split())) for _ in range(H)])

    h, w = map(int, input().split())
    B =  np.array([list(map(int, input().split())) for _ in range(h)])

    for hidx in combinations(range(H), h):
        for widx in combinations(range(W), w):
            if np.all(A[hidx, :][:, widx]==B):
                print("Yes")
                exit()
    print("No")


def D():
    s = input()
    p = "atcoder"
    n = len(p)
    l = [p.index(c) for c in s]

    ans = 0
    for i in range(n-1):
        for j in range(n-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
                ans += 1

    print(ans)

