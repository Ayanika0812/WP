class StringProcessor:
    def __init__(self):
        self.user_string = ""

    def get_String(self):
        self.user_string = input("Enter a string: ")

    def print_String(self):
        print(self.user_string.upper())

# Example usage
if __name__ == "__main__":

    # StringProcessor example
    processor = StringProcessor()
    processor.get_String()
    processor.print_String()



""" Enter a string: Hello wp lab
HELLO WP LAB"""