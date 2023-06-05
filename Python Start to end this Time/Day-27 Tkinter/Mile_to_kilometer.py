from tkinter import *


def calculate_miles():
    miles = int(entry.get())
    kilos = round(miles * 1.6)
    kilos = str(kilos)
    label4.config(text=kilos)


window = Tk()
window.minsize(400, 130)
window.title('Mile to Kilometer Project')
window.config(padx=70, pady=20)

entry = Entry()
entry.grid(row=50, column=50)


label = Label(text='Miles')
label.grid(row=50, column=60)
# label.config(padx=0, pady=50)


label_2 = Label(text='is equal to')
label_2.grid(row=60, column=20)
# label_2.config(padx=60, pady=0)


label3 = Label(text='KM')
label3.grid(row=60, column=60)
# label3.config(padx=20, pady=50)


label4 = Label(text='0')
label4.grid(row=60, column=50)
# label3.config(padx=20, pady=50)


button = Button(text='Calculate', command=calculate_miles)
button.grid(row=80, column=50)


















window.mainloop()