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
    s = input()

    if s[n-1]=="o":
        ans = True
    else:
        ans = False
    print("Yes" if ans else "No")


def B():
    p = list(map(int, input().split()))
    s = ""
    for i in range(len(p)):
        s += chr(p[i]-1+97)
    print(s)


# def C():



# def D():

