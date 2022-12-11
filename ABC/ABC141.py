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
    s = input()
    d = {"Sunny":"Cloudy", "Cloudy":"Rainy", "Rainy":"Sunny"}
    print(d[s])


def B():
    s = input()
    n = len(s)

    ans = True
    for i in range(1, n+1):
        if i%2==1 and s[i-1]=="L":
            ans =False
        elif i%2==0 and s[i-1]=="R":
            ans =False
    print("Yes" if ans else "No")


def C():
    from collections import Counter
    n, k, q = map(int, input().split())
    a = []
    for j in range(q):
        a.append(int(input())-1)
    counter = Counter(a)

    for i in range(n):
        p = k
        if i in counter:
            p += counter[i]
        
        if p-q > 0:
            print("Yes")
        else:
            print("No")


# def D():

