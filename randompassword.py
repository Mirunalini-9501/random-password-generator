# REQUIRED MODULES
import random
import string
from tkinter import *

# FUNCTION FOR GENERATING RANDOM PASSWORD
def pass_generator(length):
    char_set = string.ascii_letters + string.digits + "+-*/!~@#$%^&_?"
    result = ''.join((random.choice(char_set) for i in range(length)))
    return result
    
# MAIN FUNCTION
root = Tk()
root.title("Random Password Generator")
txt1 = Label(root,text = "Welcome to Random password generator!").grid(row=0,column=0)
txt2 = Label(root,text = "Enter the length for the random password (Minimum of 8 digits)").grid(row=1,column=0)
length = Entry(root).pack()
length.bind("<Return>",lambda a:pass_generator(length.get()))
length.focus()
#print("---------------------------------------------------------")
#print("Welcome to Random password generator!")
#print("Enter length as -1 to exit")
#print("---------------------------------------------------------")
#while True:
    #digits = int(input("\nEnter the length for the random password (Minimum of 8 digits): "))
  #  if length>=8:
   #     print("\nGenerated Random password is:",pass_generator(digits))
    #elif length!=-1 and length<8:
     #   print("\nMinimum number of length for password is 8. Please try again!")
    #elif length==-1:
     #   break

root.mainloop()
