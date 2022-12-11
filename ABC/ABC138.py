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
    a = int(input())
    s = input() 
    if a>=3200:
        print(s)
    else:
        print("red")


def B():
    n = int(input())
    a = list(map(int, input().split()))
    s = 0
    for i in range(n):
        s += 1/a[i]
    ans = 1/s
    print(ans)


def C():
    n = int(input())
    v = list(map(int, input().split()))
    v.sort()
    sums = []
    for i in range(n):
        if i==0:
            sums.append(v[i])
        else:
            sums.append((sums[-1]+v[i])/2)
    print(sums[-1])


# def D():

