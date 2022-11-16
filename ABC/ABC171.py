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
def C():
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


"""
計算量が軽いの知らなかった
    O(1): key in dic.keys()
https://qiita.com/bee2/items/4ab87d05cc03d53e19f9
"""
def D():
    from collections import Counter
    n = int(input())
    a = list(map(int, input().split()))

    sum_a = sum(a)
    counter_a = Counter(a)

    q = int(input())
    for i in range(q):
        b, c = map(int, input().split())
        
        if b in counter_a.keys():
            cnt = counter_a[b]
            sum_a += (c-b)*cnt
            
            if c in counter_a.keys():
                counter_a[c] += counter_a[b]
            else:
                counter_a[c] = counter_a[b]
            del counter_a[b]
            
        print(sum_a)
