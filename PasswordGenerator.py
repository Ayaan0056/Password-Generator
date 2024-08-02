import random
from tkinter import *
import pyperclip 
import customtkinter as ct

ct.set_appearance_mode('dark')
ct.set_default_color_theme("dark-blue")



root = ct.CTk()
#root = Tk()
root.geometry("500x400")
root.title('Password Generator')
#root.configure(background='#856ff8')
password = ""



def generate(small,caps,spc,num,sym):
    global password
    
    len = int(e.get())
    
    alpha_small = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    alpha_caps = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    space = [' ']
    numbers = ['1','2','3','4','5','6','7','8','9','0']
    symbols = ["~","!","@","#","$","%","^","&","*","(",")","_","+","-","=","{","}","|","[","]","/","?","<",">"]

    pwdList = []
    copy = ''
    
    while(len>0):
        if len == 0:
            break
        if (small):
            if len == 0:
                break
            char = random.choice(alpha_small)
            pwdList.append(char)
            len = len - 1
        
        if (caps):
            if len == 0:
                break
            char = random.choice(alpha_caps)
            pwdList.append(char)
            len = len - 1

        if (spc):
            if len == 0:
                break
            char = random.choice(space)
            pwdList.append(char)
            len = len - 1
        
        if (num):
            if len == 0:
                break
            char = random.choice(numbers)
            pwdList.append(char)
            len = len - 1

        if (sym):
            if len == 0:
                break
            char = random.choice(symbols)
            pwdList.append(char)
            len = len - 1

    
    random.shuffle(pwdList)
    
    for i in pwdList:
        copy = copy + i
    
    pwdList = []
    password = copy
    copy = ''
    #output.insert(0,password)
    #print("Generated Password: ", password)
    
    return password

def display():
    pwd = generate(sml.get(),cpl.get(),spc.get(),n.get(),symb.get())
    print(pwd) 
    output.delete("0","end")
    output.insert(0,password)


def copyClipboard():
    pyperclip.copy(password)  

#label=ct.CTkLabel(root, text="Password Generator")
#label.pack()
label = ct.CTkLabel(root,text="Enter Length")
label.pack()

e = ct.CTkEntry(root,width=60, height=10, corner_radius = 10)
e.focus_set()
e.pack()

sml = IntVar()
cpl = IntVar()
spc = IntVar()
n = IntVar()
symb = IntVar()

letter_small = ct.CTkCheckBox(root, text='Include Small Letters', variable=sml).pack(pady = 5)
letter_caps = ct.CTkCheckBox(root, text='Include Capital Letters', variable=cpl).pack(pady = 5)
letter_space = ct.CTkCheckBox(root, text='Include Blank Space', variable=spc).pack(pady = 5)
letter_symbols = ct.CTkCheckBox(root, text='Include Symbols', variable=symb).pack(pady = 5)
letter_numbers = ct.CTkCheckBox(root, text='Include Numbers', variable=n).pack(pady = 5)

b = ct.CTkButton(root,text="Okay", command=display)
b.pack(pady = 5)

#b1 = Button(root,text='print',command=display)
#b1.pack()

output = ct.CTkEntry(root, width=200, height= 10, corner_radius=10)
output.pack(pady = 5)



b2 = ct.CTkButton(root,text="Copy to Clipboard",command=copyClipboard)
b2.pack(pady = 5)

root.mainloop()