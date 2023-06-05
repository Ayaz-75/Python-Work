from tkinter import *
from tkcalendar import Calendar,DateEntry


def goto():
    from orignal_results import OriginalResults
    import orignal_results


class Results:
    PINK = "#e2979c"
    RED = "#e7305b"
    GREEN = "#9bdeac"
    YELLOW = "#f7f5dd"
    FONT_NAME = "Courier"


    window = Tk()
    window.title('Bug fixing Time Estimation')
    window.config(padx=80, pady=40, bg=YELLOW)
    title_label = Label(text="Bug fixing Time Estimation", fg='#0F3460', bg=YELLOW, font=(FONT_NAME, 20))
    title_label.grid(column=1, row=0)

    canvas = Canvas(width=400, height=270, bg=YELLOW, highlightthickness=0)
    bug_img = PhotoImage(file="bagu.png")
    canvas.create_image(200, 150, image=bug_img)
    canvas.grid(column=1, row=12)

    # Labels
    bug_id = Label(text="Bug ID:", bg=YELLOW)
    bug_id.grid(row=1, column=0)

    product_name = Label(text="Product Name", bg=YELLOW)
    product_name.grid(row=2, column=0)

    severity_category = Label(text="Severity Category", bg=YELLOW)
    severity_category.grid(row=3, column=0)

    status_category = Label(text="Status Category", bg=YELLOW)
    status_category.grid(row=4, column=0)

    qty_of_votes = Label(text="Qty Votes", bg=YELLOW)
    qty_of_votes.grid(row=5, column=0)

    qty_of_comments = Label(text="Qty comments", bg=YELLOW)
    qty_of_comments.grid(row=6, column=0)

    asignee_name = Label(text="Asignee Name", bg=YELLOW)
    asignee_name.grid(row=7, column=0)

    resolution_category = Label(text="Resolution Category", bg=YELLOW)
    resolution_category.grid(row=8, column=0)

    creation_date = Label(text="Creation Date", bg=YELLOW)
    creation_date.grid(row=9, column=0)

    update_date = Label(text="Update Date", bg=YELLOW)
    update_date.grid(row=10, column=0)

    # Entries
    bug_id_entry = Entry(width=35)
    bug_id_entry.grid(row=1, column=1, columnspan=3)

    product_entry = Entry(width=35)
    product_entry.grid(row=2, column=1, columnspan=3)

    severi_entry = Entry(width=35)
    severi_entry.grid(row=3, column=1, columnspan=3)

    status_entry = Entry(width=35)
    status_entry.grid(row=4, column=1, columnspan=3)

    qty_of_entry = Entry(width=35)
    qty_of_entry.grid(row=5, column=1, columnspan=3)

    qty_of_entry = Entry(width=35)
    qty_of_entry.grid(row=6, column=1, columnspan=3)

    asignee_entry = Entry(width=35)
    asignee_entry.grid(row=7, column=1, columnspan=3)

    resolution_entry = Entry(width=35)
    resolution_entry.grid(row=8, column=1, columnspan=3)

    creation_date_entry= DateEntry(window,width=30,bg="darkblue",fg="white",year=2022)
    creation_date_entry.grid(row=9, column=1)

    update_date = DateEntry(window,width=30,bg="darkblue",fg="white",year=2022)
    update_date.grid(row=10, column=1)


    # Buttons
    submit_button = Button(text="Submit", command=goto)
    submit_button.grid(row=11, column=1)


    window.mainloop()


result = Results()
