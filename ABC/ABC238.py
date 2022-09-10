
def A():
    n = int(input())
    if 2**n > n**2:
        print("Yes")
    else:
        print("No")


def B():
    n = int(input())
    a = list(map(int, input().split()))

    # 切り込み角度の管理
    deg = [0]*360
    deg[0] = True

    cnt_a = 0
    for i in range(n):
        cnt_a += a[i]
        cnt_a %= 360
        deg[cnt_a] = True

    deg_old = -1
    deg_diff = []
    cnt = 0
    for i in range(360):
        if deg[i]==True:
            if deg_old >= 0:
                deg_diff.append(i - deg_old)
            
            if cnt == n:
                deg_diff.append(360-i)

            deg_old = i
            cnt += 1

    print(max(deg_diff))


def C_TLE():
    mod = 998244353
    n = int(input())
    buf = []
    for i in range(1, n+1):
        if i < 10:
            buf.append(i)
        else:
            k = 10**(len(str(i))-1)
            buf.append((i-k+1))
            
    ans = sum(buf) %mod
    print(ans)


def C():
    mod = 998244353
    n = int(input())

    # 具体的な計算を観察して、問題を置き換える
    ans = n*(n+1)//2

    for i in range(1, 18+1):
        if n >= 10**i:
            ans -= 9*10**(i-1) * (n-(10**i-1))

    print(ans%mod)
