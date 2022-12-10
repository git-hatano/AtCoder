# AtCoder
勉強用のリポジトリ

## memo
* Python3よりも、PyPy3の方が速い
* numpyはできるだけ使わない
  * PyPyでは使えない（行列演算は楽だからOK）
  * PandasはそもそもAtcoderでは使えない

* 解けない問題にあたった時、具体例を考えてみる
* 時間がかかってもいいから
  * 紙に書いてみる
  * コメントアウトを書く
* 下手に綺麗に解こうとしなくて良い
  * 手が動かなくなる

* 制限時間で処理できる計算量は、10^8
  * TLEが出たときは、この計算量を超えている 
* TLEになってからが勝負
  * ソートして解決できないか
  * 探索範囲を狭められないか
  * DPに置き換えられないか

* 選ぶ/選ばない の問題は、全bit探索 or nCkの組み合わせで解く
* list よりも set の方が中身の探索が速い

* "答えは非常に大きくなる可能性があるので、xで割った余りを求めてください。"  という問題で、計算量的には大丈夫そうなのにTLEが出たとき
  * xで割った余りを格納してみる

* クエリ問題の対処パターン
  * 各クエリについて高速に計算
  * 全部前計算してしまう
  * 差分を計算することで高速に計算


## 入力と初期化
### 入力
```python
# 文字列を受け取る場合
s = input() 

# 1つの整数を入力
n = int(input())

# 複数の整数を入力
a, b = map(int, input().split())

# listで入力を受け取り
a = list(map(int, input().split()))

# 2次元listで入力を受け取り
h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
```

### 配列の初期化
```python
# 1次元配列 n
arr = [0]*(n)
# 2次元配列 n*m
arr = [[0]*(m) for i in range(n)]
```


## リスト、ソート関係
### 文字列の反転
```python
rev_s = s[::-1]
```

