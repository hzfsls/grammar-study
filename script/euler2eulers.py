with open("./data/euler.ped", "r") as f:
    content = f.read()
    assert content.count("problem ") == 50
    contents = content.split("problem ")
    for i in range(1, 51):
        s_i = "0"*(3-len(str(i))) + str(i)
        with open(f"./data/eulers/euler{s_i}.ped", "w") as f:
            f.write("problem " + contents[i].strip())