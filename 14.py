with open("file.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip()[::-1])
