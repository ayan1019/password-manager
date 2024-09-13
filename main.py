
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # nr_letters = random.randint(8, 10)
    # nr_symbols = random.randint(2, 4)
    # nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(random.randint(6, 8))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(1, 2))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(1, 2))]

    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char

    password = "".join(password_list)

    # print(f"Your password is: {password}")
    pass_input.insert(0, password)
    pyperclip.copy(password)


def save():
    web_text = web_input.get()
    email_text = email_input.get()
    pass_text = pass_input.get()
    new_data = {
        web_text: {
            "email": email_text,
            "password": pass_text,
        }
    }

    if len(web_text) == 0 or len(pass_text) == 0:
        messagebox.showwarning(title="Oops!", message="Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=web_text, message=f"These are the details entered:"
                                                               f" \nEmail: {email_text} \nPassword: {pass_text} ")
        if is_ok:
            try:

                with open("data.json", "r") as file:
                    data = json.load(file)

            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)

            else:
                data.update(new_data)

                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                web_input.delete(0, "end")
                pass_input.delete(0, "end")


def search_password():
    website = web_input.get()
    try:
        with open("data.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error!", message="No data file found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error!", message=f"No detail for {website} exists.")


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

web_input = Entry(width=21)
web_input.grid(column=1, row=1)
web_input.focus()

web_label = Label(text="Website:")
web_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)
email_input = Entry(width=38)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "ayanyadav2619@gmail.com")

pass_input = Entry(width=21)
pass_input.grid(column=1, row=3)

pass_button = Button(text="Generate Password", command=generate_password)
pass_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=13,  command=search_password)
search_button.grid(column=2, row=1)

window.mainloop()
