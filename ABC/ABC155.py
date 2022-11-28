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
    a, b, c = map(int, input().split())
    ans = False
    if len(set([a, b, c]))==2:
        ans = True
    print("Yes" if ans else "No")


def B():
    n = int(input())
    a = list(map(int, input().split()))

    ans = True
    for i in range(n):
        if a[i]%2 == 0:
            if a[i]%3!=0 and a[i]%5!=0 :
                ans = False
                break
    print("APPROVED" if ans else "DENIED")


def C():
    from collections import defaultdict
    n = int(input())
    d = defaultdict(int)
    for i in range(n):
        s = input() 
        d[s] += 1

    p = []
    for key in d:
        p.append([d[key], key])
    p.sort(reverse=True)

    max_p = p[0][0]
    names = []
    for i in range(len(p)):
        if p[i][0] == max_p:
            names.append(p[i][1])
        else:
            break
    names.sort()
    for name in names:
        print(name)


# def D():

