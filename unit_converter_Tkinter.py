# Import madules
from tkinter import *
from tkinter.font import *
from tkinter import messagebox

# Main function
def calcualte_unit():

    # Get the information
    unit_from = list_box_from.get(ACTIVE)
    unit_to = list_box_to.get(ACTIVE)

    # Exception handling (int or float)
    try :
        value_from = float(entry_from.get())
    except :
        messagebox.showerror(title="ERROR!",message="Please enter an integer or float.")
    else :

        # Centimeter to another
        if unit_from == 'Centimeter':

            if unit_to == 'Centimeter':
                result = value_from
            elif unit_to == 'Meter':
                result = value_from / 100
            elif unit_to == 'Kilometer':
                result = value_from / 100000
            elif unit_to == 'Mile':
                result = value_from * 0.00000621371
            elif unit_to == 'Yard':
                result = value_from * 0.109361

        # Meter to enother
        elif unit_from == 'Meter':

            if unit_to == 'Centimeter':
                result = value_from * 100
            elif unit_to == 'Meter':
                result = value_from
            elif unit_to == 'Kilometer':
                result = value_from / 1000
            elif unit_to == 'Mile':
                result = value_from * 0.000621371
            elif unit_to == 'Yard':
                result = value_from * 1.09361

        # Kilometer to another
        elif unit_from == 'Kilometer':

            if unit_to == 'Centimeter':
                result = value_from * 100000
            elif unit_to == 'Meter':
                result = value_from * 1000
            elif unit_to == 'Kilometer':
                result = value_from    
            elif unit_to == 'Mile':
                result = value_from * 0.621371
            elif unit_to == 'Yard':
                result = value_from * 1093.61

        # Display result
        entry_to.delete(0,END)
        entry_to.insert(END,result)

# Create main window 
root = Tk()

# Removes the maximize button
root.resizable(False,False)

# Logo & Title
root.wm_iconbitmap("info.ico")
root.wm_title("Unit Convertor")

# Create fonts
font_1 = Font(family='cosolas',size=14)
font_2 = Font(family='Times',size=18,underline=True)

# Create labels & grid of them
label_from = Label(root,text='From:',font=font_2)
label_to = Label(root,text='To:',font=font_2)
label_from.grid(row=0,column=0,sticky=W,padx=1,pady=0)
label_to.grid(row=0,column=1,sticky=W,padx=1,pady=0)

# Create entry_from & entry_to & grid of them
entry_from = Entry(root,font = font_1,bg='#a0aacd',fg='#e8e6e4')
entry_to = Entry(root,font = font_1,bg='#93d3e1',fg='#e8e6e4')
entry_from.grid(row=1,column=0,padx=2,pady=3)
entry_to.grid(row=1,column=1,padx=2,pady=3)

# Create from_listbox & to_listbox & grid of them
list_box_from = Listbox(root,exportselection=False,font=font_1,bg='#8a99cd',fg='#e8e6e4')
list_box_to = Listbox(root,exportselection=False,font=font_1,bg='#72cee2',fg='#e8e6e4')
list_box_from.grid(row=2,column=0)
list_box_to.grid(row=2,column=1)

# Insert to from_listbox
list_box_from.insert(END,'Centimeter')
list_box_from.insert(END,'Meter')
list_box_from.insert(END,'Kilometer')
list_box_from.insert(END,'Mile')
list_box_from.insert(END,'Yard')

# Insert to from_listbox
list_box_to.insert(END,'Centimeter')
list_box_to.insert(END,'Meter')
list_box_to.insert(END,'Kilometer')
list_box_to.insert(END,'Mile')
list_box_to.insert(END,'Yard')

# Create calculate button & grid of him
button = Button(root,text='Calculate',font=font_1,bg='#5ec0ff',fg='#e8e6e4',activebackground='light gray',activeforeground='blue',command=calcualte_unit)
button.grid(row=3,column=0,columnspan=2,sticky=W+E,padx=1,pady=5)

# Finish order
root.mainloop()