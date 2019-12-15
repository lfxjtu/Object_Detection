path = "/Users/lfxjtu/Dropbox/Fang Liu/Python/"

file = "cars.txt"

with open(path + file) as f:
    first_line = f.readline()
    print(first_line)
    split_txt = first_line.split(":")
    print(split_txt)
