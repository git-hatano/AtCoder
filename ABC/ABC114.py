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



def B():
    s = input()
    n = len(s)
    ans = float("inf")
    for i in range(n-2):
        ans = min(ans, abs(753-int(s[i:i+3])))
    print(ans)


def C():
    from itertools import product
    n = int(input())
    ans = []
    if n>=357:
        ans.append(357)
        s = ["3", "5", "7"]
        for seq in product(range(4), repeat=11):
            tmp = []
            for i in seq:
                if i>0:
                    tmp.append(s[i-1])
            if len(set(tmp))==3:
                tmp = int("".join(tmp))
                if tmp <= n:
                    if ans[-1] < tmp:
                        ans.append(tmp)
                else:
                    break
    print(len(ans))



# def D():

