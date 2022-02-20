file = open("pelican.txt", "w")
file.write("A wonderful bird is the pelican, \n")
file.write("His bill holds more than his belican, \n")

lines = ["He can take in his beak,\n", "Enough food for a week,\n",
"But I’m damned if I see how the helican.\n"]

file.writelines(lines)

file = open("pelican.txt", "r")
print(file.read())
file.close()

