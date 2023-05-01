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
    n, a, b = map(int, input().split())
    c = list(map(int, input().split()))
    d = a+b
    for i in range(n):
        if c[i]==d:
            print(i+1)
            break


def B():
    import sys
    h, w = map(int, input().split())
    a = [list(input()) for _ in range(h)]
    b = [list(input()) for _ in range(h)]

    for s in range(h):
        for t in range(w):
            ok = True
            for i in range(h):
                for j in range(w):
                    if a[(i+s)%h][(j+t)%w]!=b[i][j]:
                        ok = False
                        break
            if ok:
                print("Yes")
                sys.exit()
    print("No")




def C():
    h, w = map(int, input().split())
    c = [list(input()) for _ in range(h)]
    n = min(h, w)
    ans = [0]*(n+1)
    
    def test(i, j, d):
        for x in [-d, d]:
            for y in [-d, d]:
                s = i+x
                t = j+y
                if (not (0<=s<h and 0<=t<w)) or c[s][t]!="#":
                    return False
        return True

    for i in range(h):
        for j in range(w):
            if c[i][j]!="#":
                continue
            if test(i, j, 1):
                d = 1
                while test(i, j, d+1):
                    d += 1
                ans[d] += 1
    print(" ".join(str(x) for x in ans[1:]))


# def D():

