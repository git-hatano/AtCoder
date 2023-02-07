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



def C_WA():
    x = int(input())
    x = abs(x)
    cur = 0
    for i in range(1, x+1):
        if cur+i <= x:
            cur += i
        else:
            cur -= i-1
            cur += i
        
        if cur==x:
            break
    print(i)


"""
うまいこと調整すればこのステップでいけるらしい
なぜ上手くいか分からん
"""
def C_ans():
    x = int(input())
    cur = 0
    for i in range(1, x+1):
        cur += i
        if cur>=x:
            break
    print(i)


# def D():

