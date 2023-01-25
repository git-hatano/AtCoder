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



"""
累積和の応用
"""
def C():
    n = int(input())
    s = input()
    #自分より前にあるWの数と、自分より後にあるのEの数を予め計算
    num_e = [0]*(n+1)
    num_w = [0]*(n+1)
    num_e[0] = s.count("E")
    for i in range(n):
        if s[i]=="E":
            num_e[i+1] = num_e[i]-1
            num_w[i+1] = num_w[i]
        elif s[i]=="W":
            num_e[i+1] = num_e[i]
            num_w[i+1] = num_w[i]+1
    #コストが最小になるところを探す
    ans = 10**9
    for i in range(n):
        cost = 0
        #自分より前にあるWの数
        if 0 < i:
            cost += num_w[i]
        #自分より後にあるのEの数
        if i < n-1:
            cost += num_e[i+1]
        ans = min(ans, cost)
    print(ans)


# def D():

