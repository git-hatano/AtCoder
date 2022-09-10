'''
# 文字列を受け取る場合
S = input() 

# 1つの整数を入力
n = int(input())

# 複数の整数を入力
A, B = map(int, input().split())

# listで入力を受け取り
a = list(map(int, input().split()))

# 文字列の反転
rev_S = S[::-1]

# 2次元配列
dp = [[0]*(K) for i in range(N)]

A~C問題でコードが煩雑になる時、問題文を読み間違えてる可能性大
'''

def A():
    k = int(input())
    h = k//60
    m = k%60
    if m < 10:
        m = "0"+str(m)
    else:
        m = str(m)

    print("{}:{}".format(21+h, m))


def B_WA():
    n = int(input())
    a = []
    for i in range(n):
        a.append([int(i) for i in list(input())])

    import numpy as np
    a = np.array(a)
    max_a = np.max(a.flatten())
    start_i, start_j = np.unravel_index(np.argmax(a), a.shape)

    a = np.tile(a, (3,3))
    start_i, start_j = start_i+n, start_j+n


    res = {(start_i, start_j):max_a}
    for k in range(n-1):
        max_tmp = 0
        max_tmp_i = 0
        max_tmp_j = 0
        for i in [-1, 1]:
            for j in [-1, 1]:
                if a[start_i+i][start_j+j] >= max_tmp:
                    if (start_i+i, start_j+j) not in res.keys():
                        max_tmp = a[start_i+i][start_j+j]
                        max_tmp_i = start_i+i
                        max_tmp_j = start_j+j
    
        res[(max_tmp_i, max_tmp_j)] = max_tmp
        start_i = max_tmp_i
        start_j = max_tmp_j
    
    ans = int("".join([str(i) for i in list(res.values())]))
    print(ans)


def B():
    n = int(input())
    a = []
    for i in range(n):
        a.append([int(i) for i in list(input())])

    di = [-1, -1, -1,  0, 0,  1, 1, 1]
    dj = [-1,  0,  1, -1, 1, -1, 0, 1]

    ans = 0
    # 全探索用2重ループ
    for i in range(n):
        for j in range(n):

            # 8方向用ループ
            for v in range(8):
                x = 0

                # n-1回移動するループ
                for k in range(n):
                    x = x*10 + a[i][j]
                    i += di[v]
                    j += dj[v]
                    i = (i+n)%n
                    j = (j+n)%n
                
                ans = max(ans, x)

    print(ans)


def C_TLE():
    n, q = map(int, input().split())
    s = input()

    for i in range(q):
        t, x = map(int, input().split())

        if t==1:
            for j in range(x):
                s = s[-1] + s[:-1]
        elif t==2:
            print(s[x-1])


'''
単純にやるとTLEになるので、ズレ幅を管理する
'''
def C():
    n, q = map(int, input().split())
    s = input()

    p = 0
    for i in range(q):
        t, x = map(int, input().split())

        if t==1:
            p = (p-x+n)%n
        elif t==2:
            print(s[(p+x-1)%n])


def D():
    n, x = map(int, input().split())

    ab = []
    s_ab = [0]*(n+1) #1回だけやった時の累積和
    for i in range(n):
        a, b= map(int, input().split())
        ab.append([a, b])
        s_ab[i+1] = s_ab[i] + a+b 

    ans = float('inf')
    for i in range(n):
        if x-i>0:
            tmp = s_ab[i+1] +ab[i][1]*(x-i-1)
            ans = min(ans, tmp)

    print(ans)
