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
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    ans = a*d -b*c
    print(ans)


def B():
    n, x = map(int, input().split())
    s = input() 

    for c in s:
        if c=="o":
            x += 1
        elif c=="x" and x>0:
            x -= 1
    print(x)


def area_check():
    import numpy as np
    arr = np.zeros((11, 11))
    a = 5
    b = 5
    for c in range(11):
        for d in range(11):
            if a+b == c+d:
                arr[c, d] = 1
            elif a-b == c-d:
                arr[c, d] = 2
            elif abs(a-c) + abs(b-d) <= 3:
                arr[c, d] = 3
    print(arr)


"""
初めに、
3手以内にどのマスでも到達できる
相対的な移動で考えれば良い
という２点を押さえないとできない
"""
def C_ans():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    #r1, c1を原点に: ここの考え方はOK
    r = r2-r1
    c = c2-c1
    #0
    if r==0 and c==0:
        ans = 0
    #1 問題文の条件
    elif r+c==0 or r-c==0: #対角線上
        ans = 1
    elif abs(r) +abs(c) <= 3: #近距離のエリア内
        ans = 1
    #2 考えて正しく条件作れないと厳しい
    elif (r+c)%2 == 0: #移動A+移動B
        ans = 2
    elif abs(r) + abs(c) <= 6: #移動C+移動C
        ans = 2
    elif abs(r+c)<=3 or abs(r-c)<=3: #移動A+移動C, 移動B+移動C
        ans = 2
    #3 どれにも当てはまらないなら3
    else:
        ans = 3
    print(ans)


# def D():

