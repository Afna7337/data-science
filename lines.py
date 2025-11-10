3. filename = input("Enter a file name: ")
with open(filename) as f:
    line_count = sum(1 for line in f)
print("Number of lines:", line_count)
