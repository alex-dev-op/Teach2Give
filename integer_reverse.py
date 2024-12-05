# Write a program that takes an integer as input and returns an integer with
# reversed digit ordering.
# Examples:
# For input 500, the program should return 5.
# For input -56, the program should return -65.
# For input -90, the program should return -9.
# For input 91, the program should return 19.


def reverse_integer(num):
    sign = -1 if num < 0 else 1
    
    # Convert to positive then to string which is simpler for reversal
    reversed_str = str(abs(num))[::-1]
    
    # Convert back to integer and apply the original sign
    return sign * int(reversed_str)

def main():
    while True:
        try:
            # Prompt
            user_input = input("Enter an integer to reverse (or 'q' to quit): ")
            
            if user_input.lower() == 'q':
                break
            
            # Convert input to integer and reverse
            number = int(user_input)
            result = reverse_integer(number)
            
            print(f"Reversed integer: {result}")
        
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    # start
    main()