file = open("passage.txt", "r")
data = file.read()
number_of_characters = len(data)
number_of_words = data.split()
print('Number of characters in text file :', number_of_characters)
print('Number of words in text file :', len(number_of_words))


