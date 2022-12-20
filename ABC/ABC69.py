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
    a = [x%4 for x in a]
    counter = Counter(a)

    ans = False
    if counter[0]>=n//2:
        ans = True
    else:
        if counter[2]%2==0:
            n -= counter[2]
        else:
            n -= counter[2]-1
        
        if n==0:
            ans = True
        elif n==1 and counter[0]==1:
            ans = True
        elif counter[0]>=n//2:
            ans = True
    print("Yes" if ans else "No")


# def D():

