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
    n, m, x, t, d = map(int, input().split())

    if m >= x:
        ans = t
    else:
        born = t - x*d
        ans = born + m*d

    print(ans)


def B():
    import numpy as np
    a, b, d, = map(int, input().split())

    u = np.array([a, b])

    t = np.deg2rad(d)
    # 回転行列
    R = np.array([[np.cos(t), -np.sin(t)],
                [np.sin(t),  np.cos(t)]])

    u = np.dot(R, u)
    print(u[0], u[1])


def C_WA_TLE():
    s = input()
    t = input()
    res = "No"

    if s==t:
        res = "Yes"
    else:
        if s[-1]==t[-1]:
            for i in range(len(t)):
                if i>1 and i<len(s):
                    if t[i]!=s[i]:
                        if t[i]==s[i-2] and t[i]==s[i-1]:
                            s = t[:i+1] + s[i:]
                        else:
                            break

                if s==t:
                    res = "Yes"
                    break
    print(res)

def C():
    '''
    ラングレス圧縮
    '''
    def trans(s):
        cnt = 1
        vec = []
        for i in range(len(s)):
            if i>0 and s[i-1]!=s[i]:
                vec.append([s[i-1], cnt])
                cnt = 1
            else:
                cnt += 1
        vec.append([s[i], cnt])
        return vec
            

    s = input()
    t = input()

    s_vec = trans(s)
    t_vec = trans(t)

    if len(s_vec)!=len(t_vec):
        res = False
    else:
        res = True
        for i in range(len(s_vec)):
            if s_vec[i][0]!=t_vec[i][0]:
                res = False
                break
            if not (s_vec[i][1]==t_vec[i][1] or (s_vec[i][1]<t_vec[i][1] and s_vec[i][1]>=2)):
                res = False
                break
        
    if res:
        print("Yes")
    else:
        print("No")

