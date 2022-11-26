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
    ans = 0
    for c in s:
        if c=="v":
            ans+=1
        else:
            ans += 2
    print(ans)


def B():
    s = input() 
    t = input()
    ans = False
    if len(s) >= len(t):
        if t in s:
            ans = True
    print("Yes" if ans else "No")


def C():
    from collections import defaultdict
    def rot(s):
        return list(zip(*s[::-1]))

    h, w = map(int, input().split())
    s,t = [], []
    for i in range(h):
        s.append(list(input()))
    for i in range(h):
        t.append(list(input()))

    s_r = ["".join(x) for x in rot(s)]
    t_r = ["".join(x) for x in rot(t)]

    s_d = defaultdict(int)
    t_d = defaultdict(int)
    for i in range(w):
        s_d[s_r[i]] += 1
        t_d[t_r[i]] += 1

    ans = True
    for key in s_d:
        if key in t_d:
            if s_d[key] != t_d[key]:
                ans = False
                break
        else:
            ans = False
            break
    print("Yes" if ans else "No")


def D_TLE():
    import math
    a, b = map(int, input().split())
    g = 1
    t = a/math.sqrt(g)

    old_t = t
    while True:
        g += 1
        t = a/math.sqrt(g) + b*(g-1)
        if t >= old_t:
            ans = old_t
            break
        else:
            old_t = t
    print(ans)


def D():
    import math
    a, b = map(int, input().split())
    init_g = 1
    t = a/math.sqrt(init_g)
    ans = t
    
    #微分方程式(dt/dg = 0)で求めたgの初期値
    tmp_g = (a/(2*b))**(2/3)
    
    if tmp_g > init_g:
        tmp_g = int(tmp_g)
        for i in range(-1*10**3, 10**3):
            g = tmp_g +i
            if g > init_g:
                t = a/math.sqrt(g) + b*(g-1)
                ans = min(ans, t)
    print(ans)
