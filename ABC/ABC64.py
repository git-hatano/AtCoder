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



def C_ans():
    n = int(input())
    a = list(map(int, input().split()))
    s = set()
    over = 0
    for i in range(n):
        if 1<=a[i]<400:
            s.add("gray")
        elif 400<=a[i]<800:
            s.add("bronze")
        elif 800<=a[i]<1200:
            s.add("green")
        elif 1200<=a[i]<1600:
            s.add("lightblue")
        elif 1600<=a[i]<2000:
            s.add("blue")
        elif 2000<=a[i]<2400:
            s.add("yellow")
        elif 2400<=a[i]<2800:
            s.add("orange")
        elif 2800<=a[i]<3200:
            s.add("red")
        else:
            over += 1

    mi = max(len(s), 1)#####
    ma = len(s)+over
    print(f"{mi} {ma}")


# def D():

