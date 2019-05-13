for line in open("example.txt"):
    for word in line.split():
        if word.endswith("er"):
            print(f"{word}")
