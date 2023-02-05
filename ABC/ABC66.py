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
    from collections import deque
    n = int(input())
    a = list(map(int, input().split()))
    b = deque([])
    for i in range(n):
        if i==0:
            b.append(a[i])
            continue
        if i%2==1:
            b.append(a[i])
        elif i%2==0:
            b.appendleft(a[i])

    if n%2==0:
        b.reverse()
    ans = " ".join([str(x) for x in b])
    print(ans)

# def D():

