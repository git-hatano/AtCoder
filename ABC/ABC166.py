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


"""
10**3: 探索範囲が狭くてWA
10**4: TLE
"""
def D_TLE():
    x = int(input())
    for a in range(10**4):
        for b in range(10**4):
            if a**5-b**5 == x:
                print(a, b)
                break
            if a**5+b**5 == x:
                print(a, -b)
                break

"""
xの取りうる範囲を考えないといけなかった
200**5 - 199**5 = 7*10**9 > 10**9
だから、a=200, b=199まで抑えて全探索すればよかった
"""
def D_ans():
    x = int(input())
    v = {}
    for i in range(-1000, 1000):
        v[i**5] = i

    for key in v:
        b5 = key
        b = v[key]
        
        if x+b5 in v.keys():
            a = v[x+b5]
            print(a, b)
            break


