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
    s = input()
    ans = []
    for c in s:
        if c=="0":
            ans.append("1")
        else:
            ans.append("0")
    ans = "".join([str(x) for x in ans])
    print(ans)


def B():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a = [x-1 for x in a]
    s = []
    ans = []
    for i in range(n):
        s.append(i)
        if i not in a:
            s.reverse()
            ans += s
            s = []

    ans = " ".join([str(x+1) for x in ans])
    print(ans)


def C():
    from itertools import combinations
    n, m = map(int, input().split())
    a = []
    for i in range(m):
        c = input()
        a.append(list(map(int, input().split())))

    ans = 0
    for i in range(1, m+1):
        for c in combinations(range(m), i):
            s = set()
            for j in c:
                for v in a[j]:
                    s.add(v)
            if len(s)==n:
                ans += 1
    print(ans)


def D():
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = set(list(map(int, input().split())))
    x = int(input())

    ans = False
    dp = [False]*(x+1)
    dp[0] = True
    for i in range(x):
        if dp[i]:
            for j in range(n):
                nex = i+a[j]
                if nex not in b and nex<=x:
                    dp[nex] = True

    if dp[x]:
        ans = True
    print("Yes" if ans else "No")


from collections import defaultdict
t = int(input())
for _ in t:
    n, m = map(int, input().split())
    c = list(map(int, input().split()))#各頂点の色を格納
    g = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)
    
    
