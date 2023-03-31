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
    d = {"Sunny":"Cloudy", "Cloudy":"Rainy", "Rainy":"Sunny"}
    print(d[s])


def B():
    s = input()
    n = len(s)

    ans = True
    for i in range(1, n+1):
        if i%2==1 and s[i-1]=="L":
            ans =False
        elif i%2==0 and s[i-1]=="R":
            ans =False
    print("Yes" if ans else "No")


def C():
    from collections import Counter
    n, k, q = map(int, input().split())
    a = []
    for j in range(q):
        a.append(int(input())-1)
    counter = Counter(a)

    for i in range(n):
        p = k
        if i in counter:
            p += counter[i]
        
        if p-q > 0:
            print("Yes")
        else:
            print("No")


def D_WA():
    import math
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    #大きい額から割引券を使う
    costs = []
    for i in range(n):
        if a[i]>2 and m>0:
            x = a[i]//2
            y = min(m, int(math.log2(x)))
            costs.append(a[i]//(2**y))
            m -= y
        else:
            costs.append(a[i])
    #まだ余っていたら使いきる
    costs.sort(reverse=True)
    for i in range(n):
        if m>0:
            if costs[i]==1:
                costs[i] //= 2 #=0
                m -= 1
            else:
                y = min(m, int(math.log2(costs[i])))
                costs[i] //= 2**y
                m -= y
    ans = sum(costs)
    if m>=ans:
        ans = 0
    print(ans)


"""
優先度付きque
を使って大きいものからひたすら割引券を使っていく
"""
def D_ans():
    import heapq
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    que = [-x for x in a]
    heapq.heapify(que)

    while m>0:
        minima = heapq.heappop(que)
        minima *= -1#反転しないと//2がうまくいかない?
        minima //= 2
        minima *= -1
        heapq.heappush(que, minima)
        m -= 1

    ans = -1*sum(que)
    print(ans)
