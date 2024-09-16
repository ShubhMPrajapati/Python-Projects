from random import *
from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]

    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_numbers + password_letter + password_symbols
    shuffle(password_list)

    passwords = "".join(password_list)

    password_input.delete(0, END)
    password_input.insert(0, passwords)


windows = Tk()
windows.title("Password Manager")
windows.config(pady=50, padx=50)


def add():
    get_website = website_input.get()
    get_email = email_input.get()
    get_password = password_input.get()

    if len(get_website) == 0 or len(get_password) == 0:
        messagebox.showinfo(title="Oops", message="Please dont leave any field empty")
    else:
        is_ok = messagebox.askokcancel(title=get_website,
                                       message=f"These are the details entered:\nEmail: {get_email}\n Password: "
                                               f"{get_password}\n IS IT CORRECT?")

        if is_ok:
            string = f"{get_website},{get_email},{get_password}"
            with open("data.txt", mode="a") as file:
                file.write(f"{string}\n")

            website_input.delete(0, END)
            password_input.delete(0, END)


canvas = Canvas(height=200, width=200, )
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

website = Label()
website.config(text="Website: ")
website.grid(row=1, column=0)

email = Label()
email.config(text="Email/Username: ")
email.grid(row=2, column=0)

password = Label()
password.config(text="Password: ")
password.grid(row=3, column=0)

website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "example@gmail.com")

password_input = Entry(width=26)
password_input.grid(row=3, column=1, columnspan=1)

button_generate = Button(text="Generate")
button_generate.grid(row=3, column=2)
button_generate.config(command=generate)

button_add = Button(text="Add", width=30)
button_add.grid(row=4, column=1, columnspan=2)

button_add.config(command=add)

windows.mainloop()
