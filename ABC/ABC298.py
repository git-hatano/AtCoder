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
    from collections import Counter
    n = int(input())
    s = list(input())
    counter = Counter(s)

    ans = False
    if counter["o"]>0 and counter["x"]==0:
        ans = True
    print("Yes" if ans else "No")


def rot(s):
    return list(zip(*s[::-1]))

def B():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    b = [list(map(int, input().split())) for _ in range(n)]

    ans = False
    for i in range(4):
        ok = True
        for i in range(n):
            for j in range(n):
                if a[i][j]==1 and b[i][j]==0:
                    ok = False
        if ok:
            ans = True
            break
        else:
            a = rot(a)
    print("Yes" if ans else "No")


def C():
    from collections import defaultdict
    n = int(input())
    q = int(input())

    boxes = defaultdict(list)
    cards = defaultdict(list)
    for i in range(q):
        query = list(map(int, input().split()))
        i = query[1]
        if query[0]==1:
            j = query[2]
            boxes[j].append(i)
            cards[i].append(j)
        elif query[0]==2:
            boxes[i] = sorted(boxes[i])
            print(" ".join([str(x) for x in boxes[i]]))
        else:
            cards[i] = sorted(list(set(cards[i])))
            print(" ".join([str(x) for x in cards[i]]))


def D_TLE():
    from collections import deque
    q = int(input())
    s = deque([1])
    mod = 998244353
    for i in range(q):
        query = list(input().split())
        query[0] = int(query[0])
        if query[0]==1:
            x = int(query[1])
            s.append(x)
        elif query[0]==2:
            s.popleft()
        else:
            ans = "".join([str(x) for x in s]) #ここがネック
            ans = int(ans) % mod
            print(ans)


"""
文字列やリストではなく、
そもそも数字で管理しておけばよかった

繰り返し二乗法(pow)
を使わないと累乗でTLEになる
"""
def D_ans():
    from collections import deque
    q = int(input())
    mod = 998244353
    s = deque([1])
    r = 1
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0]==1:
            x = query[1]
            s.append(x)
            r = (10*r + x) % mod
        elif query[0]==2:
            y = s.popleft()
            # r = r - y * (10**len(s) % mod) ##遅い
            r = r - y * (pow(10, len(s), mod)%mod)
            r %= mod
        else:
            print(r)

