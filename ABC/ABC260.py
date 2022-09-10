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
'''

def A():
    s = input()
    d = {}
    for i in range(len(s)):
        if s[i] not in d.keys():
            d[s[i]] = 1
        else:
            d[s[i]] += 1

    ans = False
    for key in d.keys():
        if d[key] == 1:
            ans = True
            break
        
    if ans:
        print(key)
    else:
        print(-1)


def B_RE():
    import pandas as pd
    n, x, y, z = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    d = []
    for i in range(1, n+1):
        d.append([i, a[i-1], b[i-1], a[i-1]+b[i-1], False])

    df = pd.DataFrame(d, columns=["index", "math", "eng", "sum", "res"])

    df = df.sort_values(["math", "index"], ascending=[False, True])
    cnt = 0
    if x>0:
        for i in range(n):
            if df.iat[i, 4] == False:
                df.iat[i, 4] = True
                cnt+=1
            if x==cnt:
                break
    # print(df)

    df = df.sort_values(["eng", "index"], ascending=[False, True])
    cnt = 0
    if y>0:
        for i in range(n):
            if df.iat[i, 4] == False:
                df.iat[i, 4] = True
                cnt+=1
            if y==cnt:
                break
    # print(df)

    df = df.sort_values(["sum", "index"], ascending=[False, True])
    cnt = 0
    if z>0:
        for i in range(n):
            if df.iat[i, 4] == False:
                df.iat[i, 4] = True
                cnt+=1
            if z==cnt:
                break
    # print(df)

    df = df.sort_values(["index"], ascending=[True])
    for i in range(n):
        if df.iat[i, 4] == True:
            print(df.iat[i, 0])


def B():
    n, x, y, z = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    res = [0]*n

    #math
    sort_l = sorted(a, reverse=True)
    test = x
    if test>0:
        cnt = 0
        for v in sort_l:
            for i in range(n):
                if v==a[i] and res[i]==0:
                    res[i] = 1
                    cnt+=1
                if cnt==test:
                    break
            if cnt==test:
                break
    #eng
    sort_l = sorted(b, reverse=True)
    test = y
    if test>0:
        cnt = 0
        for v in sort_l:
            for i in range(n):
                if v==b[i] and res[i]==0:
                    res[i] = 1
                    cnt+=1
                if cnt==test:
                    break
            if cnt==test:
                break
    #add
    test = z
    if test>0:
        cnt = 0
        ab = []
        for i in range(n):
            ab.append(a[i]+b[i])
        sort_l = sorted(ab, reverse=True)
        for v in sort_l:
            for i in range(n):
                if v==ab[i] and res[i]==0:
                    res[i] = 1
                    cnt+=1
                if cnt==test:
                    break
            if cnt==test:
                break

    #output
    for i in range(n):
        if res[i]==1:
            print(i+1)



def C():
    n, x, y = map(int, input().split())
    # r = [level1の個数, level2の個数, ..., level10の個数]
    r = [0]*10
    r[n-1] = 1
    # b = [level1の個数, level2の個数, ..., level10の個数]
    b = [0]*10

    # levelが大きい方から変換していく
    for i in reversed(range(10)):
        if i>0 and r[i] > 0:
            r[i-1] += r[i]
            b[i] += r[i]*x
            r[i] = 0
        
        if i>0 and b[i] > 0:
            r[i-1] += b[i]
            b[i-1] += b[i]*y
            b[i] = 0
            
    print(b[0])
