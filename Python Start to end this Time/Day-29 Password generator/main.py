from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #
new_line = '\n'


def save_passwords():
    website = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="OOPS!", message="You should not let any field empty!")

    else:
        is_ok = messagebox.askokcancel(title="Confirm Details", message=f"Do you confirm these details \nWebsite: {website}"
                                                                        f" \nEmail: {email} \nPassword: {password}")

        if is_ok:
            f = open("passwords.txt", "a")
            f.write(f"{website} | {email} | {password} {new_line}")

            f.close()
    web_entry.delete(0, END)
    password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('My Password generator')
window.minsize(width=200, height=200)
window.config(padx=50, pady=50)

img = PhotoImage(file='logo.png')

canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

# Working with Labels
web_label = Label(text='Website')
web_label.grid(row=1, column=0)

email_label = Label(text='Email/Username')
email_label.grid(row=2, column=0)

password_label = Label(text='Password: ')
password_label.grid(row=3, column=0)

# Working with Entries
web_entry = Entry(width=39)
web_entry.grid(row=1, column=1, columnspan=2)
web_entry.focus()

email_entry = Entry(width=39)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "123@example.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Working with Buttons
password_button = Button(text="Generate Password")
password_button.grid(row=3, column=2)

add_button = Button(text='Add', width=33, command=save_passwords)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
