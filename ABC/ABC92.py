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
    n = int(input())
    a = list(map(int, input().split()))
    sort_a = sorted(a)
    for i in range(n):
        if a[i]==sort_a[0]:
            l = sort_a[1]
        else:
            l = sort_a[0]
        
        if a[i]==sort_a[-1]:
            r = sort_a[-2]
        else:
            r = sort_a[-1]
            
        if l*r>0:
            ans = max(abs(l), abs(r))*2
        else:
            ans = abs(l-r)*2
        print(ans)


def C():
    n = int(input())
    a = list(map(int, input().split()))
    a = [0] +a
    #全部回った時のコスト
    cost = []
    for i in range(n):
        cost.append(abs(a[i]-a[i+1]))
    cost.append(abs(a[n]-0))
    sum_cost = sum(cost)

    for i in range(n):
        #省いた場所に関連するコストを引く
        ans = sum_cost -cost[i] -cost[i+1]
        #省いた場所の前後を直で飛んだ時のコストを足す
        ans += abs(a[i%(n+1)] - a[(i+2)%(n+1)])
        print(ans)

