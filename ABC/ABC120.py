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
    ans = min(b//a, c)
    print(ans)


def B():
    a, b, k = map(int, input().split())
    cnt = 0
    for i in reversed(range(1, 101)):
        if a%i==0 and b%i==0:
            cnt += 1
        if k==cnt:
            ans = i
            break
    print(ans)


def C_ans():
    from collections import Counter
    s = list(input())
    counter = Counter(s)
    ans = min(counter["0"], counter["1"])
    ans *= 2
    print(ans)


# def D():