### リストの反転
sort のように2パターンの書き方 ([参照元](https://note.nkmk.me/python-reverse-reversed/))
```python
a.reverse()
rev_a = reversed(a)
```

### リストの要素を文字列に変換
文字列の連結は遅いので、リストで保持して最後にまとめて連結する
```python
#空白区切りの例
ans = " ".join([str(x) for x in a])
```

### リストから末尾の要素を消したいとき
listのスライシングで消すのは遅いので、delで対応
```python
#後ろから3要素消える
buf = buf[:-3]#遅い
del buf[-3:]#速い
```

### リストの先頭要素を操作したいとき
deque を使う ([参照元](https://x1.inkenkun.com/archives/944))
```python
# ABC158 D
from collections import deque
x = deque([])
#先頭に追加: O(1)
x.appendleft(a)
#1番後ろに挿入: O(1)
x.append(a)
#先頭を削除: O(1)
x.popleft()
```

### 毎回ソートをしなくても、小さい順に要素を取り出したいとき
優先度付きキューを使う
```python
import heapq
que = [2, 1, 3]
heapq.heapify(que)
# pop 最小値が取り出せる
minima = heapq.heappop(que)
# push
heapq.heappush(que, minima)
```

### 値に優先順位をつけてキーをソートする方法 
keyを上手く設定すれば色々と応用できるはず ([参照元](https://qiita.com/naritai_geek/items/495086bfb6dbce8a39ef))
```python
# ABC222 C
# 1列目を降順にソートして、1列目が同じ値の場合、0列目は昇順にする例
"""
a = [[0,0], [1,1], [2,1], [3,0]]
↓
a = [[1,1], [2,1], [0,0], [3,0]]
"""
a = sorted(a, key=lambda x: (x[1], -x[0]), reverse=True)
```

### 2次元のリストを次元ごとの小さい順に並べたいとき
普通にソートすれば良い
```python
"""
こういう配列に並べ替えたい
x = [
 [1, 2, 5],
 [1, 3, 4],
 [2, 3, 4],
 [3, 4, 5],
]
"""
x = sorted(x)
```

### 2次元配列を時計回りに90deg回転
引数に2次元のリストを渡す
```python
# ABC218 C
def rot(s):
    return list(zip(*s[::-1]))
```


## itertools
### リストから組み合わせ、順列を生成 
全bit探索をしなくてもいい ([参照元](https://note.nkmk.me/python-math-factorial-permutations-combinations/))
```python
a = range(10)
n = 2
# aから2つ選ぶ組み合わせを作る
from itertools import combinations
for c in combinations(a, n):
    print(c) 

# aから2つ選ぶ順列を作る
from itertools import permutations
for p in permutations(a, n):
    print(p) 
```

### 区間和に関する問題
ひとまず累積和を考える
```python
# リストaの累積和
from itertools import accumulate
s = [0] + list(accumulate(a))
```


## collections
### 連想配列（辞書型）の初期化を省略する
defaultdict を使うと存在していないkeyが入ったとき、指定した値で初期化してくれる
```python
from collections import defaultdict
d = defaultdict(int)
d[key] += 1
```

### リストの各要素の出現個数をカウントしたいとき
辞書型でもできるけどこっちの方が楽そう
```python
# ABC210 C 尺取法の実装に利用した例
from collections import Counter
counter = Counter(a[:k])
```


## 二分探索
予め探索するリストのソートが必須
### リストの中から、xよりも値が大きな要素の個数を求める
```python
from bisect import bisect_left
a = sorted(a) #予めソートが必須
less_than_x_count = bisect_left(a, x)
ans = len(a) - less_than_x_count
```

### リストの中にlからrの数は何個あるか
```python
# ABC248 C
from bisect import bisect_left, bisect_right
a = sorted(a) #予めソートが必須
st = bisect_left(a, l) #l以上の数が初めて現れる場所
gl = bisect_right(a, r) #rより大きい数が初めて現れる場所
ans = gl - st
```


## Tips

### 再帰関数の上限を変更
大きくしすぎるとエラーが出るので注意
```python
#再帰関数の場合は、Python3の方が速そう
import sys
sys.setrecursionlimit(10**6)
```

### 最小公倍数
([参照元](https://note.nkmk.me/python-gcd-lcm/))
```python
import math
def lcm(x, y):
    return (x * y) // math.gcd(x, y)
```

### 素数判定
引数nが素数ならTrueを返す
```python
import math
def is_prime(n):
    if n == 1: 
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
```

### 素因数分解
2以上の整数n => [[素因数, 指数], ...]の2次元リストを返す ([参照元](https://qiita.com/snow67675476/items/e87ddb9285e27ea555f8))
```python
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
    if temp!=1:
        arr.append([temp, 1])
    if arr==[]:
        arr.append([n, 1])
    return arr
```
1次元に変換
```python
def factorization_1d(n):
    facts = factorization(n)
    nums = []
    for f in facts:
        for i in range(f[1]):
            nums.append(f[0])
    return nums
```

### 組み合わせの総数を算出 
nCr の結果を返す ([参照元](https://note.nkmk.me/python-math-factorial-permutations-combinations/))
```python
import math
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
```

### popcount
二進数表記した時の1の個数
```python
def popcount(n):
    return bin(n).count("1")
```

###  2つの閉区間 [a,b],[c,d] が共通部分を持つかの判定
開区間で与えられたら、閉区間に変換して当てはめる
```python
# ABC207 C
max(a,c) <= min(b,d)
```

### 対角線で分けて、上側（下側）三角だけ探索したいとき
```python
a = [
 ['-', 'W', 'W', 'W'],
 ['L', '-', 'D', 'D'],
 ['L', 'D', '-', 'W'],
 ['L', 'D', 'W', '-']
]
#例として、転置成分が同じ値かを確認する処理
ans = True
for i in range(n):
    for j in range(i+1, n):
        if a[i][j] == a[j][i]:
            ans = False
```

### 回転行列
角度tは反時計回りが正
```python
#ABC168 C
import numpy as np
def rotation(u, t, deg=True):
    if deg:
        t = np.deg2rad(t)
    R = np.array([[np.cos(t), -np.sin(t)], [np.sin(t),  np.cos(t)]])
    return  np.dot(R, u)
```

### 10進数の数字を26進数（アルファベット）に変換
再帰を使うことで進数変換ができる
```python
# ABC171 C
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

ans = num2alpha(27) #aa
```
