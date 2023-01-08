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
    key = "a"
    ans = -1
    if key in s:
        for i in reversed(range(len(s))):
            if s[i]==key:
                ans = i+1
                break
    print(ans)


def B():
    from collections import defaultdict
    n, m = map(int, input().split())

    d = defaultdict(list)
    for i in range(m):
        a, b = map(int, input().split())
        d[a].append(b)
        d[b].append(a)

    for i in range(n):
        d[i+1] = [len(d[i+1])] + sorted(d[i+1])
        ans = " ".join([str(x) for x in d[i+1]])
        print(ans)


def C():
    n = int(input())
    p = list(map(int, input().split()))

    for i in reversed(range(n-1)):
        if p[i] > p[i+1]:
            x = p[i]
            idx = i
            break

    buf = []
    for i in range(idx, n):
        if x > p[i]:
            buf.append([p[i], i])
    buf.sort(reverse=True)

    j = buf[0][1]
    p[idx], p[j] = p[j], p[idx]

    tmp = sorted(p[idx+1:], reverse=True)
    ans = p[:idx+1] + tmp

    ans = " ".join([str(x) for x in ans])
    print(ans)


"""
AC:18, WA:23
sampleは通る
"""
def D_WA():
    import sys
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()

    #全部同じなら何もしない
    same = True
    for i in range(n-1):
        if a[i]!=a[i+1]:
            same = False
    if same:
        print(0)
        sys.exit()

    #2でも3でも割れない数字が入っていたら無理
    for i in range(n):
        if a[i]!=1 and a[i]%2!=0 and a[i]%3!=0:
            print(-1)
            sys.exit()

    #その時の最小値に合わせることができるか見ていく? #math.log2(10**9) <= 30
    mi = a[0]
    while mi>=1:
        cnt = 0
        for i in range(1, n):
            if a[i]//mi == a[i]/mi:
                d = a[i]//mi
                if d%3==0:
                    cnt += d//3
                    d %= 3
                if d%2==0:
                    cnt += d//2
                    d %= 2
                if d!=0:
                    cnt = 0
                    break
            else:
                cnt = 0
                break
        if cnt>0:
            break
        
        if mi==1:
            break
        elif a[0]%3==0:
            mi //= 3
        elif a[0]%2==0:
            mi //= 2
        else:
            break
        
    if cnt==0:
        print(-1)
    else:
        print(cnt)


def D_ans():
    import math
    n = int(input())
    a = list(map(int, input().split()))

    #最大公約数
    g = 0
    for i in range(n):
        g = math.gcd(g, a[i])

    ans = 0
    for i in range(n):
        # なんで最大公約数で割っていい?
        # 最大公約数に揃えると考えて、最大公約数になるための操作回数を求めている
        a[i] //= g 
        while a[i]%2==0:#2で割り続ける
            a[i] //= 2
            ans += 1
        while a[i]%3==0:#3で割り続ける
            a[i] //= 3
            ans += 1
        if a[i]!=1:#2,3で割り続けて1じゃなかったら無理
            ans = -1
            break
    print(ans)


def D_ans2():
    import sys
    n = int(input())
    a = list(map(int, input().split()))
    cnt2 = []
    cnt3 = []
    #2,3で割り続けてそもそも同じになるか確認
    for i in range(n):
        cnt = 0
        while a[i]%2==0:#2で割り続ける
            a[i] //= 2
            cnt += 1
        cnt2.append(cnt)
        cnt = 0
        while a[i]%3==0:#3で割り続ける
            a[i] //= 3
            cnt += 1
        cnt3.append(cnt)

    #2,3で割り続けた結果、同じにならないなら無理
    for i in range(n-1):
        if a[i]!=a[i+1]:
            print(-1)
            sys.exit()
    ans = 0
    #/2の操作回数
    mi = min(cnt2)
    for i in range(n):
        ans += cnt2[i]-mi
    #/3の操作回数
    mi = min(cnt3)
    for i in range(n):
        ans += cnt3[i]-mi
    print(ans)
