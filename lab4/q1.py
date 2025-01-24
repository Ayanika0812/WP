def reverse_file_content(input_file, output_file):
    try:
        # Read content from the input file
        with open(input_file, 'r') as infile:
            content = infile.read()
        
        # Reverse the content
        reversed_content = content[::-1]
        
        # Write reversed content to the output file
        with open(output_file, 'w') as outfile:
            outfile.write(reversed_content)

        print(f"Content reversed and saved to '{output_file}' successfully.")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_file = 'q1in.txt'
output_file = 'output.txt'
reverse_file_content(input_file, output_file)



""" Content reversed and saved to 'output.txt' successfully.
"""