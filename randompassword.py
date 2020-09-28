# REQUIRED MODULES
import random
import string

# FUNCTION FOR GENERATING RANDOM PASSWORD
def pass_generator(length):
    char_set = string.ascii_letters + string.digits + string.punctuation
    result = ''.join((random.choice(char_set) for i in range(length)))
    return result
    
# MAIN FUNCTION
print("---------------------------------------------------------")
print("Welcome to Random password generator!")
print("Enter length as -1 to exit")
print("---------------------------------------------------------")
while True:
    digits = int(input("\nEnter the length for the random password (Minimum of 8 digits): "))
    if digits>=8:
        print("\nGenerated Random password is:",pass_generator(digits))
    elif digits!=-1 and digits <8:
        print("\nMinimum number of length for password is 8. Please try again!")
    elif digits==-1:
        break


