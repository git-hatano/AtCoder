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
    s = input()
    l = 0
    ans = 0
    for i in range(n):
        if s[i]=="|":
            l += 1
        elif s[i]=="*" and l==1:
            ans += 1
    if ans>0:
        print("in")
    else:
        print("out")


def B():
    n, t = map(int, input().split())
    c = list(map(int, input().split()))
    r = list(map(int, input().split()))

    if t not in set(c):
        t = c[0]
    ans = -1
    ma = 0
    for i in range(n):
        if c[i]==t and r[i]>ma:
            ans = i
            ma = r[i]
    print(ans+1)


def C():
    import sys
    n = int(input())
    s = list(input())
    ans = -1
    cnt = 0
    if len(set(s))==1:
        print(ans)
        sys.exit()

    for i in range(n):
        if s[i]=="o":
            cnt += 1
        else:
            ans = max(ans, cnt) 
            cnt = 0
    if cnt>0:
        ans = max(ans, cnt) 
    print(ans)


# def D():

