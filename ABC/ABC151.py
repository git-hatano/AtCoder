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
    s = ord(s)
    ans = chr(s+1)
    print(ans)


def B():
    n, k, m = map(int, input().split())
    a = list(map(int, input().split()))

    x = max(0, m*n - sum(a))
    if x <= k:
        ans = x
    else:
        ans = -1
    print(ans)


def C():
    from collections import defaultdict
    n, m = map(int, input().split())
    ac_s = set()
    wa_d = defaultdict(int)

    for i in range(m):
        p, s = input().split()
        p = int(p)
        
        if p<=n and p not in ac_s:
            if s=="AC":
                ac_s.add(p)
            else:
                wa_d[p] += 1

    ac = len(ac_s)
    wa = 0
    for p in ac_s:
        wa += wa_d[p]

    print(f"{ac} {wa}")


# def D():

