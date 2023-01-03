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
    s = list(map(int, input().split("/")))
    if s[0]<2019:
        print("Heisei")
    elif s[1]<4:
        print("Heisei")
    elif s[1]==4 and s[2]<=30:
        print("Heisei")
    else:
        print("TBD")


def B():
    n = int(input())
    rate = 380000
    yen = 0
    bit = 0
    for i in range(n):
        x, u = input().split()
        x = float(x)
        if u=="BTC":
            bit += x
        else:
            yen += x
    ans = yen + bit*rate
    print(ans)


# def C():



# def D():

