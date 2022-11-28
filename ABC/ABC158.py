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
    s = set(list(input()))
    if len(list(s)) > 1:
        ans = True
    else:
        ans = False
    print("Yes" if ans else "No")


def B():
    n, a, b = map(int, input().split())
    brock_num = n // (a+b)
    ans = brock_num * a
    mod = n % (a+b)
    if mod >= a:
        ans += a
    else:
        ans += mod
    print(ans)


def C():
    a, b = map(int, input().split())
    ans = -1
    n = 10**4
    for i in range(1, n):
        tmp_a = int(i*8/100)
        tmp_b = int(i*10/100)
        if a==tmp_a and b==tmp_b:
            ans = i
            break
    print(ans)


def D():
    from collections import deque
    s = list(input())
    s = deque(s)
    flag_rev = False

    q = int(input())
    for i in range(q):
        query = input()
        t = int(query[0])
        
        if t==1:
            flag_rev = not flag_rev
        else:
            query = query.split()
            f = int(query[1])
            c = query[2]
            
            if f==1:
                if not flag_rev:
                    s.appendleft(c)
                else:
                    s.append(c)
            else:
                if not flag_rev:
                    s.append(c)
                else:
                    s.appendleft(c)
    s = list(s)
    if flag_rev:
        s = s[::-1]
    ans = "".join(s)
    print(ans)
