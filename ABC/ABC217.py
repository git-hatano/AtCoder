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
ans = False
print("Yes" if ans else "No")
'''

def A():
    s,t = input().split()
    x = sorted([s, t])

    if s==x[0]:
        ans = True
    else:
        ans = False
    print("Yes" if ans else "No")


def B():
    s = []
    for _ in range(3):
        s.append(input())

    x = ["ABC", "ARC", "AGC", "AHC"]
    diff = set(s) ^ set(x)
    print(list(diff)[0])

def C():
    n = int(input())
    p = [x-1 for x in list(map(int, input().split()))]

    q = [0]*n
    for i in p:
        q[p[i]] = i
    print(" ".join([str(x+1) for x in q]))


"""
sampleは通るが、REが出る
やりたいことの考え方は似ていたが、実装できなかった
"""
def D_RE():
    l, q = map(int, input().split())
    pos = [False]*(l+1)
    pos[0] = True
    pos[l] = True
    for _ in range(q):
        c, x = map(int, input().split())
        if c==1:
            pos[x] = True
        else:
            start = -1
            end = -1
            #xから小さい方向に一番近い切れ目を探す
            for i in reversed(range(x+1)):
                if pos[i]:
                    start = i
                    break
            #xから大きい方向に一番近い切れ目を探す
            for i in range(x, l+1):
                if pos[i]:
                    end = i
                    break
            ans = end - start
            print(ans)


class BinaryTrie:
    def __init__(self, max_query=2*10**5, bitlen=30):
        n = max_query * bitlen
        self.nodes = [-1] * (2 * n)
        self.cnt = [0] * n
        self.id = 0
        self.bitlen = bitlen

    # xの挿入
    def insert(self,x):
        pt = 0
        for i in range(self.bitlen-1,-1,-1):
            y = x>>i&1
            if self.nodes[2*pt+y] == -1:
                self.id += 1
                self.nodes[2*pt+y] = self.id
            self.cnt[pt] += 1
            pt = self.nodes[2*pt+y]
        self.cnt[pt] += 1

    # 昇順x番目の値
    def kth_elm(self,x):
        pt, ans = 0, 0
        for i in range(self.bitlen-1,-1,-1):
            ans <<= 1
            if self.nodes[2*pt] != -1 and self.cnt[self.nodes[2*pt]] > 0:
                if self.cnt[self.nodes[2*pt]] >= x:
                    pt = self.nodes[2*pt]
                else:
                    x -= self.cnt[self.nodes[2*pt]]
                    pt = self.nodes[2*pt+1]
                    ans += 1
            else:
                pt = self.nodes[2*pt+1]
                ans += 1
        return ans

    # x以上の最小要素が昇順何番目か
    def lower_bound(self,x):
        pt, ans = 0, 1
        for i in range(self.bitlen-1,-1,-1):
            if pt == -1: break
            if x>>i&1 and self.nodes[2*pt] != -1:
                ans += self.cnt[self.nodes[2*pt]]
            pt = self.nodes[2*pt+(x>>i&1)]
        return ans


l, q = map(int, input().split())
bt = BinaryTrie()
bt.insert(0)
bt.insert(l)
for _ in range(q):
    c, x = map(int, input().split())
    if c==1:
        bt.insert(x)
    else:
        p = bt.lower_bound(x)
        ans = bt.kth_elm(p) - bt.kth_elm(p-1)
        print(ans)
        
