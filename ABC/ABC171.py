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
    s = input()
    if s.islower():
        print("a")
    else:
        print("A")


def B():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    p.sort()

    ans = 0
    for i in range(k):
        ans += p[i]
    print(ans)


"""
数値→アルファベット
https://tanuhack.com/num2alpha-alpha2num/
"""
# def C():
def num2alpha(num, islower=True):
    if islower:
        ascii_start = 97 #a
    else:
        ascii_start = 64 #A

    if num<=26:
        return chr(ascii_start-1+num)
    elif num%26==0:
        return num2alpha(num//26-1)+chr(ascii_start+26-1)
    else:
        return num2alpha(num//26)+chr(ascii_start-1+num%26)

n = int(input())
ans = num2alpha(n)
print(ans)


# def D():

