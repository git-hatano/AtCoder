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
    if a>0 and b==0:
        print("Gold")
    elif a==0 and b>0:
        print("Silver")
    else:
        print("Alloy")


def B():
    k = [int(x) for x in input()]

    ans = True
    if len(set(k))==1:
        ans = False
    elif (k[0]+1)%10==k[1] and (k[1]+1)%10==k[2] and (k[2]+1)%10==k[3]:
        ans = False
            
    print("Strong" if ans else "Weak")


# def C():


# def D():

