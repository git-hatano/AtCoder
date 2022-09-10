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
    if n>=42:
        n += 1
    print(f"AGC{str(n).zfill(3)}")


def B():
    s = input()
    t = "oxx"*10

    ans = False
    for i in range(len(t)):
        if s==t[i:i+len(s)]:
            ans = True
            break
    print("Yes" if ans else "No")
        

def C_RE_TLE():
    n, a, b = map(int, input().split())
    p, q, r, s = map(int, input().split())

    arr = [[0]*n for i in range(n)]
    k1 = range(max(1-a, 1-b), min(n-a, n-b)+1)
    for k in k1:
        arr[a+k-1][b+k-1] = 1

    k2 = range(max(1-a, b-n), min(n-a, b-1)+1)
    for k in k2:
        arr[a+k-1][b-k-1] = 1

    import numpy as np
    arr = np.array(arr)
    arr = arr[p-1:q+1, r-1:s+1]

    for i in range(arr.shape[0]):
        s = ""
        for j in range(arr.shape[1]):
            if arr[i,j]==0:
                s += "."
            else:
                s += "#"
        print(s)


def C():
    n, a, b = map(int, input().split())
    p, q, r, s = map(int, input().split())

    h = q-p-1
    w = s-r+1

    for i in range(p, q+1):
        ans = []
        for j in range(r, s+1):
            if (i-j == a-b) or (i+j == a+b):
                ans.append("#")
            else:
                ans.append(".")
        print(*ans, sep="")
    

# def D():

