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
print("Yes" if ans else "No")
'''

def A():
    x, y, n = map(int, input().split())
    y_per = y/3

    # 1この方がお得
    if y_per >= x:
        ans = x*n
    else:
        ans = (n//3)*y
        ans += (n%3)*x

    print(ans)


def B():
    n, m, t = map(int, input().split())
    a = list(map(int, input().split()))

    xy = {}
    for i in range(m):
        x, y = map(int, input().split())
        xy[x] = y
        
    pos = 1
    ans = True
    for i in range(n-1):
        if t > a[i]:
            t -= a[i]
            pos += 1
        else:
            ans = False
            break
            
        if pos in xy:
            t += xy[pos]
        
    print("Yes" if ans else "No")


def C():
    h, w = map(int, input().split())
    g = []
    for i in range(h):
        g.append(list(input()))

    # 通ったところ確認用
    posed = [[0]*w for i in range(h)]
    posed[0][0] = 1

    # i,j
    vec = {"U":[-1,0], "D":[1,0], "L":[0,-1], "R":[0,1]}
    pos = [0, 0]

    while True:
        v_i = vec[g[pos[0]][pos[1]]][0]
        v_j = vec[g[pos[0]][pos[1]]][1]
        
        #はじっこでない
        if (pos[0]+v_i)>=0 and (pos[0]+v_i)<h and (pos[1]+v_j)>=0 and (pos[1]+v_j)<w:
            pos[0] += v_i
            pos[1] += v_j
            
            # 無限対策
            if posed[pos[0]][pos[1]]==1:
                print(-1)
                break
            else:
                posed[pos[0]][pos[1]] = 1
                
        #はじっこ
        else:
            print(f"{pos[0]+1} {pos[1]+1}")
            break


def D_WA():
    n, p, q, r = map(int, input().split())
    a = list(map(int, input().split()))

    x = -1
    y = -1
    z = -1
    w = -1
    ans = False
    for i in range(n):
        #p
        tmp_p = a[i]
        for j in range(i+1, n):
            if tmp_p < p:
                tmp_p += a[j]
            elif tmp_p > p:
                break
            elif tmp_p == p:
                x = i
                y = j
                break
        if x<0 and y<0:
            continue
        #q
        tmp_q = a[y]
        for j in range(y+1, n):
            if tmp_q < q:
                tmp_q += a[j]
            elif tmp_q > q:
                break
            elif tmp_q == q:
                z = j
                break
        if z<0:
            continue
        #r
        tmp_r = a[z]
        for j in range(z+1, n):
            if tmp_r < r:
                tmp_r += a[j]
            elif tmp_r > r:
                break
            elif tmp_r == r:
                w = j
                break
        if w<0:
            continue
            
        if x>0 or y>0 or z>0 or w>0:
            ans = True
            break
    print("Yes" if ans else "No")


def D():
    n, p, q, r = map(int, input().split())
    a = list(map(int, input().split()))
    b = [p, q, r]

    # 累積和
    from itertools import accumulate
    s = [0] + list(accumulate(a))
    st = set(s)

    ans = False
    for i in range(n+1):
        ns = s[i]
        
        for j in range(3):
            ns += b[j]
            if ns not in st:
                break
            if j==2:
                ans = True
        
        if ans:
            break
                
    print("Yes" if ans else "No")
