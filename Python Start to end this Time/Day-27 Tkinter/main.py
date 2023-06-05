from tkinter import Tk, Label, Button, Entry


# Button
def button_clicked():
    # Label()
    label.config(text=inputt.get(), font=('Times new roman', 24, 'bold'))


window = Tk()
window.title('My first GUI Program')

window.minsize(500, 300)

# Label
label = Label(text='I am a label', font=('Times new roman', 24, 'bold'))
# label.pack(side='top', expand=True)
label.grid(row=0, column=0)


# Button
button = Button(background='gray', text='Button', command=button_clicked)
# button.pack(side='bottom', expand=True)
button.grid(row=1, column=1)


# Button
new_button = Button(background='sky blue', text='New Button', command=button_clicked)
# button.pack(side='bottom', expand=True)
new_button.grid(row=0, column=2)


# Entry
inputt = Entry(width=10)
# inputt.pack()
inputt.grid(row=2, column=3)



























window.mainloop()
