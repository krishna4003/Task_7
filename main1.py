data = {
    "students": [
        {"name": "Alice", "scores": {"math": 90, "science": 85}},
        {"name": "Bob", "scores": {"math": 75, "science": 95}},
        {"name": "Charlie", "scores": {"math": 88, "science": 92}}
    ],
    "classes": {"classA": ["Alice", "Bob"], "classB": ["Charlie"]}
}


def access(d, path, create=False):
    """Navigate to the parent of the target in the path."""
    keys = path.split(".")
    for k in keys[:-1]:
        k = int(k) if k.isdigit() else k
        if create and k not in d:
            d[k] = {}
        d = d[k]
    return d, keys[-1]

while True:
    cmd = input("\nEnter command (get/set/del/list/exit): ").split()
    if not cmd: continue
    op = cmd[0]
    if op == "exit": break
    path = cmd[1]
    try:
        parent, key = access(data, path)
        key = int(key) if key.isdigit() else key

        if op == "get":
            print(parent[key])
        elif op == "set":
            val = cmd[2]
            val = int(val) if val.isdigit() else val
            parent[key] = val
        elif op == "del":
            del parent[key]
        elif op == "list":
            target = parent[key] if key in parent else parent
            if isinstance(target, dict): print(list(target.keys()))
            elif isinstance(target, (list, tuple)): print(list(range(len(target))))
            elif isinstance(target, set): print(list(target))
            else: print(target)
        else:
            print("Unknown command")
    except Exception as e:
        print("Error:", e)


 