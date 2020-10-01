#REQIURED MODULES

import random
import string

#CODE FOR GENERATING PASSWORD

print("-------------------------------------")
print("WELCOME TO RANDOM PASSWORD GENERATOR")
print("        --------------             ")
print("MINIMUM LENGTH OF THE PASSWORD IS 8")
print("        --------------             ")
print("PRESS -1 FOR EXIT")
print("------------------------------------")
length = int(input("Enter the length of the password:"))

def get_random_alphanumeric_string(length):
    sample_characters = '+-/x=<>.`@&$#!%^*abcdefghijklmnoprqstuvwxyz1234567890'   #PASSWORD IS OF THIS CHARACTER RANGE
    result_str = ''.join((random.choice(sample_characters) for i in range(length)))
    print("Random specialcharacter String is:", result_str)

#CODE FOR RESTRICTION OF LENGTH

if(length>=8):
    get_random_alphanumeric_string(length)
    
elif(length> -1 and length<=8):
    print("The minimum length must be 8\nTry Again!")

elif(length==-1):
    exit()
