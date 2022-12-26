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
    n = int(input())
    a = list(map(int, input().split()))
    counter = Counter(a)

    ans = 0
    for key in counter:
        x = counter[key]-key
        #key個より大きいなら、key個に揃えるように消す
        if x>0:
            ans += x
        #key個未満なら、全て消してしまう
        elif x<0:
            ans += counter[key]
    print(ans)


# def D():

