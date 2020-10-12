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
    label = Label(root,text=str(result)).pack()
    f = open("storedpassword.txt","w")
    f.write(result)
    f.close()
    #print(result) prints the result in the output screen

# MAIN FUNCTION
root = Tk()
root.title("Random Password Generator")
txt1 = Label(root,text = "Welcome to Random password generator!").pack()
txt2 = Label(root,text = "Enter the length for the random password (Minimum of 8 digits)").pack()
length = Entry(root)
length.pack()

calc = Button(root,text = "Calculate",width=15,command = pass_generator)
calc.pack()


root.mainloop()
