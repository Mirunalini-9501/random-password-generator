# REQUIRED MODULES
import random
import string

# FUNCTION FOR GENERATING RANDOM PASSWORD
def get_random_alphanumeric_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    print("Random alphanumeric String is:", result_str)

# MAIN FUNCTION
print("---------------------------------------------------------")
print("Welcome to Random password generator!")
print("Enter length as -1 to exit")
print("---------------------------------------------------------")
while True:
    digits = int(input("\nEnter the length for the random password (Minimum of 8 digits): "))
    if digits>=8:
        get_random_alphanumeric_string(digits)
    elif digits>-1 and digits <8:
        print("\nMinimum number of length for password is 8. Please try again!")
    elif digits==-1:
        break


