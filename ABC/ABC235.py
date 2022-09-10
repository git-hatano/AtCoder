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
if ans:
    print("Yes")
else:
    print("No")
'''

def A():
    s = input()
    ans = int(s) + int(s[1]+s[2]+s[0]) + int(s[2]+s[0]+s[1])
    print(ans)

def B():
    n = int(input())
    h = list(map(int, input().split()))

    now_h = h[0]
    for i in range(n-1):
        if now_h < h[i+1]:
            now_h = h[i+1]
        else:
            break
    print(now_h)


# def C():
n ,q = map(int, input().split())
a = list(map(int, input().split()))

numbers = {}
for i in range(n):
    if a[i] not in numbers:
        numbers[a[i]] = [i+1]
    else:
        numbers[a[i]].append(i+1)

for i in range(q):
    x, k = map(int, input().split())

    if x in numbers and len(numbers[x])>=k:
        print(numbers[x][k-1])
    else:
        print(-1)



# def D():

