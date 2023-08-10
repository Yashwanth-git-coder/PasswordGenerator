from tkinter import *
import random
import pyperclip

BLACK = "#252B48"
RED = "#F31559"

def generate_password():
    password = []
    try:
        letter = letter_entrey.get()
        number = number_entry.get()
        symbol = symbol_entry.get()

        letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
                   "V", "W", "X", "Y", "Z", 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                   'q', 'r',
                   's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = [
            '!', '#', '$', '%', '&', '(', ')', '*', '+']


        integer_letter = int(letter)
        integer_number = int(number)
        integer_symbol = int(symbol)




        for _ in range(1, int(integer_letter + 1)):
            password.append(random.choice(letters))

        for _ in range(1, int(integer_number + 1)):
            password.append(random.choice(numbers))

        for _ in range(1, int(integer_symbol + 1)):
            password.append(random.choice(symbols))

        random.shuffle(password)
        password = "".join(password)

        generated_password_entry.insert(0, password)
        pyperclip.copy(password)
    except ValueError:
        generated_password_entry.insert(0, "Insert above Values")

    finally:
        letter_entrey.delete(0, END)
        number_entry.delete(0, END)
        symbol_entry.delete(0, END)


#------------------------------------------------------UI_SetUp------------------------------------------------------#

windows = Tk()
windows.title("Password Generator")
windows.config(padx=50, pady=50, bg=BLACK)

canvas = Canvas(width=309, height=309, highlightthickness=0, bg=BLACK)
logo_img = PhotoImage(file="image/1-modified.png")
canvas.create_image(154, 154, image=logo_img)
canvas.grid(column=0, row=0, columnspan=2)

no_letters = Label(text="Number of Letters : ", bg=BLACK, fg="white", padx=10, pady=10)
no_letters.grid(column=0, row=1)

letter_entrey = Entry(width=8)
letter_entrey.grid(column=1, row=1)

no_numbers = Label(text="Number of Numbers : ", bg=BLACK, fg="white", padx=10, pady=10)
no_numbers.grid(column=0, row=2)

number_entry = Entry(width=8)
number_entry.grid(column=1, row=2)

no_symbols = Label(text="Number of Symbols : ", bg=BLACK, fg="white", padx=10, pady=10)
no_symbols.grid(column=0, row=4)

symbol_entry = Entry(width=8)
symbol_entry.grid(column=1, row=4)

space = Label(bg=BLACK, padx=10, pady=7)
space.grid(column=0, row=5)

generated_password_entry = Entry(width=20)
generated_password_entry.grid(column=0, row=6, columnspan=2)

generate_button = Button(text="Generate", bg=RED, command=generate_password)
generate_button.grid(column=2, row=6)


windows.mainloop()