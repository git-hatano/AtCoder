import os

'''
A, B = map(int, input().split())

n = int(input())
a = list(map(int, input().split()))
'''

def test1():
    A, B, C, X = map(int, input().split())

    if 0 < X and X <= A:
        print(1)
    elif A+1 <= X and X <= B:
        print(C/(B-A))
    else:
        print(0)

def test2():
    # 文字列を受け取る場合
    S = input() 
    str_list = sorted(S)
    print("".join(str_list))

def test3():
    N = int(input())

    list_x = []
    for X in range(10**(N-1), 10**N):
        if "0" not in str(X):
            for n in range(len(str(X)) -1):
                x_i = int(str(X)[n])
                x_i1 = int(str(X)[n+1])

                if abs(x_i - x_i1) >1:
                    break
                
                if n == len(str(X))-2:
                    list_x.append(X)
            
    print(len(list_x)%998244353)


def trans(x):
    if x==1:
        return range(x, x+2)
    elif x==9:
        return range(x-1, x+1)
    else:
        return range(x-1, x+2)


def test3_1():
    N = int(input())
    list_x = []

    for x in range(1, 10):
        for n in range(N):
            

    


if __name__=='__main__':

    test3()
