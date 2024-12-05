# Write a Python function to check whether a string is pangram or not. (Assume
# the string passed in does not have any punctuation)
# Note: Pangrams are words or sentences containing every letter of the
# alphabet at least once. For example: "The quick brown fox jumps over the
# lazy dog"

def is_pangram(sentence):
    unique_letters = set(char for char in sentence.lower() if char.isalpha())

    return len(unique_letters) == 26

def main():
    while True:
        # Prompt the user
        sentence = input("Enter a sentence to check (or 'q' to quit): ")
        if sentence.lower() == 'q':
            break

        # Check if the sentence is a pangram
        if is_pangram(sentence):
            print(f"'{sentence}' is a pangram!")
        else:
            print(f"'{sentence}' is not a pangram.")

if __name__ == "__main__":
    # start
    main()