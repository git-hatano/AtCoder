'''
# 文字列を受け取る場合
s = input() 

# 1つの整数を入力
n = int(input())

# 複数の整数を入力
a, b = map(int, input().split())

# listで入力を受け取り
a = list(map(int, input().split()))
'''

def A():
    n = int(input())
    lim = 2**31
    if n>=-lim and n<lim:
        print("Yes")
    else:
        print("No")

def B():
    h, w = map(int, input().split())
    a = []
    for i in range(h):
        a.append(list(map(int, input().split())))

    import numpy as np
    a = np.array(a)
    b = a.T
    for i in range(w):
        print(" ".join([str(x) for x in list(b[i])]))


def C():
    s = input()
    ans = False
    # 元から回文のとき
    if s==s[::-1]:
        ans = True
    else:
        if s[-1]=="a":
            # 前側
            cnt_forward = 0
            for i in range(len(s)):
                if s[i]=="a":
                    cnt_forward += 1
                else:
                    break
            # 後ろ側
            cnt_back = 0
            for i in range(len(s)):
                if s[len(s)-1-i]=="a":
                    cnt_back += 1
                else:
                    break
            if cnt_back>cnt_forward:
                a = "a"*(cnt_back-cnt_forward)
                s = a+s
                if s==s[::-1]:
                    ans = True

    if ans:
        print("Yes")
    else:
        print("No")


def D_TLE():
    n = int(input())
    s = input()

    from collections import deque
    a = deque([0])
    for i, x in enumerate(s):
        if i==0:
            if x=="L":
                a.appendleft(i+1)
                pos = 0
            else:
                a.append(i+1)
                pos = 1
        else:
            if x=="L":
                a.insert(pos, i+1)
            else:
                pos += 1
                a.insert(pos, i+1)

    print(" ".join([str(x) for x in a]))


def D():
    n = int(input())
    s = input()

    L = []
    R = []
    for i, c in enumerate(s):
        if c=="L":
            R.append(i)
        else:
            L.append(i)

    res = L + [n] + R[::-1]
    print(" ".join([str(x) for x in res]))


