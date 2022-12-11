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
    n = int(input())
    print(n**3)


def B():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        if i>0 and a[i-1]+1==a[i]:
            ans += c[a[i-1]-1]
        ans += b[a[i]-1]
        
    print(ans)


def C():
    n = int(input())
    b = list(map(int, input().split()))
    a = [b[0]]
    for i in range(n-1):
        if a[-1] > b[i]:
            a[-1] = b[i]
        a.append(b[i])
    ans = sum(a)
    print(ans)


# def D():

