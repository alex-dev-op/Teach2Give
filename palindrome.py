# Write a Python function that checks whether a word or phrase is palindrome or
# not.
# Note: A palindrome is word, phrase, or sequence that reads the same
# backward as forward, e.g., madam,kayak,racecar, or a phrase "nurses run"

def check_palindrome():
    
    # Get input 
    user_input = input("Enter a word or phrase to check if it is palindrome: ")
    
    # Remove spaces and convert to lowercase
    cleaned_text = ''.join(char.lower() for char in user_input if char.isalnum())
    
    if cleaned_text == cleaned_text[::-1]:
        print(f"'{user_input}' IS palindrome!")
    else:
        print(f"'{user_input}' is NOT a palindrome.")

check_palindrome()


# test
# ┌──(alex-dev-op㉿kali)-[~/technical]
# └─$ python palindrome.py 
# Enter a word or phrase to check if it is palindrome: a man
# 'a man' is NOT a palindrome.