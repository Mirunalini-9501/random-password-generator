# REQUIRED MODULES
import random
import string
from tkinter import *
value = 0

# FUNCTION FOR GENERATING RANDOM PASSWORD
def pass_generator():
    global value 
    value = length.get()
    char_set = string.ascii_letters + string.digits + "+-*/!~@#$%^&_?"
    result = ''.join((random.choice(char_set) for i in range(int(value))))
    print(result)

# MAIN FUNCTION
root = Tk()
root.title("Random Password Generator")
txt1 = Label(root,text = "Welcome to Random password generator!").pack()
txt2 = Label(root,text = "Enter the length for the random password (Minimum of 8 digits)").pack()
length = Entry(root)
length.pack()

calc = Button(root,text = "Calculate",width=15,command = pass_generator)
calc.pack()
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
