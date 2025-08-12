d = {"name": "Alice", "age": 25}
print(d["name"])             # i) dict access
print(len(d))                # ii) len()
d.clear()                    # iii) clear()
d = {"name": "Alice", "age": 25}
print(d.get("age"))          # iv) get()
print(d.pop("age"))          # v) pop()
d = {"name": "Alice", "age": 25}
print(d.popitem())           # vi) popitem()
print(d.keys())              # vii) keys()
print(d.values())            # viii) values()
print(d.items())             # ix) items()
d2 = d.copy()                # x) copy()
d.update({"gender": "F"})    # xi) update()
