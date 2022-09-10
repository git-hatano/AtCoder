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


# def C():


# def D():

