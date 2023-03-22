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
    if n%2==0:
        ans=n
    else:
        ans=n*2
    print(ans)


def B():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = abs(a[0]-a[-1])
    print(ans)


"""
マンハッタン距離の差の総和を最小化するときは中央値を使う
"""
def C():
    n = int(input())
    a = list(map(int, input().split()))
    x = []
    for i in range(n):
        x.append(a[i]-i-1)
    x.sort()

    #中央値bを求める
    if n==1:
        b = x[0]
    elif n%2==1:
        b = x[n//2]
    else:
        b = (x[n//2-1] + x[n//2])//2
    
    ans = 0
    for i in range(n):
        ans += abs(a[i]-b-i-1)
    print(ans)


# def D():

