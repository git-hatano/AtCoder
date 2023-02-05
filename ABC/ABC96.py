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

# def A():



# def B():



def C():
    h, w = map(int, input().split())
    s = [list(input()) for _ in range(h)]
    vec = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    ans = True
    for i in range(h):
        for j in range(w):
            if s[i][j]=="#":
                ok = False
                for v in vec:
                    if 0<=i+v[0]<h and 0<=j+v[1]<w and s[i+v[0]][j+v[1]]=="#":
                        ok = True
                        break
                if not ok:
                    ans = False
    print("Yes" if ans else "No")


# def D():

