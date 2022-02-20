file = open("pelican.txt", "r")
# Type of contents not file
print(type(file))

file_list = file.readlines()
print("There are", len(file_list), "lines in this list")

for line in file_list:
    print(line.strip())

file.close()