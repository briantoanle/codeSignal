from collections import Counter
from statistics import mean
a = [[3, 3, 4, 2],
     [4, 4],
     [4, 0, 3, 3],
     [2, 3],
     [3, 3, 3],
    [1,2,3,4,7],
    [9],[13],[14]]
b=[]
c = []

x = list(mean(i) for i in a)

y = x.copy()

for i in y:
  if y.count(i)>1:
    y.pop(i)

for i in y:
  c.append([j for j, k in enumerate(x) if k == i])

print(c)