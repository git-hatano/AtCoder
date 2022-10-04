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
ans = False
print("Yes" if ans else "No")
'''

def A():
    a, b, c = map(int, input().split())
    if a**2 + b**2 < c**2:
        ans = True
    else:
        ans = False
    print("Yes" if ans else "No")


def B():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans = 0
    if min(b)>=max(a):
        ans = min(b)-max(a)+1
    print(ans)


def C_TLE():
    n = int(input())
    s = input() 
    q = int(input())
    query = []
    for i in range(q):
        t, a, b = map(int, input().split())
        a -= 1
        b -= 1
        query.append([t, a, b])

    for i in range(q):
        #t=1
        if query[i][0]==1:
            s = list(s)
            a = query[i][1]
            b = query[i][2]
            s[a], s[b] = s[b], s[a]
            s = "".join(s)
        #t=2
        else:
            s = s[n:] + s[:n]#ここがネック
    print(s)


"""
文字列のスワップを高速化
クエリが2の時、反転状態かどうかのフラグを変更する
反転状態であれば、クエリが1の時、a, bを変換する
"""
def C_ans():
    n = int(input())
    s = list(input())
    q = int(input())
    is_flipped = 0

    for i in range(q):
        t, a, b = map(int, input().split())
        if t==1:
            a -= 1
            b -= 1
            if is_flipped:
                a = (a+n)%(2*n)
                b = (b+n)%(2*n)
            s[a], s[b] = s[b], s[a]
        else:
            is_flipped ^= 1

    if is_flipped:
        s = s[n:] + s[:n]
    print("".join(s))


"""
文字列のスワップを高速化
文字列の前半と後半を別々に保持しておくパターン
考え方は分かりやすいかも
"""
def C_ans2():
    n = int(input())
    s = list(input())
    q = int(input())

    s = [s[:n], s[n:]]
    for i in range(q):
        t, a, b = map(int, input().split())
        if t==1:
            a -= 1
            b -= 1
            s[a//n][a%n], s[b//n][b%n] = s[b//n][b%n], s[a//n][a%n]
        else:
            s[0], s[1] = s[1], s[0]
    print("".join(s[0]+s[1]))


# def D():

