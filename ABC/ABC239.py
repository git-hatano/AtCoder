
from cmath import sqrt


def A():
    import math
    h = int(input())
    horizon = math.sqrt(h * (12800000 + h))
    print(horizon)


def B():
    x = int(input())
    div = x//10
    print(div)


def C():
    x1, y1, x2, y2 = map(int, input().split())

    v = [
        [2, 1], [1, 2], [-1, 2], [-2, 1],
        [-2, -1], [-1, -2],[1, -2], [2, -1],
    ]

    point1 = []
    point2 = []
    for i in range(len(v)):
        point1.append([x1+v[i][0], y1+v[i][1]])
        point2.append([x2+v[i][0], y2+v[i][1]])

    ans = False
    for i in range(len(v)):
        if point1[i] in point2:
            ans = True

    if ans:
        print("Yes")
    else:
        print("No")


# 素数を計算
def prime(N):
    primes = []
    for i in range(2, N + 1):
        primes.append(i)
        for p in range(2, i):
            if i % p == 0:
                primes.remove(i)
                break
    return primes


a, b, c, d = map(int, input().split())
prime = prime(200)

nums = []
for i in range(a, b+1):
    buf = []
    for j in range(c, d+1):
        buf.append(i+j)
    nums.append(buf)

for i in range(len(nums)):
    can = True
    for j in range(len(nums[0])):
        if nums[i][j] in prime: 
            can = False
            break
    if can:
        break

if can:
    print("Takahashi")
else:
    print("Aoki")


