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

def A51():
    from collections import deque
    q = int(input())
    stack = deque([])

    for i in range(q):
        query = input().split()
        if query[0]=="1":
            stack.append(query[1])
        elif query[0]=="2":
            print(stack[-1])
        else:
            stack.pop()


def B51():
    from collections import deque
    stack = deque([])
    s = input()

    for i, c in enumerate(s):
        if c=="(":
            stack.append(i)
        else:
            print(stack[-1]+1, i+1)
            stack.pop()


def A52():
    from collections import deque
    q = int(input())
    que = deque([])

    for i in range(q):
        query = input().split()
        if query[0]=="1":
            que.append(query[1])
        elif query[0]=="2":
            print(que[0])
        else:
            que.popleft()


def B52():
    from collections import deque
    que = deque([])
    n, x = map(int, input().split())
    x -= 1
    a = list(input())

    que.append(x)
    a[x] = "@"
    while len(que)>0:
        pos = que[0]
        if pos-1>=0 and a[pos-1]==".":
            a[pos-1] = "@"
            que.append(pos-1)
        if pos+1<n and a[pos+1]==".":
            a[pos+1] = "@"
            que.append(pos+1)
        que.popleft()
    print("".join([str(x) for x in a]))


def A53():
    import heapq
    que = []
    heapq.heapify(que)
    q = int(input())
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0]==1:
            heapq.heappush(que, query[1])
        elif query[0]==2:
            # pop 最小値が取り出せる
            minima = heapq.heappop(que)
            print(minima)
            # push
            heapq.heappush(que, minima)
        elif query[0]==3:
            heapq.heappop(que)


def A54():
    q = int(input())
    d = {}
    for i in range(q):
        query = input().split()
        if query[0]=="1":
            d[query[1]] = int(query[2])
        elif query[0]=="2":
            if query[1] in d:
                print(d[query[1]])


def B54():
    from collections import Counter
    import math
    def combinations_count(n, r):
        return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    counter = Counter(a)
    ans = 0
    for key in counter:
        if counter[key]>=2:
            ans += combinations_count(counter[key], 2)
    print(ans)


def A56():
    n, q = map(int, input().split())
    s = input()
    mod = 2147483647 #大きな素数
    power = 100 #26より大きな数
    #i文字目までのハッシュ値を計算
    h = [0]
    for i in range(1, n+1):
        h.append((h[i-1]*power + ord(s[i-1])-ord("a")+1)%mod)
    #100の累乗を予め計算
    power100 = [1]
    for i in range(1, n+1):
        power100.append((power100[i-1]*power)%mod)

    def hash_value(l, r):
        val = h[r] - (power100[r-l+1]*h[l-1])%mod
        if val<0:
            val += mod
        return val

    for i in range(q):
        a, b, c, d = map(int, input().split())
        h1 = hash_value(a, b)
        h2 = hash_value(c, d)
        print("Yes" if h1==h2 else "No")


"""
回文
ハッシュ値を使うと求めやすくなる
"""
def B56():
    n, q = map(int, input().split())
    s = input()
    mod = 2147483647 #大きな素数
    power = 100 #26より大きな数

    #左から読んだ時のハッシュ値を計算
    h = [0]
    for i in range(1, n+1):
        h.append((h[i-1]*power + ord(s[i-1])-ord("a")+1)%mod)
    #右から読んだ時のハッシュ値を計算
    s_rev = s[::-1]
    h_rev = [0]
    for i in range(1, n+1):
        h_rev.append((h_rev[i-1]*power + ord(s_rev[i-1])-ord("a")+1)%mod)

    #100の累乗を予め計算
    power100 = [1]
    for i in range(1, n+1):
        power100.append((power100[i-1]*power)%mod)

    def hash_value(l, r, h):
        val = h[r] - (power100[r-l+1]*h[l-1])%mod
        if val<0:
            val += mod
        return val

    for i in range(q):
        l, r = map(int, input().split())
        h1 = hash_value(l, r, h)
        h2 = hash_value(n-r+1, n-l+1, h_rev)
        print("Yes" if h1==h2 else "No")




