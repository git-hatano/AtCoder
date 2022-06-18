'''
1 秒間で処理できる for 文ループの回数は、10**8回程度

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

def test1():
    H, W = map(int, input().split())
    R, C = map(int, input().split())

    num = 4
    if W > 1 and H > 1:
        if R==1 or R==H:
            if C==1 or C==W:
                num = 2
            else:
                num = 3
        elif C==1 or C==W:
            num = 3
    else:
        if W==1 and H==1:
            num = 0
        else:
            if H > 1:
                if R==1 or R==H:
                    num = 1
                else:
                    num = 2
            elif W > 1:
                if C==1 or C==W:
                    num = 1
                else:
                    num = 2

    print(num)


def test2():
    import numpy as np
    N, A, B = map(int, input().split())

    arr = np.zeros((N*A, N*B))

    for i in range(N):
        for j in range(N):
            if (i+j)%2==1: #balck
                arr[i*A: i*A+A, j*B: j*B+B] = 1

    for a in range(N*A):
        rows =""
        for b in range(N*B):
            if arr[a, b] == 1:
                rows += "#"
            else:
                rows += "."    
        print(arr)


def test3_TLE():
    import numpy as np
    N, Q = map(int, input().split())
    x_list = []
    for n in range(Q):
        x_list.append(int(input()))

    a_list = np.arange(1, N+1)

    for x_i in x_list:
        index = a_list.tolist().index(x_i)

        if index == len(a_list)-1:
            a_list[index], a_list[index -1] = a_list[index-1], a_list[index]
        
        else:
            a_list[index], a_list[index +1] = a_list[index+1], a_list[index]
            
    print(" ".join([str(x) for x in a_list]))


import numpy as np
N, Q = map(int, input().split())

val = np.arange(1, N+1) #ボールの並びを管理：出力したいもの
pos = np.arange(0, N) #ボールの位置を管理：高速化に必要

x = []
for i in range(Q):
    x.append(int(input()))

for i in range(Q):
    p0 = pos[x[i] -1]
    p1 = p0

    if p0 != N-1:
        p1 += 1
    else:
        p1 -= 1
    
    v0 = val[p0]
    v1 = val[p1]

    val[p0], val[p1] = val[p1], val[p0]
    pos[v0-1], pos[v1-1] = pos[v1-1], pos[v0-1]

print(" ".join([str(v) for v in val]))