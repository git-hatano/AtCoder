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
    if (a+b)%2 == 0:
        ans = (a+b)//2
        print(ans)
    else:
        print("IMPOSSIBLE")


def B():
    n = int(input())
    p = list(map(int, input().split()))
    diff = []
    ans = True
    for i in range(n):
        if p[i]!=i+1:
            diff.append([i+1, p[i]])

    if len(diff)>0:
        if len(diff)==2:
            if diff[0][0]!=diff[1][1] or diff[0][1]!=diff[1][0]:
                ans = False
        else:
            ans = False
    print("YES" if ans else "NO")


def C():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if b[i] >= a[i]:
            ans += a[i]
            b[i] -= a[i]
            a[i] = 0
        else:
            ans += b[i]
            a[i] -= b[i]
            b[i] = 0
        
        if b[i]==0:
            continue
        
        if b[i] >= a[i+1]:
            ans += a[i+1]
            b[i] -= a[i+1]
            a[i+1] = 0
        else:
            ans += b[i]
            a[i+1] -= b[i]
            b[i] = 0
    print(ans)


# def D():

