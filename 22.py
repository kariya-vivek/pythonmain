s = {1, 2, 3}
s.add(4)
s.update([5, 6])
s2 = s.copy()
s.pop()
s.remove(2)
s.discard(10)
s.clear()
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
