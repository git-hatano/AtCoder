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

