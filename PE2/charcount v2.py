from os import strerror

counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
file_name = input("Enter the name of the file to analyze: ")
try:
    f = open(file_name, "rt")
    for line in f:
        for char in line:
            if char.isalpha():
                counters[char.lower()] += 1
    f.close()
    f = open(file_name + '.hist', 'wt')
    for char in sorted(counters.keys(), key=lambda x: counters[x], reverse=True):
        cnt = counters[char]
        if cnt > 0:
            f.write(char + ' -> ' + str(cnt) + '\n')
    f.close()
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
