import math
import os
import numpy as np

'''
Atcoderのインデントは、スペース2

# 文字列を受け取る場合
S = input() 

# 1つの整数を入力
n = int(input())

# 複数の整数を入力
A, B = map(int, input().split())
A, B, C, D = map(int, input().split())

# listで入力を受け取り
a = list(map(int, input().split()))
'''

def test1():
    N = 3 
    points = np.array([list(map(int, input().split())) for l in range(N)])
    
    x_l = points[:, 0]
    y_l = points[:, 1]

    uniques, counts = np.unique(x_l, return_counts=True)
    for u, c in zip(uniques, counts):
        if c == 1:
            x = u

    uniques, counts = np.unique(y_l, return_counts=True)
    for u, c in zip(uniques, counts):
        if c == 1:
            y = u

    print("{} {}".format(x, y))



def test2():
    A, B = map(int, input().split())
    theta = math.atan2(B, A)
    x = math.cos(theta)
    y = math.sin(theta)

    print (x, y)
    
def test3():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    sort_A = sorted(A)

    prices = []
    for a in sort_A:
        if a < X:
            prices.append(max([a, 0]))
        else:
            k = a // X
            mod = a%X

            if K>0:
                if k<K:
                    if mod > X%2 and k+1<K:
                        k = k+1
                    prices.append(max([a-k*X, 0]))
                    K -= k
                else:
                    prices.append(max([a-K*X, 0]))
                    K = 0
            else:
                prices.append(max([a, 0]))

    print(sum(prices))


def C_TLE():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))

    while K>0:
        A = sorted(A, reverse=True)
        A[0] = max(A[0]-X, 0)
        K -= 1
        total = sum(A)

        if total==0:
            break

    print(total)


def C():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))

    # Xより高いものに優先して割り当てる
    for i in range(N):
        if K>0 and A[i]>=X:
            k = min(A[i]//X, K)
            A[i] = max(A[i]-k*X, 0)
            K -= k

    # 全てX未満になったので、値段が大きい方から1枚ずつ割り当てる
    A = sorted(A, reverse=True)
    for i in range(N):
        if K>0:
            A[i] = max(A[i]-X, 0)
            K -= 1
        else:
            break

    print(sum(A))
