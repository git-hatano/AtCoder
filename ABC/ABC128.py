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
    a, p = map(int, input().split())
    p += 3*a
    ans = p//2
    print(ans)


def B():
    n = int(input())
    a = []
    for i in range(n):
        s, p = input().split()
        a.append([s, int(p), i+1])

    a = sorted(a, key=lambda x: (x[0], -x[1]))
    for i in range(n):
        print(a[i][2])


"""
分からん
というより、難しく考えすぎた
"""
def C_WA():
    from itertools import combinations
    n, m = map(int, input().split())
    k = []
    s = []
    for i in range(m):
        x = list(map(int, input().split()))
        k.append(x[0])
        s.append(x[1:])
    p = list(map(int, input().split()))

    set1 = set()
    for i in range(m):
        if p[i]==0:
            start = 0
        else:
            start = 1
        
        set2 = set()
        for j in range(start, k[i]+1, 2):
            for c in combinations(s[i], j):
                b = [0]*m
                for l in range(j):
                    b[c[l]-1] = 1
                b = "".join([str(x) for x in b])
                set2.add(b)
        
        if i==0:
            set1 = set2
        else:
            set3 = set1
            set1 = set()
            for p2 in set2:
                for p3 in set3:
                    if int(p2, 2)|int(p3, 2)>0:
                        set1.add(bin(max(int(p2, 2), int(p3, 2)))[2:])
    ans = len(list(set1))
    print(ans)


"""
全bit探索
0始まりにするならちゃんとする
"""
def C():
    n, m = map(int, input().split())
    k = []
    s = []
    for i in range(m):
        x = list(map(int, input().split()))
        k.append(x[0])
        s.append([y-1 for y in x[1:]])
    p = list(map(int, input().split()))

    ans = 0
    for switch in range(2**n):#スイッチのon/offパターン
        ok = 0
        for ramp in range(m):#電球j
            cnt = 0
            for k in s[ramp]:#電球jに繋がっているスイッチ
                #今のスイッチのon/offパターンiと
                #電球jに繋がっているスイッチがonになっていたらカウント
                if switch & 2**k:
                    cnt += 1
            #カウントした結果、2の余りが与えられたものと同じならOK
            if cnt%2==p[ramp]:
                ok += 1
        if ok==m:#全ての電球が点灯するか
            ans += 1
    print(ans)
