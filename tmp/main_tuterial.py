'''
1 秒間で処理できる for 文ループの回数は、10**8回程度

# 文字列を受け取る場合
S = input() 

# 1つの整数を入力
n = int(input())

# 複数の整数を入力
A, B = map(int, input().split())
A, B, C, D = map(int, input().split())

# listで入力を受け取り
a = list(map(int, input().split()))

# 文字列の反転
rev_S = S[::-1]
'''


def findSumOfDigits(num):
    d_sum = 0
    while num > 0:
        d_sum += num % 10
        n = n // 10
    return d_sum

# 全探索をするときにループを減らすコツ
def threeLoop_to_twoLoop():
    N, Y = map(int, input().split())
    res = "-1 -1 -1"

    for x in range(N+1):
        for y in range(N+1-x):
            z = N - x -y
            total = 10000*x + 5000*y + 1000*z

            if x+y+z==N and total==Y:
                res = "{} {} {}".format(x, y, z)
    print(res)


def str_rev():
    # 文字列を受け取る場合
    S = input() 
    T = ""
    result = "NO"
    words = ["dream", "dreamer", "erase", "eraser"]

    # 反転
    rev_S = S[::-1]
    rev_words = [word[::-1] for word in words]

    i = 0
    while True:
        old_i = i
        for rev_word in rev_words:
            if rev_S[i:i+len(rev_word)] == rev_word:
                T += rev_word
                i += len(rev_word)
                break
        
        if rev_S == T:
            result = "YES"
            break

        if old_i == i:
            break

    print(result)

def tesst10():
    N = int(input())
    t = [0] * (N+1)
    x = [0] * (N+1)
    y = [0] * (N+1)

    for i in range(N):
        t[i+1], x[i+1], y[i+1] = map(int, input().split())

    can = True
    for i in range(N):
        dt = t[i+1] - t[i]
        dist = abs(x[i+1] - x[i]) + abs(y[i+1] - y[i])

        if dist > dt:
            can = False
        
        if dt%2 != dist%2:
            can = False

    if can:
        print("Yes")
    else:
        print("No")


def exam_grid1():
    import numpy as np
    H, W = map(int, input().split())

    S = []
    for i in range(H):
        S.append(input())

    bom_map = np.zeros((H, W)).astype("int")

    # bom map作成
    for h in range(H):
        for w in range(W):
            if S[h][w]=="#":
                for y in [-1, 0, 1]:
                    for x in [-1, 0, 1]:
                        if h+y>=0 and h+y<H and w+x>=0 and w+x<W:
                            bom_map[h+y, x+w] += 1

    # 表示用作成
    for h in range(H):
        buf = ""
        for w in range(W):
            if S[h][w]=="#":
                buf += "#"
            else:
                buf += str(bom_map[h, w])
        print(buf)

