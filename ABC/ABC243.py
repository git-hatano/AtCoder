def B():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    res_1 = 0
    res_2 = 0
    temp_2 = {}
    for i in range(n):
        if a[i]==b[i]:
            res_1 += 1
        else:
            if a[i] in temp_2.keys():
                res_2 += 1
            else:
                temp_2[a[i]] = True
                
            if b[i] in temp_2.keys():
                res_2 += 1
            else:
                temp_2[b[i]] = True
    print(res_1)
    print(res_2)


def A():
    v, a, b, c = map(int, input().split())
    i = 0
    while (v >= 0):
        if i%3==0:
            v -= a
        elif i%3==1:
            v -= b
        elif i%3==2:
            v -= c
        i += 1
    if i%3==0:
        print("T")
    elif i%3==1:
        print("F")
    elif i%3==2:
        print("M")


def C():
    def Yes():
        print("Yes")
        exit(0)

    N = int(input())
    X, Y = [], []
    for _ in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    S = input()

    right_min, left_max = dict(), dict()
    for i in range(N):
        if S[i] == 'R':
            if Y[i] in left_max and X[i] < left_max[Y[i]]:
                Yes()
        else:
            if Y[i] in right_min and right_min[Y[i]] < X[i]:
                Yes()

        if S[i] == 'R':
            if Y[i] in right_min:
                right_min[Y[i]] = min(X[i], right_min[Y[i]])
            else:
                right_min[Y[i]] = X[i]
        else:
            if Y[i] in left_max:
                left_max[Y[i]] = max(X[i], left_max[Y[i]])
            else:
                left_max[Y[i]] = X[i]
    print("No")


"""
O(n)は間に合っているから、xの桁が大きい？
"""
def D_TLE():
    n, x = map(int, input().split())
    s = input()
    cur = x
    for i in range(n):
        if s[i]=="U":
            cur //= 2
        elif s[i]=="L":
            cur *= 2
        else:
            cur = 2*cur +1
    print(cur)


"""
相対的な移動量を求めて最後にxでスタートした時に置き換えられないか: むずそう
先にsを圧縮できないか: ここの計算量は関係なさそう? : こっちの考え方が正解
"""
def D_ans():
    n, x = map(int, input().split())
    s = input()
    t = []
    for i in range(n):
        if len(t)>0 and s[i]=="U" and (t[-1]=="R" or t[-1]=="L"):
            t.pop()
        else:
            t.append(s[i])
    for c in t:
        if c=="U":
            x //= 2
        elif c=="L":
            x *= 2
        elif c=="R":
            x = 2*x +1
    print(x)
