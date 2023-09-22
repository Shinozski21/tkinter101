from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

my_label = Label(text="I am a Label.", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0,)

def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)

def button_clicked2():
    new_text = input.get()
    my_label.config(text=new_text)


input = Entry(width=10)
input.grid(column=3, row=2)

button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button", command=button_clicked2)
new_button.grid(column=2, row=0)
#Entry

print(input.get())
#my_label["text"] = "New Text"
#my_label.config(text="New Text2")




# my_label2 = tkinter.Label(text="You need to work now, Yuki!!!!", font=("Arial", 40, "bold"))
# my_label2.pack()











window.mainloop()