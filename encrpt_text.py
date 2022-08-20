
from cgitb import text
from operator import index
from secrets import choice
from tkinter.font import BOLD
from turtle import down, position
from numpy import insert
from pyparsing import alphanums
from pyrsistent import s
from tkinter import *
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def clears():

    enter_text.delete("1.0",END)
    output_text.delete("1.0",END)
    shift.set(0)





def get_shift():

    return shift.get()

def get_text():

    
    t1 =  enter_text.get("1.0",END)
    return t1
    
    
        


def encrpt(x):
    xxx =' '
    yyy = ' '
    global alphabet

    xyz = get_text()
    s = get_shift()
    print(xyz)

    s = s % 26

    if x == 2:

        s = -(s)


    
    for char in xyz:
        if char in alphabet:
            position = alphabet.index(char)
            change_position = position + s
            final_text = alphabet[change_position]
            xxx +=final_text
        else:
            xxx +=char
    
    for char in xxx:
        if char in alphabet:
            position = alphabet.index(char)
            change_position = position + s 
            final_text = alphabet[change_position]      # this second loop is used for enhancing security  and diversion for hackers
            yyy +=final_text
        else:
            yyy+=char
        

        
        
    output_text.insert(END,yyy)



fix_font = ("Arial" ,16 , BOLD)



win = Tk()
win.config(bg="#00254a")

win.geometry("600x570+300+50")

enter_text = Text(win, width=30,height=5,font=("Arial" ,16))


enter_text.place(x=100,y=50)



l1 = Label(win,text="Choose An Option ",font=fix_font,bg="#00254a")
encrptButton = Button(win,text="Encrption",font=fix_font,command=lambda x=1:encrpt(x))

decrptButton = Button(win,text="Decryption",font=fix_font,command=lambda x=2:encrpt(x))

shift = Scale(win,bg="white",font=fix_font,length=120,)
shift.place(x=470,y=50)


encrptButton.place(x=70,y=300)
decrptButton.place(x=370,y=300)
l1.place(x= 200,y=230)

output_text = Text(win, width=30,height=5,font=("Arial" ,16))
output_text.place(x=100,y=360)

clear = Button(win,text="Clear",width=27,font=fix_font,bg='yellow',command=clears)
clear.place(x= 100,y=500)











 







# def ceaser(start_text,shift_amount,direction):
    
#     xyz = ""

#     if direction == "decode":
#         shift_amount = -(shift_amount)
    

#     for char in start_text:

#         if char in alphabet:

#             position = alphabet.index(char)

#             new_position= position + shift_amount

#             xyz += alphabet[new_position]
#         else:
#             xyz +=char


        
    
#     return xyz






# run = True

# while run:



#     direction = input("Encode or Decode ")
#     text= input("Enter a text ")
#     shift =int(input("How many shifts "))



#     print(ceaser(text,shift,direction))

#     ask = input("Do you want to continue yes or no").lower()
#     if ask == 'no':
#         run = False






win.mainloop()

    

    








