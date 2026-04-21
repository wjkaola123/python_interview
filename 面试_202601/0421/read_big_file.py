def read_file():
    with open(".\demo.txt", "r", encoding="utf-8") as f:
        # f.readlines() # 一行一行读

        while True:
            buffer = f.read(20)
            yield buffer

            if not buffer:
                break


# test
buffer = read_file()
for c in buffer:
    print(c)
