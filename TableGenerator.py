from tkinter import *
from tkinter.ttk import *

def generateTable():
    tables = ""
    for i in range(endVal.get() + 1):
        tables += str(the_num.get()) + "x" + str(i) + "=" + str(the_num.get() * i) + "\n"
    table_display.configure(text = tables)


window = Tk()

title = Label(window, text = "Table Generator", font = ("Arial", 15))

title.grid(row = 0, column = 0, columnspan = 3)

l1 = Label(window, text = "Numbers and Range", font = ("Arial", 15))
l1.grid(row = 1, column = 0)

the_num = IntVar()
numbers = Combobox(window, textvariable = the_num, width = 5)
numbers["values"] = tuple(range(21))


endVal = IntVar()

r1 = Radiobutton(window, variable = endVal, text = "10", value = 10)
r2 = Radiobutton(window, variable = endVal, text = "20", value = 20)
r3 = Radiobutton(window, variable = endVal, text = "30", value = 30)
numbers.grid(row = 1, column = 1)

endVal.set(30)


r1.grid(row = 1, column = 2)
r2.grid(row = 2, column = 2)
r3.grid(row = 3, column = 2)

b1 = Button(window, text = "Generate", command = generateTable)
b1.grid(row = 4, column = 1)

table_display = Label(window, anchor = "center")
table_display.grid(row = 5, column = 1)





window.mainloop()