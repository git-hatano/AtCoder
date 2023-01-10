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
    s, t = input().split()
    print(t+s)


def B():
    a, b, k = map(int, input().split())
    ans_a = a
    ans_b = b
    if k>0:
        ans_a = max(0, a-k)
        k -= (a - ans_a)
    if k>0:
        ans_b =  max(0, b-k)
    print(ans_a, ans_b)


"""
min() で考えた方がコードがすっきり
"""
def B_ans():
    a, b, k = map(int, input().split())
    eat = min(a, k)
    a -= eat
    k -= eat

    eat = min(b, k)
    b -= eat
    k -= eat
    print(a, b)


def C():
    import math
    def is_prime(n):
        if n == 1: 
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    x = int(input())
    ans = -1
    for i in range(x, 10**6):
        if is_prime(i):
            ans = i
            break
    print(ans)


"""
貪欲法（今勝てる時に勝つ）の考え方であっていた
DPでも解けるらしいが設計できず
"""
def D():
    from collections import deque
    n, k = map(int, input().split())
    r, s, p = map(int, input().split())
    t = input()
    #今出せないものを管理
    que = deque([-1]*k)#今出せないもの
    ans = 0
    for i in range(n):
        l = que.popleft()
        
        if t[i]=="r" and l!="p":
            ans += p
            que.append("p")
        elif t[i]=="s" and l!="r":
            ans += r
            que.append("r")
        elif t[i]=="p" and l!="s":
            ans += s
            que.append("s")
        else:
            #負け、あいこの場合はk手先で都合が良い方を出せるようにしておいた
            ans += 0
            que.append(-1)
    print(ans)
