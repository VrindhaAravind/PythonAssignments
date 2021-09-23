file = open("demo", "r")

lines = 0
words = 0
characters = 0

for line in file:
  line = line.strip("\n")
  word = line.split()


  lines += 1
  words += len(word)
  characters += len(line)


print(" Total number of lines:", lines, ", total words: ", words, " and total characters: ", characters)