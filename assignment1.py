import tkinter as tk
import tkinter.ttk as ttk


window = tk.Tk()
window.geometry('550x220')
window.title("Assignment")

# Q1 Combobox
combobox_label = tk.Label(window, text="Select Month")
combobox_label.grid(row=0, column=0, pady=8)

combobox = ttk.Combobox(window, width=27, )
combobox['values'] = ("January", "February", "March")
combobox.grid(row=0, column=1)

# Q2 Program to create three single line text box to accept values
name_label = tk.Label(window, text="Enter name")
name_label.grid(row=1, column=0, padx=3, pady=5)

name_entry1 = tk.Entry(window)
name_entry1.grid(row=1, column=1, padx=3, pady=5)

name_entry2 = tk.Entry(window)
name_entry2.grid(row=1, column=2, padx=3, pady=5)

name_entry3 = tk.Entry(window)
name_entry3.grid(row=1, column=3, padx=3, pady=5)


# Q3 Enter two integers and display their sum
integer_label = tk.Label(window, text="Enter integer")
integer_label.grid(row=2, column=0, padx=3, pady=5)


# Function to calculate two numbers
def addInteger():
    integer1_value = int(integer1.get())
    integer2_value = int(integer2.get())
    sum_int = integer1_value + integer2_value
    tk.Label(window, text=sum_int).grid(row=3, column=1)


integer1 = tk.Entry(window)
integer1.grid(row=2, column=1)

integer2 = tk.Entry(window)
integer2.grid(row=2, column=2)

int_label = tk.Label(window, text="Answer =")
int_label.grid(row=3, column=0)

button= tk.Button(window, text="Calculate", command=addInteger)
button.grid(row=2, column=3, pady=3)


# Q4 Program that displays a dialogue box that accepts integer and returns double

# Function to convert to float
def returnsDouble():
    number_value = int(number.get())
    convert_to_float = float(number_value)
    tk.Label(window, text=convert_to_float).grid(row=5, column=1)


number_label = tk.Label(window, text="Enter number")
number_label.grid(row=4, column=0, padx=3, pady=5)

number = tk.Entry(window)
number.grid(row=4, column=1)

number_label_answer = tk.Label(window, text="Float Value =")
number_label_answer.grid(row=5, column=0, padx=3, pady=5)

number_button = tk.Button(window, text="Click to convert", command=returnsDouble)
number_button.grid(row=4, column=2, pady=2)
window.mainloop()