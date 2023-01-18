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
    ans = False
    if b==2*a or b==2*a+1:
        ans = True
    print("Yes" if ans else "No")


def B():
    n = int(input())
    s = input() 
    for i in range(1, n):
        l = 0
        for j in range(0, n-i):
            if s[j]!=s[j+i]:
                l += 1
            else:
                break
        print(l)


def C():
    s = input()
    n = len(s)
    ans = 0
    for i in range(n):
        v = (ord(s[i])-ord('A')+1)
        e = (n-i-1)
        e = (26)**e
        ans += v*e
    print(ans)


def D_TLE():
    n = int(input())
    s = [None]*n
    t = [None]*n
    for i in range(n):
        s[i], t[i] = input().split()

    s_set = set(s)
    #renameできたか
    res = [False]*n
    cnt = 0
    ans = False
    for i in range(n*3):
        if cnt==n:
            ans = True
            break
        if res[i%n]==False and t[i%n] not in s:
            s_set.discard(s[i%n]) #ここが遅そう
            s_set.add(t[i%n])
            s[i%n] = t[i%n]
            res[i%n] = True
            cnt += 1
    print("Yes" if ans else "No")

"""
TLEが取れてWAになった時点でロジックが間違ってる
"""
def D_WA():
    from collections import defaultdict
    n = int(input())
    s = [None]*n
    t = [None]*n
    for i in range(n):
        s[i], t[i] = input().split()

    s_cnter = defaultdict(int)
    for i in range(n):
        s_cnter[s[i]] += 1

    #renameできたか
    res = [False]*n
    cnt = 0
    ans = False
    for i in range(n*3):
        if cnt==n:
            ans = True
            break
        if res[i%n]==False and s_cnter[t[i%n]]==0: #なんでこの分岐でできないの？
            s_cnter[s[i%n]] -= 1
            s_cnter[t[i%n]] += 1
            res[i%n] = True
            cnt += 1
    print("Yes" if ans else "No")


"""
グラフの形がサイクル、パスしかないので
サイクルがあるかを判定すれば良い
"""
def D_ans():
    import sys
    n = int(input())
    s = [None]*n
    t = [None]*n
    for i in range(n):
        s[i], t[i] = input().split()

    to = {} #有向グラフを作成
    for i in range(n):
        to[s[i]] = t[i]

    used = set() #計算量削減のために一度訪れたところを記録
    for ss in s: #始点を試す
        ns = ss
        while ns not in used:
            used.add(ns)
            if ns not in to.keys(): #行き先がなければbreak
                break
            ns = to[ns] #行き先があれば次に
            if ns==ss: #始点に帰ってきたか（サイクルになってるか）を判定
                print("No")
                sys.exit()
    print("Yes")
