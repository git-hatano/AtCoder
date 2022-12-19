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

def A36():
    n, k = map(int, input().split())
    ans = False
    if k >= 2*n-2 and k%2==0:
        ans = True
    print("Yes" if ans else "No")


def B36():
    n, k = map(int, input().split())
    s = input()
    on = 0
    for c in s:
        if c=="1":
            on += 1

    ans = False
    if on%2 == k%2:
        ans = True
    print("Yes" if ans else "No")


def A37():
    n, m, b = map(int, input().split())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))

    ans = sum(a)*m + b*n*m + sum(c)*n
    print(ans)


def B38_WA():
    d = {}
    def f(n):
        if n in d:
            return d[n]
        elif n < 10:
            d[n] = sum(range(1, n+1))
            return d[n]
        sn = str(n)
        return f(int(sn[:len(sn)//2])) + f(int(sn[len(sn)//2:]))

    n = int(input())
    print(f(n))


def A38():
    d, n = map(int, input().split())
    lim = [0]*(d+1)
    for i in range(1, d+1):
        lim[i] = 24

    for i in range(n):
        l, r, h = map(int, input().split())
        for j in range(l, r+1):
            lim[j] = min(lim[j], h)

    ans = sum(lim)
    print(ans)


def B38():
    n = int(input())
    s = input()
    heights = [1]*n
    for i in range(n-1):
        if s[i]=="A":
            heights[i+1] = max(heights[i+1], heights[i]+1)
        else:
            if heights[i]-1>=1:
                heights[i+1] = min(heights[i+1], heights[i]-1)
            else:
                heights[i] += 1
                for j in reversed(range(i+1)):
                    if j-1>=0 and heights[j]==heights[j-1]:
                        heights[j-1] += 1
                    else:
                        break
    ans = sum(heights)
    print(ans)


def B38_ans():
    n = int(input())
    s = input()
    #左から見て A:< がいくつ連続しているか
    streak1 = 1
    ret1 = [0]*n
    ret1[0] = 1
    for i in range(n-1):
        if s[i]=="A":
            streak1 += 1
        if s[i]=="B":
            streak1 = 1
        ret1[i+1] = streak1
    #右から見て B:> がいくつ連続しているか
    streak2 = 1
    ret2 = [0]*n
    ret2[n-1] = 1
    for i in reversed(range(n-1)):
        if s[i]=="B":
            streak2 += 1
        if s[i]=="A":
            streak2 = 1
        ret2[i] = streak2
    #ret1[i]とret2[i]の大きい方が答え
    ans = 0
    for i in range(n):
        ans += max(ret1[i], ret2[i])
    print(ans)


"""
区間スケジューリング問題
終了時刻が早い順に採用していく
"""
def A39():
    n = int(input())
    a = []
    for i in range(n):
        l, r = map(int, input().split())
        a.append([r, l, i])
    a.sort()

    ans = []
    cur = 0
    for i in range(n):
        if a[i][1]>=cur:
            ans.append(a[i][2])
            cur = a[i][0]
    print(len(ans))


def B39_TLE():
    n, d = map(int, input().split())
    xs = []
    ys = []
    for i in range(n):
        x, y = map(int, input().split())
        xs.append(x)
        ys.append(y)

    used = [False]*(n+1)
    ans = 0
    for i in range(1, d+1):
        maxValue = 0
        maxID = -1
        for j in range(n):
            if used[j]:
                continue
            if maxValue<ys[j] and xs[j]<=i:
                maxValue = ys[j]
                maxID = j
        
        if maxID!=-1:
            ans += maxValue
            used[maxID] = True
    print(ans)


def B39():
    n, d = map(int, input().split())
    a = []
    for i in range(n):
        x, y = map(int, input().split())
        a.append([x, y])

    a = sorted(a, key=lambda x: (x[1], -x[0]), reverse=True)
    used = [False]*n
    ans = 0
    for i in range(1, d+1):
        for j in range(n):
            if a[j][0]<=i and used[j]==False:
                ans += a[j][1]
                used[j] = True
                break
    print(ans)


def A40():
    from collections import Counter
    import math
    def combinations_count(n, r):
        return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

    n = int(input())
    a = list(map(int, input().split()))
    counter = Counter(a)
    ans = 0
    for key in counter:
        if counter[key]>=3:
            ans += combinations_count(counter[key], 3)
    print(ans)


def B40():
    from collections import defaultdict
    n = int(input())
    a = list(map(int, input().split()))
    cnt = defaultdict(int)

    for i in range(n):
        p = a[i]%100
        cnt[p] += 1

    ans = 0
    for key in cnt:
        x = 100 - key
        if key<x and x in cnt:
            ans += cnt[x]*cnt[key]

    if 0 in cnt:
        ans += cnt[0]*(cnt[0]-1)//2
    if 50 in cnt:
        ans += cnt[50]*(cnt[50]-1)//2
    print(ans)


def A41():
    n = int(input())
    s = input()
    ans = False
    for i in range(n-2):
        if s[i:i+3]=="RRR" or s[i:i+3]=="BBB":
            ans = True
    print("Yes" if ans else "No")


def B41():
    x, y = map(int, input().split())
    values = []
    while not (x==1 and y==1):
        values.append([x, y])
        if x>y:
            x -= y
        elif y>x:
            y -= x

    k = len(values)
    print(k)
    for i in reversed(range(k)):
        print(" ".join([str(v) for v in values[i]]))


def A42():
    n, k = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)

    ans = 0
    for ai in range(1, 101):
        for bi in range(1, 101):
            cnt = 0
            for i in range(n):
                if ai<=a[i]<=ai+k and bi<=b[i]<=bi+k:
                    cnt += 1
            ans = max(ans, cnt)
    print(ans)


def B42_WA():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    ans = 0
    for i in range(2): #表 0:正 1:負
        s1 = []
        s2 = []
        for j in range(n):
            if i==0 and a[j]>0:
                s1.append(a[j])
                s2.append(b[j])
            elif i==1 and a[j]<0:
                s1.append(a[j])
                s2.append(b[j])
        ans = max(ans, abs(sum(s1))+abs(sum(s2)))
        
    for i in range(2): #裏 0:正 1:負
        s1 = []
        s2 = []
        for j in range(n):
            if i==0 and b[j]>0:
                s1.append(a[j])
                s2.append(b[j])
            elif i==1 and b[j]<0:
                s1.append(a[j])
                s2.append(b[j])
        ans = max(ans, abs(sum(s1))+abs(sum(s2)))
    print(ans)


# omote=1 のとき表の総和が正
# ura=1 のとき裏の総和が正
# omote=2 のとき表の総和が負
# ura=2 のとき裏の総和が負
def B42_ans():
    def solve(omote, ura, a, b):
        s = 0
        for i in range(n):
            card1 = a[i]
            if omote==2:
                card1 = -a[i]
            card2 = b[i]
            if ura==2:
                card2 = -b[i]
            #カードiは選ぶべきか
            if card1 + card2 >= 0:
                s += (card1 + card2)
        return s

    n = int(input())
    a = [None]*n
    b = [None]*n
    for i in range(n):
        a[i], b[i] = map(int, input().split())

    ans1 = solve(1, 1, a, b)
    ans2 = solve(1, 2, a, b)
    ans3 = solve(2, 1, a, b)
    ans4 = solve(2, 2, a, b)
    print(max(ans1, ans2, ans3, ans4))


def A43():
    n, l = map(int, input().split())
    a = [None]*n
    b = [None]*n
    for i in range(n):
        a[i], b[i] = input().split()
        a[i] = int(a[i])

    ans = 0
    for i in range(n):
        if b[i]=="E":
            ans = max(ans, l-a[i])
        else:
            ans = max(ans, a[i])
    print(ans)


def B43():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    miss = [0]*n
    for i in range(m):
        miss[a[i]-1] += 1

    for i in range(n):
        print(m - miss[i])


def A44():
    n, q = map(int, input().split())
    a = list(range(1, n+1))
    reverse = False
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0]==1:
            x = query[1]
            y = query[2]
            if not reverse:
                a[x-1] = y
            else:
                a[-x] = y
        elif query[0]==2:
            reverse = not reverse
        else:
            x = query[1]
            if not reverse:
                print(a[x-1])
            else:
                print(a[-x])


def B44():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    r = list(range(n))

    q = int(input())
    for i in range(q):
        t, x, y = map(int, input().split())
        x -= 1
        y -= 1
        if t==1:
            r[x], r[y] = r[y], r[x]
        else:
            print(a[r[x]][y])

