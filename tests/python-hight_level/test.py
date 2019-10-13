q = int(input())
map = {}
for i in range(q):
    buffer = input()
    if ":" in buffer:
        f, s = buffer.split(":")
    else:
        f = buffer
        s = "object"
    f = f.strip()
    s = s.strip().split()

    map[f] = s

    for key, value in map.items():
        for it in s:
            if it == key:
                s+=map[it]


q = int(input())
for i in range(q):
    f, s = input().split()
    if s == f:
        print("Yes")
    if f in map[s]:
        print("Yes")
    else:
        print("No")

print(map)
