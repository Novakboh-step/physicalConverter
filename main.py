from DistanceConverter import DistanceConverter
from MassConverter import MassConverter
from TimeConverter import TimeConverter
from tkinter import *
from tkinter import ttk

def changeUnits(*args):
    units1["values"] = units[converters.get()]
    units2["values"] = units[converters.get()]

def convert():
    cur = converters.current()
    if cur == 0:
        con = DistanceConverter()
    elif cur == 1:
        con = MassConverter()
    else:
        con = TimeConverter()
    number = float(entry.get())
    unit1 = units1.get()
    unit2 = units2.get()
    number *= con.convert(unit1, unit2)
    result["text"] = number

def nightTheme():
    root.config(bg="black")
    result.config(bg="black", fg="white")
    button.config(bg="black", fg="white")
    theme.config(bg="black", fg="white", text="Day theme", command=dayTheme)

def dayTheme():
    root.config(bg="lightgrey")
    result.config(bg="lightgrey", fg="black")
    button.config(bg="lightgrey", fg="black")
    theme.config(bg="lightgrey", fg="black", text="Night theme", command=nightTheme)

units = {
    "Distance": ["km", "m", "dm", "cm", "mm", "ml", "ft"],
    "Mass": ["t", "kg", "g", "mg", "lb", "oz"],
    "Time": ["y", "mon","d", "h", "min", "s", "ms"]
}
root = Tk()
root.geometry("300x300")
root.title("Converter")
converters = ttk.Combobox(values=list(units.keys()), width=40)
converters.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
entry = Entry(width=30)
entry.grid(row=1, column=0, padx=5, pady=5)
units1 = ttk.Combobox(width=10)
units1.grid(row=1, column=1, padx=5, pady=5)
units2 = ttk.Combobox(width=10)
units2.grid(row=2, column=1, padx=5, pady=5)
result = Label(text="...............")
result.grid(row=2, column=0, padx=5, pady=5)
button = Button(text="Convert", width=30, command=convert)
button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
theme = Button(text="Night theme", width=30, command=nightTheme)
theme.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
converters.bind("<<ComboboxSelected>>", changeUnits)
root.mainloop()