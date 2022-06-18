import math
import os
from ssl import SSL_ERROR_EOF
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
    # 文字列を受け取る場合
    S = input() 

    S = "0" + S
    S = S[0:4]
    print(S)
    

def test2():
    import itertools
    import copy

    # 1つの整数を入力
    N = int(input())
    list_st = []
    for i in range(N):
        s, t = input().split()
        list_st.append([s, t])
    
    a = []
    for i in range(len(list_st)):
        buf = copy.deepcopy(list_st)
        buf.pop(i)
        buf = list(itertools.chain.from_iterable(buf))
        buf = set(buf)

        s = list_st[i][0]
        t = list_st[i][1]

        if s not in buf:
            a.append(True)
        elif t not in buf:
            a.append(True)
        else:
            a.append(False)
    
    if False in a:
        print("No")
    else:
        print("Yes")


def test3():
    import copy

    # 1つの整数を入力
    N = int(input())
    S = [1]

    if N > 1:
        for n in range(2, N+1):
            buf = []
            buf.extend(S)
            buf.append(n)
            buf.extend(S)
            S = copy.deepcopy(buf)

        S = list(map(lambda x: str(x), S))
        out = " ".join(S)
    else:
        out = 1

    print(out)

def test4():
    N = int(input())
    
    buf = []
    sum_ball = 0
    for i in range(N):
        query = list(map(int, input().split()))
        
        if query[0] == 1:
            x = query[1]
            c = query[2]

            a = [x] * c
            buf.extend(a)
        
        elif query[0] == 2:
            c = query[1]

            sum_ball = sum(buf[0: c])
            print(sum_ball)

            del buf[0: c]
            sum_ball = 0

if __name__=='__main__':

    test4()
