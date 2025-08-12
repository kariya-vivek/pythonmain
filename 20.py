t = (5, 1, 3, 3)
print(len(t))             # i) len()
print(t.count(3))         # ii) count()
print(t.index(1))         # iii) index()
print(sorted(t))          # iv) sorted()
print(min(t), max(t))     # v & vi
print(cmp := (1 if t > (1, 2) else -1))  # vii) cmp (manual comparison)
print(tuple(reversed(t))) # viii) reversed()
