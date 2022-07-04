'''
# 文字列を受け取る場合
S = input() 

# 1つの整数を入力
n = int(input())

# 複数の整数を入力
A, B = map(int, input().split())
A, B, C, D = map(int, input().split())

# listで入力を受け取り
a = list(map(int, input().split()))

# 文字列の反転
rev_S = S[::-1]
'''


def A():
    n = int(input())
    print(2**n)


def B():
    n = int(input())
    a = list(map(int, input().split()))
    p = 0

    # third, second, first, base
    bases = [0, 0, 0, 0]

    for i in range(n):
        bases[3] = 1
        bases += [0]*a[i]

        p += sum(bases[:-4])
        bases = bases[-4:]    
        
    print(p)


'''
探索の考え方はOK
だが、探索範囲を狭めすぎてしまった。
'''
def C():
    h1, h2, h3, w1, w2, w3 = list(map(int, input().split()))[:]
    a = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    count = 0
    for n in range(1, 30):
        a[0][0] = n

        for m in range(1, 30):
            a[0][1] = m
            a[0][2] = h1-a[0][0]-a[0][1]
            
            for l in range(1, 30):
                a[1][0] = l
                a[2][0] = w1-a[0][0]-a[1][0]

                for k in range(1, 30):
                    a[1][1] = k
                    a[1][2] = h2-a[1][0]-a[1][1]
                    a[2][1] = w2-a[0][1]-a[1][1]
                    a[2][2] = h3-a[2][0]-a[2][1]

                    if min(a[0][2], a[2][0], a[1][2], a[2][1], a[2][2])>0 and w3==(a[0][2]+a[1][2]+a[2][2]):
                        count += 1

    print(count)


'''
あと1問だけTLEだったからマジ惜しい
'''
def D_TLE():
    N = int(input())

    res = [0]*(2*10**5)
    for i in range(N):
        L, R = map(int, input().split())
        start = L-1
        stop = R-1
        res[start:stop] = [1]*(stop-start)

    old = 0
    for i in range(len(res)):
        if old==0 and res[i]==1:
            X = i+1
        
        if old==1 and res[i]==0:
            Y = i+1
            print(X, Y)
        
        old = res[i]


def D():
    N = int(input())
    LR = []
    for i in range(N):
        L, R = map(int, input().split())
        LR.append([L, R])

    LR = sorted(LR, key=lambda x: x[0])

    X = []
    Y = []
    for i in range(N):
        l = LR[i][0]
        r = LR[i][1]

        if len(X)==0 or Y[-1] < l:
            X.append(l)
            Y.append(r)
        else:
            if Y[-1] < r:
                Y[-1] = r

    for i in range(len(X)):
        print(X[i], Y[i])
