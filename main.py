from tkinter import *

window = Tk()


window.title("Mile to Km Converter")
window.minsize(width=400, height=200)
window.config(padx=80, pady=70)

def miles_to_km_converter():
    miles_to_km_convert = float(miles_to_km.get())
    km = round(miles_to_km_convert * 1.609, 2)
    kilometer_result_label.config(text=f"{km}")




miles_to_km = Entry(width=8)
miles_to_km.grid(row=0, column=1)

miles = Label(text="Miles")
miles.grid(row=0, column=2)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(row=1, column=0)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(row=1, column=1)

km = Label(text="Km")
km.grid(row=1, column=2)

calculate = Button(text="Calculate", command=miles_to_km_converter)
calculate.grid(row=3, column=1)



window.mainloop()