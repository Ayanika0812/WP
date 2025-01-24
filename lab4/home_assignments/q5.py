class StringReverser:
    def __init__(self, input_string):
        self.input_string = input_string

    def reverse_words(self):
        # Split the input string into words
        words = self.input_string.split()
        
        # Reverse the list of words
        reversed_words = words[::-1]
        
        # Join the words back into a single string with spaces
        return ' '.join(reversed_words)

# Example usage
if __name__ == "__main__":
    input_string = input("Enter a string: ")
    reverser = StringReverser(input_string)
    reversed_string = reverser.reverse_words()
    print("Reversed string word by word:")
    print(reversed_string)


"""Enter a string: Hello World !
Reversed string word by word:
! World Hello"""