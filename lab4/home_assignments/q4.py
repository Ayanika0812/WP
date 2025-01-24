class ParenthesesValidator:
    def __init__(self, s):
        self.s = s

    def is_valid(self):
        stack = []
        # Create a mapping of closing brackets to opening ones
        bracket_map = {')': '(', '}': '{', ']': '['}

        # Traverse through the string
        for char in self.s:
            if char in bracket_map.values():  # If it's an opening bracket
                stack.append(char)
            elif char in bracket_map:  # If it's a closing bracket
                if stack and stack[-1] == bracket_map[char]:
                    stack.pop()  # Pop the matching opening bracket
                else:
                    return False  # If no match or stack is empty

        # If the stack is empty, all the brackets were matched properly
        return not stack

if __name__ == "__main__":
    s = input("Enter a string of parentheses: ")
    validator = ParenthesesValidator(s)
    if validator.is_valid():
        print("The parentheses are valid.")
    else:
        print("The parentheses are invalid.")


"""Enter a string of parentheses: Enter a string of parentheses: ({[()]})
The parentheses are valid."""