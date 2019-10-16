import os

map = []

for current_dir, dirs, files in os.walk("main"):
    if len(files) != 0:
        for it in files:
            if len(it) < 4 or it[-3:] != ".py":
                continue
            else:
                if current_dir not in map:
                    map.append(current_dir)

    # print(current_dir, dirs, files)
map.sort()
with open("out.txt", "w") as file:
    for item in map:
        file.write("%s\n" % item)
