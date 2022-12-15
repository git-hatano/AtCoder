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
    from collections import Counter
    s = list(input())
    ans = False
    if len(set(s))==2:
        s.sort()
        counter = Counter(s)
        if counter[s[0]]==counter[s[-1]]:
            ans = True
    print("Yes" if ans else "No")


def B():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(1, n-1):
        if p[i] == sorted([p[i-1], p[i], p[i+1]])[1]:
            ans += 1
    print(ans)


def C():
    n = int(input())
    d = list(map(int, input().split()))
    d.sort()
    ans = 0
    if d[n//2-1]<d[n//2]:
        ans = d[n//2] - d[n//2-1]
    print(ans)


# def D():

