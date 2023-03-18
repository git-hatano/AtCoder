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
ans = True #ans = False
print("Yes" if ans else "No")

# リストの中身を文字列に
ans = " ".join([str(x) for x in a])
'''

def A():
    a, b = map(int, input().split())
    ans = False
    if a%2==1 and b%2==1:
        ans = True
    print("Yes" if ans else "No")


def B():
    n = int(input())
    ss = set()
    words = []
    ans = True
    for i in range(n):
        s = input()
        if s in ss:
            ans = False
        if len(words)>0 and words[-1][-1]!=s[0]:
            ans = False
        ss.add(s)
        words.append(s)
    print("Yes" if ans else "No")


def C():
    import math
    n, x = map(int, input().split())
    xs = list(map(int, input().split()))
    xs.append(x)
    xs.sort()

    ans = 0
    for i in range(n):
        d = xs[i+1] - xs[i]
        ans = math.gcd(ans, d)
    print(ans)


"""
問題文が理解できてない?
複雑に考えすぎてた
"""
def D_WA():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    #[i, j]
    vecs = {
        # "U": [-1, 0], #上
        "D": [1, 0],  #下
        # "L": [0, -1], #左
        "R": [0, 1]   #右
    }
    process = []
    for i in range(h):
        for j in range(w):
            if a[i][j]>=1 and a[i][j]%2==1:
                for k in vecs:
                    y = i + vecs[k][0]
                    x = j + vecs[k][1]
                    if 0<=y<h and 0<=x<w:
                        if k=="D" and a[y][x]%2==0:
                            a[y][x] += 1
                            a[i][j] -= 1
                            process.append([i, j, y, x])
                            break
                        else:
                            a[y][x] += 1
                            a[i][j] -= 1
                            process.append([i, j, y, x])
    print(len(process))
    for p in process:
        i, j, y, x = p
        print(f"{i} {j} {y} {x}")


def D_ans():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    process = []
    #とりあえず右に奇数を寄せていく
    for i in range(h):
        for j in range(w-1):
            if a[i][j]%2==1:
                a[i][j+1] += 1
                a[i][j] -= 1
                process.append([i, j, i, j+1])

    #右端の列で奇数だったら下に寄せていく
    for i in range(h-1):
        if a[i][w-1]%2==1:
            a[i+1][w-1] += 1
            a[i][w-1] -= 1
            process.append([i, w-1, i+1, w-1])

    print(len(process))
    for p in process:
        i, j, y, x = p
        print(f"{i+1} {j+1} {y+1} {x+1}")
