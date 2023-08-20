# This function returns the entirety of "Dracula" as a string
def readBook():
  f = open("dracula.txt", "r")
  s = f.read().replace("-", " ")
  f.close()
  return ''.join(c for c in s if c.isalnum() or c == " ")

draculaText = readBook()


# Remove/strip additional punctuations fron draculaText string
for char in '.,\n':
  draculaText = draculaText.replace(char, ' ')

# Take a string convert to lower case and split each word in string with a space as delimiter using split() function
words = draculaText.lower().split()

# Define variables and a Dictionary
word = ""
numberOfTimes = 0
wordAndCount = {}

# Count and save in the Dictionary the number of each word contained in the string and associate count with the corresponding key in the Dictionary
for word in words:
  if word in wordAndCount:
    wordAndCount[word] += 1
  else:
    wordAndCount[word] = 1

# Calculate how many four-letter words are there in the string/book
keyWord = ""
highestWordCount = 0
for key, value in wordAndCount.items():
  if(highestWordCount < value):
    highestWordCount = value
for key, value in wordAndCount.items():  
    if wordAndCount[key] == highestWordCount:
     print(f" '{key}' is the word that appears the most throughout the text file analyzed by this program; a total of {highestWordCount} times")

# Add two empty lines between print outs
print()
print()

# Calcule the word that shows up the most often in the string/book
fourLetterWordCount = 0
for key, value in wordAndCount.items():
  if(len(key) == 4):
    fourLetterWordCount += 1
print(f" There are {fourLetterWordCount} four letter words in the text file analyzed by this program")

# Add two empty lines between print outs
print()
print()

# Print every word in string/book that shows up at least five hundred times
print("The words below shows up at least five hundred or more times throughout the file analyzed by this program:")  
for key, value in wordAndCount.items():
  if(value > 500):
    print(f"{key} - {value}")