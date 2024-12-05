# Write a program that accepts a string as input, capitalizes the first letter of each
# word in the string, and then returns the result string.
# Examples:
# "hi"=> returns "Hi"
# "i love programming"=> returns "I Love Programming"


def capitalize_words(input_string):
    
    # Split into words, capitalize join back
    return ' '.join(word.capitalize() for word in input_string.split())

def main():
    while True:
        # Prompt
        user_input = input("type something in lower case (or 'q' to quit): ")
        
        # Option to quit
        if user_input.lower() == 'q':
            break
        
        # Capitalize and display the result
        result = capitalize_words(user_input)
        print(f"Capitalized string: {result}")

# Run the program
if __name__ == "__main__":
    main()