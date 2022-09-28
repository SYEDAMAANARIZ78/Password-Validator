from tkinter import *
import bcrypt


def validate(password):
    hash = b'$2b$12$N3ILXhwxfhqDkfv9r6.NmuBOmoQT9xnqsneGGMHDgCLH4WP8o0.SO'
    password = bytes(password, encoding='utf-8')

    if bcrypt.checkpw(password,hash):
       print('Login successful')
    else:
       print('Invalid Password')
       
root =Tk()
root.geometry("300x300")

password_entry = Entry(root)
password_entry.pack()

button = Button(text = 'Validate', command=lambda: validate(password_entry.get()))
button.pack()
root.mainloop()
