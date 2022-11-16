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
    s = input()
    if s=="ABC":
        print("ARC")
    else:
        print("ABC")


def B():
    n, k = map(int, input().split())
    people = set()
    for i in range(k):
        d = int(input())
        a = list(map(int, input().split()))
        for x in a:
            people.add(x)

    ans = 0
    for i in range(n):
        if i+1 not in people:
            ans += 1
    print(ans)


def C():
    from collections import defaultdict
    n, m = map(int, input().split())
    h = list(map(int, input().split()))

    d = defaultdict(list)
    for j in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        d[a].append(h[b])
        d[b].append(h[a])

    ans = 0
    for i in range(n):
        if len(d[i])==0:
            ans += 1
        else:
            if h[i] > max(d[i]):
                ans += 1
    print(ans)


# def D():

