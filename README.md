# AtCoder
勉強用のリポジトリ

## 📌超基本
* Python3よりも、PyPy3の方が速い
  * 再帰関数の場合は、Python3の方が速そう
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

## 💡Tips
* 選ぶ/選ばない の問題は、全bit探索 or nCkの組み合わせで解く
* list よりも set の方が中身の探索が速い
* "答えは非常に大きくなる可能性があるので、xで割った余りを求めてください。"  という問題で、計算量的には大丈夫そうなのにTLEが出たとき
  * xで割った余りを格納してみる


## 🍀ユースケース

### 基本的な入力
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

### 文字列、リストの反転
```python
rev_s = s[::-1]
```

### リストから先頭要素を削除したいとき
list.pop()は遅いので使わない
```python
from collections import deque
x = deque([])
x.append(n)
x.popleft()
```

### リストから末尾の要素を消したいとき
listのスライシングで消すのは遅いので、delで対応
```python
#後ろから3要素消える
buf = buf[:-3]#遅い
del buf[-3:]#速い
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


### 2次元のリストを次元ごとの小さい順に並べたいとき
普通にソートすれば良い
```python
"""
こういう配列に並べ替えたい
x = [
 [1, 2, 5],
 [1, 3, 4],
 [1, 3, 5],
 [2, 3, 4],
 [2, 3, 5],
 [3, 4, 5],
]
"""
x = sorted(x)
```

### リストから任意のn個の組み合わせを取り出したいとき
全bit探索をしなくてもいい

```python
# aから2つ選ぶ組み合わせを作る例
from itertools import combinations
a = range(10)
n = 2
for c in combinations(a, n):
    print(c) #t=(1,2)など
```

### 毎回ソートをしなくても、小さい順に要素を取り出したいとき
優先度付きキューを使う
```python
import heapq
que = [2, 1, 3]
heapq.heapify(que)
# pop
minima = heapq.heappop(que) #最小値が取り出せる
# push
heapq.heappush(que, minima)
```

### 連想配列（辞書型）の初期化を省略する
defaultdict を使うと、存在していないkeyが入ったとき、指定した値で初期化してくれる
```python
from collections import defaultdict
d = defaultdict(int)#0で初期化
d[key] += 1
```

### リストの中から、xよりも値が大きな要素の個数を求める
二分探索を使う
```python
a = sorted(a) #予めソートが必須

from bisect import bisect_left
less_than_x_count = bisect_left(a, x)
print(len(a) - less_than_x_count)
```

### 区間和に関する問題
ひとまず累積和を考える
```python
# リストaの累積和
from itertools import accumulate
s = [0] + list(accumulate(a))
```

### 値に優先順位をつけてキーをソートする方法 ([参照元](https://qiita.com/naritai_geek/items/495086bfb6dbce8a39ef))
keyを上手く設定すれば色々と応用できるはず
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

### リストの各要素の出現個数をカウントしたいとき
辞書型でもできるけどこっちの方が楽そう
```python
# ABC210 C
# 尺取法の実装に利用した例
from collections import Counter
counter = Counter(a[:k])

for i in range(k, n):
    left = c[i-k]
    right = c[i]
    counter[left] -= 1
    counter[right] += 1
    if counter[left]==0:
        del counter[left]
```

###  2つの閉区間 [a,b],[c,d] が共通部分を持つかの判定
開区間で与えられたら、閉区間に変換して当てはめる
```python
# ABC207 C
max(a,c) <= min(b,d)
```

