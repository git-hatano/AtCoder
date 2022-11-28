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
    s, t = input().split()
    a, b = map(int, input().split())
    u = input()

    if u==s:
        a -= 1
    else:
        b -= 1
    print(a, b)


# def B():



# def C():



# def D():

