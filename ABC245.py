import os

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
    A, B, C, D = map(int, input().split())

    if A < C:
        print("Takahashi")
    elif A==C and B<=D:
        print("Takahashi")
    else:
        print("Aoki")

def test2():
    N = int(input())
    A = list(map(int, input().split()))
    
    


if __name__=='__main__':

    test2()
