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
    n = int(input())
    a = list(map(int, input().split()))
    ans = []
    for i in range(n):
        if a[i]%2==0:
            ans.append(a[i])
    ans = " ".join([str(x) for x in ans])
    print(ans)


def B():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    ans = []
    for i in range(h):
        tmp = []
        for j in range(w):
            if a[i][j]==0:
                tmp.append(".")
            else:
                tmp.append(chr(a[i][j]+64))
        tmp = "".join([str(x) for x in tmp])
        ans.append(tmp)
    for i in range(h):
        print(ans[i])


def C():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    c = a+b
    c.sort()
    pos_a = []
    i_a = 0
    pos_b = []
    i_b = 0
    for i in range(n+m):
        if i_a<n and c[i]==a[i_a]:
            pos_a.append(i+1)
            i_a += 1
        else:
            pos_b.append(i+1)
            i_b += 1

    pos_a = " ".join([str(x) for x in pos_a])
    pos_b = " ".join([str(x) for x in pos_b])

    print(pos_a)
    print(pos_b)


def D():
    import heapq
    que = []
    heapq.heapify(que)
    wait = set()
    num = 1
    n, q = map(int, input().split())
    for i in range(q):
        s = list(input().split())
        if s[0]=="1":
            heapq.heappush(que, num)
            num += 1
        elif s[0]=="2":
            x = int(s[1])
            wait.add(x)
        else:
            while que:
                if que[0] in wait:
                    wait.discard(que[0])
                    heapq.heappop(que)
                else:
                    print(que[0])
                    break
