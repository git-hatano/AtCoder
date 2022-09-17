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

from tokenize import group


def A():
    a, b,c,d = map(int, input().split())
    print((a+b)*(c-d))
    print("Takahashi")

def B():
    s = []
    for i in range(10):
        s.append(input())

    r = []
    c = []
    for i in range(10):
        for j in range(10):
            if s[i][j]=="#":
                r.append(i)
                c.append(j)

    print(f"{min(r)+1} {max(r)+1}")
    print(f"{min(c)+1} {max(c)+1}")
            

def C():
    n = int(input())
    nb = bin(n)[2:]
    l = len(nb)

    a = []
    for i in range(l):
        if nb[i]=="1":
            if len(a)==0:
                a.append(0)
                a.append(2**(l-i-1))
            else:
                tmp = []
                for x in a:
                    tmp.append(x + 2**(l-i-1))
                a += tmp

    if len(a):
        a = sorted(a)
        for x in a:
            print(x)
    else:
        print(0)
    
    
def D():
    n = int(input())
    point = []
    group = []#group_id
    for i in range(n):
        group.append(i)
        point.append(list(map(int, input().split())))

    vec = [
        [-1,-1],[-1,0],
        [0,-1],[0,1],
        [1,0],[1,1],
    ]
    for i in range(n):
        for j in range(n):
            for v in vec:
                if point[i][0]+v[0]==point[j][0] and point[i][1]+v[1]==point[j][1]:
                    old = group[j]
                    group[j] = group[i]
                    
                    for g in range(len(group)):
                        if group[g]==old:
                            group[g] = group[i]

    print(len(set(group)))
