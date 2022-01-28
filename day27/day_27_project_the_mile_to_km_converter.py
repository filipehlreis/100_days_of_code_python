import tkinter


def calculate_miles_to_km():
    number = float(miles_input_miles.get())
    result = round(number * 1.60934, 3)
    miles_label_result.config(text=result)


def calculate_km_to_miles():
    number = float(km_input_miles.get())
    result = round(number / 1.60934, 3)
    km_label_result.config(text=result)


def calculate_mils_to_mm():
    number = float(mils_input_miles.get())
    result = round(number / 39.37, 3)
    mils_label_result.config(text=result)


def calculate_mm_to_mils():
    number = float(mm_input_miles.get())
    result = round(number * 39.37, 3)
    mm_label_result.config(text=result)


window = tkinter.Tk()
# window.minsize(width=100, height=100)
window.title("Mile to Km converter")
window.config(padx=20, pady=20)


# Miles to KM
miles_input_miles = tkinter.Entry()
miles_input_miles.insert(tkinter.END, string="0.0")
miles_input_miles.config(width=10, justify="center")
miles_input_miles.grid(row=0, column=1)

miles_label_miles = tkinter.Label()
miles_label_miles.config(text="miles")
miles_label_miles.grid(row=0, column=2)

miles_label_equal = tkinter.Label()
miles_label_equal.config(text="is equal to")
miles_label_equal.grid(row=1, column=0)

miles_label_result = tkinter.Label()
miles_label_result.config(text="0.0")
miles_label_result.grid(row=1, column=1)

miles_label_km = tkinter.Label()
miles_label_km.config(text="km")
miles_label_km.grid(row=1, column=2)

miles_button_calculate = tkinter.Button()
miles_button_calculate.config(text="Calculate", command=calculate_miles_to_km)
miles_button_calculate.grid(row=2, column=1)

label_space_1 = tkinter.Label()
label_space_1.grid(row=3)


# KM to Miles
km_input_miles = tkinter.Entry()
km_input_miles.insert(tkinter.END, string="0.0")
km_input_miles.config(width=10, justify="center")
km_input_miles.grid(row=4, column=1)

km_label_miles = tkinter.Label()
km_label_miles.config(text="km")
km_label_miles.grid(row=4, column=2)

km_label_equal = tkinter.Label()
km_label_equal.config(text="is equal to")
km_label_equal.grid(row=5, column=0)

km_label_result = tkinter.Label()
km_label_result.config(text="0.0")
km_label_result.grid(row=5, column=1)

km_label_km = tkinter.Label()
km_label_km.config(text="miles")
km_label_km.grid(row=5, column=2)

km_button_calculate = tkinter.Button()
km_button_calculate.config(text="Calculate", command=calculate_km_to_miles)
km_button_calculate.grid(row=6, column=1)

label_space_2 = tkinter.Label()
label_space_2.grid(row=7)


# Mils to mm
mils_input_miles = tkinter.Entry()
mils_input_miles.insert(tkinter.END, string="0.0")
mils_input_miles.config(width=10, justify="center")
mils_input_miles.grid(row=8, column=1)

mils_label_miles = tkinter.Label()
mils_label_miles.config(text="mils")
mils_label_miles.grid(row=8, column=2)

mils_label_equal = tkinter.Label()
mils_label_equal.config(text="is equal to")
mils_label_equal.grid(row=9, column=0)

mils_label_result = tkinter.Label()
mils_label_result.config(text="0.0")
mils_label_result.grid(row=9, column=1)

mils_label_km = tkinter.Label()
mils_label_km.config(text="mm")
mils_label_km.grid(row=9, column=2)

mils_button_calculate = tkinter.Button()
mils_button_calculate.config(text="Calculate", command=calculate_mils_to_mm)
mils_button_calculate.grid(row=11, column=1)

label_space_3 = tkinter.Label()
label_space_3.grid(row=12)


# mm to Mils
mm_input_miles = tkinter.Entry()
mm_input_miles.insert(tkinter.END, string="0.0")
mm_input_miles.config(width=10, justify="center")
mm_input_miles.grid(row=13, column=1)

mm_label_miles = tkinter.Label()
mm_label_miles.config(text="mm")
mm_label_miles.grid(row=13, column=2)

mm_label_equal = tkinter.Label()
mm_label_equal.config(text="is equal to")
mm_label_equal.grid(row=14, column=0)

mm_label_result = tkinter.Label()
mm_label_result.config(text="0.0")
mm_label_result.grid(row=14, column=1)

mm_label_km = tkinter.Label()
mm_label_km.config(text="mils")
mm_label_km.grid(row=14, column=2)

mm_button_calculate = tkinter.Button()
mm_button_calculate.config(text="Calculate", command=calculate_mm_to_mils)
mm_button_calculate.grid(row=15, column=1)


window.mainloop()
