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


def A57():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    """
    dp[i][j]: 2**i日後に穴jにいる
    """
    dp = [[0]*(n) for i in range(30)]
    for i in range(30):
        for j in range(n):
            if i==0:
                #穴jを0始まりに
                dp[i][j] = a[j]-1
            else:
                dp[i][j] = dp[i-1][dp[i-1][j]]

    for k in range(q):
        x, y = map(int, input().split())
        cur = x-1
        for d in reversed(range(30)):
            # if (y//2**d)%2 != 0: #Y の 2^d の位を取り出す
            if (y>>d)&1 == 1: #高速にY の 2^d の位を取り出す: yをd[bit]右にシフトして1と&を取るとできる
                cur = dp[d][cur]
        print(cur+1)


def B57():
    n, k = map(int, input().split())
    """
    dp[i][j]: 2**i回後にjになる
    """
    dp = [[None]*(n+1) for i in range(30)]
    for i in range(n+1):
        s = sum([int(x) for x in list(str(i))])
        dp[0][i] = i-s
    for d in range(1, 30):
        for i in range(n+1):
            dp[d][i] = dp[d-1][dp[d-1][i]]

    for i in range(1, n+1):
        curnum = i
        for d in reversed(range(30)):
            if (k>>d)&1 == 1:
                curnum = dp[d][curnum]
        print(curnum)


class segtree:
    #要素datの初期化を行う
    def __init__(self, n):
        self.size = 1
        while self.size < n:
            self.size *= 2
        self.dat = [0]*(self.size*2)
    
    #クエリ1に対する処理
    def update(self, pos, x):
        pos += self.size #posは0-indexedなので、A[pos]のみに対応するセル番号はpos+size
        self.dat[pos] = x
        while pos>=2:
            pos //= 2
            # self.dat[pos] = max(self.dat[pos*2], self.dat[pos*2+1])
            self.dat[pos] = self.dat[pos*2] + self.dat[pos*2+1]
    
    #クエリ2に対する処理
    """
    u: 現在のセル番号
    [a, b): セルに対する半開区間
    [l, r): 求めたい半開区間
    """
    def query(self, l, r, a, b, u):
        if r<=a or b<=l:#一切含まれない場合
            return 0
        if l<=a and b<=r:#完全に含まれる場合
            return self.dat[u]
        m = (a+b)//2
        answerl = self.query(l, r, a, m, u*2)
        answerr = self.query(l, r, m, b, u*2+1)
        # return max(answerl, answerr)
        return answerl +  answerr

def A58_ans():
    n, q = map(int, input().split())
    queries = [ list(map(int, input().split())) for i in range(q) ]
    Z = segtree(n)
    for q in queries:
        tp, *cont = q
        if tp==1:
            pos, x = cont
            Z.update(pos-1, x)
        if tp==2:
            l, r = cont
            answer = Z.query(l-1, r-1, 0, Z.size, 1)
            print(answer)


#RSQ segtreeクラスを使った版
def B59_ans():
    n = int(input())
    a = list(map(int, input().split()))
    Z = segtree(n)
    ans = 0
    for i in range(n):
        ans += Z.query(a[i], n, 0, Z.size, 1)
        Z.update(a[i]-1, 1)
    print(ans)


def B59_ans_py():
    size = 1<<18 #2**18
    dat = [0]*(size*2)
    #代入 seg[i]=v
    def update(i:int, v:int) -> None:
        i += size #datのサイズがバカでかいからこの書き方ができる
        dat[i] = v
        while i>1:
            i >>= 1 #i//=2
            dat[i] = dat[i*2] + dat[i*2+1]
    #sum(seg[l], seg[l+1], ..., seg[r-1])を求める
    def query(l:int, r:int) -> int:
        l += size
        r += size
        ans = 0
        while l<r:
            if l&1:
                ans += dat[l]
                l += 1
            if r&1:
                r -= 1
                ans += dat[r]
            l >>= 1 #l//=2
            r >>= 1 #r//=2
        return ans

    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += query(a[i]+1, size)
        update(a[i], 1)
    print(ans)


def A60():
    from collections import deque
    n = int(input())
    a = list(map(int, input().split()))
    stack = deque([])
    day = [-1]
    for i in range(n):
        if i>0:
            while len(stack)>0:
                if stack[-1][1] < a[i]:
                    stack.pop()
                else:
                    break
            if len(stack)>0:
                day.append(stack[-1][0])
            else:
                day.append(-1)
        stack.append([i+1, a[i]])

    ans = " ".join([str(x) for x in day])
    print(ans)
