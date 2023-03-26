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
    # Let's output the counters.
    for char in counters.keys():
        cnt = counters[char]
        if cnt > 0:
            print(char, '->',cnt)
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
