'''
# 文字列を受け取る場合
s = input() 

# 1つの整数を入力
n = int(input())

# 複数の整数を入力
a, b = map(int, input().split())

# listで入力を受け取り
a = list(map(int, input().split()))

# Yes/Noテンプレ
ans = True
print("Yes" if ans else "No")
'''

def A():
    n = int(input())

    if n<40:
        print(40-n)
    elif 40<=n and n<70:
        print(70-n)
    elif 70<=n and n<90:
        print(90-n)
    else:
        print("expert")


def B():
    n = 3
    s = []
    for i in range(n):
        s.append(input())
        
    t = [int(x)-1 for x in input()]

    ans = ""
    for i in t:
        ans += s[i]
    print(ans)




"""
考え方はあってたが、変換表を間違えていた
"""
def C_WA():
    x = input() 
    n = int(input())
    s = [input() for _ in range(n)]

    #変換表の作成
    import string
    d = {}
    d_rev = {}
    a = string.ascii_lowercase
    for i in range(len(x)):
        d[a[i]] = x[i]
        d_rev[x[i]] = a[i]

    #変換
    s_trans = []
    for i in range(n):
        word = ""
        for c in s[i]:
            word += d[c]
        s_trans.append(word)

    #逆変換
    s_trans = sorted(s_trans)
    for i in range(n):
        word = ""
        for c in s_trans[i]:
            word += d_rev[c]
        print(word)


def C_ans():
    x = input() 
    n = int(input())
    s = [input() for _ in range(n)]

    #変換表の作成
    import string
    d = {}
    for i in range(26):
        nxt = chr(i + ord('a'))
        d[x[i]] = nxt

    trans = []
    for i in range(n):
        t = ""
        for c in s[i]:
            t += d[c]
        trans.append([t, s[i]])

    trans = sorted(trans)
    for i in range(n):
        print(trans[i][1])



# def D():
def C():
    x = input() 
    n = int(input())
    s = [input() for _ in range(n)]

    #変換表の作成
    import string
    d = {}
    d_rev = {}
    a = string.ascii_lowercase
    for i in range(len(x)):
        d[x[i]] = a[i]#####
        d_rev[a[i]] = x[i]#####

    #変換
    s_trans = []
    for i in range(n):
        word = ""
        for c in s[i]:
            word += d[c]
        s_trans.append(word)

    #逆変換
    s_trans = sorted(s_trans)
    for i in range(n):
        word = ""
        for c in s_trans[i]:
            word += d_rev[c]
        print(word)
