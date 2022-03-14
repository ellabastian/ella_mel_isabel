filename = "pelican.txt"
errmsg = ""
file = ""

try:
    file = open(filename, "r")

except FileNotFoundError:
    errmsg = filename + " not found"
except(TypeError, ValueError):
    errmsg = "Invalid filename"

if errmsg != "":
    exit(errmsg)

# Type of contents not file
print(type(file))

file_list = file.readlines()
print("There are", len(file_list), "lines in this list")

for line in file_list:
    print(line.strip())

file.close()