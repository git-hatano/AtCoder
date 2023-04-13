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
    if n<1200:
        print("ABC")
    elif n<2800:
        print("ARC")
    else:
        print("AGC")


def B():
    s = input()
    n = len(s)
    pos = set([0])
    ans = True
    if s[0]!="A":
        ans = False
    cnt = 0
    for i in range(2, n-1):
        if s[i]=="C":
            cnt += 1
            pos.add(i)
    if cnt!=1:
        ans = False

    for i in range(n):
        if i not in pos and s[i].isupper():
            ans = False
    print("AC" if ans else "WA")


# def C():



# def D():

