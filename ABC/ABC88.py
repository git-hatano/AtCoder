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
    c = [list(map(int, input().split())) for _ in range(3)]
    ans = True
    if c[0][0]-c[0][1] != c[1][0]-c[1][1]:
        ans = False
    if c[0][1]-c[0][2] != c[1][1]-c[1][2]:
        ans = False
    if c[1][0]-c[1][1] != c[2][0]-c[2][1]:
        ans = False
    if c[1][1]-c[1][2] != c[2][1]-c[2][2]:
        ans = False
    print("Yes" if ans else "No")


# def D():

