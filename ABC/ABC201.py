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
    a = list(map(int, input().split()))
    a = sorted(a)

    if a[2]-a[1] == a[1]-a[0]:
        ans = True
    else:
        ans = False
    print("Yes" if ans else "No")


def B():
    n = int(input())

    ts = []
    for i in range(n):
        s, t = input().split()
        t = int(t)
        ts.append([t, s])

    ts = sorted(ts, reverse=True)
    print(ts[1][1])


def C():
    s = input()
    need = []
    known = []

    for i, c in enumerate(s):
        if c=="o":
            need.append(i)
            known.append(i)
        elif c=="?":
            known.append(i)
    need = set(need)

    ans = 0
    if len(need)==4:
        ans = 24

    elif 0<len(known) and len(need)<4:
        from itertools import product
        buf = []
        for p in product(known, repeat=4):
            if need.issubset(p):
                buf.append("".join([str(x) for x in p]))
        ans = len(set(buf))
        
    print(ans)


def C_ans():
    s = input()

    ans = 0
    for i in range(10**4):
        #iに含まれる数字にフラグを立てる
        flag = [False]*10
        now = i
        for j in range(4):
            flag[now%10] = True
            now //= 10

        flag2 = True
        for j in range(10):
            if s[j]=="o" and not flag[j]:
                #暗証番号に確実に含まれていた数字jが含まれていない
                flag2 = False
            if s[j]=="x" and flag[j]:
                #暗証番号に確実に含まれていなかった数字jが含まれている
                flag2 = False
        
        ans += flag2
    print(ans)