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


