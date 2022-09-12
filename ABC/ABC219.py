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
例題はOKなのに通らない
ソートが想定（辞書順）と違う？
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


x = input() 
n = int(input())
s = [input() for _ in range(n)]




# def D():

