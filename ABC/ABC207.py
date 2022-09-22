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
ans = False
print("Yes" if ans else "No")
'''

def A():
    a = list(map(int, input().split()))
    a = sorted(a)
    print(a[1]+a[2])


def B():
    a, b, c, d = map(int, input().split())

    ans = -1
    if c*d > b:
        i = 0
        blue = a
        red = 0
        while blue > red*d:
            i += 1
            blue += b
            red += c
        ans= i
            
    print(ans)


"""
ifのゴリ押しで通ってしまったが、たまたま感強い
"""
def C():
    n = int(input())
    t = []
    l = []
    r = []
    for i in range(n):
        a = list(map(int, input().split()))
        t.append(a[0])
        l.append(a[1])
        r.append(a[2])

    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if l[j]<l[i] and l[i]<r[j]:
                ans += 1
            elif l[j]<r[i] and r[i]<r[j]:
                ans += 1
            elif (t[i]==1 or t[i]==2) and (t[j]==1 or t[j]==3) and r[j]==l[i]:
                ans += 1
            elif (t[i]==1 or t[i]==3) and (t[j]==1 or t[j]==2) and r[i]==l[j]:
                ans += 1
            elif l[i]<=l[j] and r[j]<=r[i]:
                ans += 1
            elif l[j]<=l[i] and r[i]<=r[j]:
                ans += 1

    print(ans)


def C_ans():
    n = int(input())
    l = [0]*n
    r = [0]*n
    for i in range(n):
        t, l[i], r[i] = map(int, input().split())
        #開区間を閉区間にする
        if t==2:
            r[i] -= 0.5
        elif t==3:
            l[i] += 0.5
        elif t==4:
            l[i] += 0.5
            r[i] -= 0.5
        
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            ans += (max(l[i], l[j]) <= min(r[i], r[j]))
    print(ans)


# def D():

