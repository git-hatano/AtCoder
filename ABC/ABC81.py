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
    from collections import Counter
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    counter = Counter(a)
    b = []
    for key in counter.keys():
        b.append([counter[key], key])
    b.sort()

    ans = 0
    m = len(b)
    for i in range(len(b)):
        if m>k:
            ans += b[i][0]
            m -= 1
        else:
            break
    print(ans)



# def D():

