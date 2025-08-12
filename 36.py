items = [10, 20, 30, 40, 50, 60, 70]
filtered = [items[i] for i in range(len(items)) if i not in (0, 2, 3, 5)]
print(filtered)
