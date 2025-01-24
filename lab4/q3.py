# Function to sort words alphabetically
def sort_words_alphabetically(sentence):
    words = sentence.split()  # Split the sentence into words
    words.sort()  # Sort the words alphabetically
    return words

# Taking input from the user
sentence = input("Enter a sentence: ")

# Sorting words
sorted_words = sort_words_alphabetically(sentence)

# Displaying sorted words
print("Sorted words in alphabetical order:")
print(" ".join(sorted_words))






""" Enter a sentence: banana apple mango orange grape
Sorted words in alphabetical order:
apple banana grape mango orange
"""