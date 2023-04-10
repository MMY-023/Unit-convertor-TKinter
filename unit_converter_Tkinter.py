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

        # Milimeter to another
        if unit_from == 'Milimeter':

            if unit_to == 'Milimeter':
                result = value_from
            elif unit_to == 'Centimeter':
                result = value_from / 10
            elif unit_to == 'Meter':
                result = value_from / 1000 
            elif unit_to == 'Kilometer':
                result = value_from / 1000000
            elif unit_to == 'Mile':
                result = value_from / 1609000
            elif unit_to == 'Yard':
                result = value_from / 914.4
            elif unit_to == 'Inch':
                result = value_from / 25.4
            elif unit_to == 'Foot':
                result = value_from / 304.8

        # Centimeter to another
        elif unit_from == 'Centimeter':

            if unit_to == 'Milimeter':
                result = value_from
            elif unit_to == 'Centimeter':
                result = value_from
            elif unit_to == 'Meter':
                result = value_from / 100
            elif unit_to == 'Kilometer':
                result = value_from / 100000
            elif unit_to == 'Mile':
                result = value_from / 160900
            elif unit_to == 'Yard':
                result = value_from / 91.44
            elif unit_to == 'Inch':
                result = value_from / 2.54
            elif unit_to == 'Foot':
                result = value_from / 30.48

        # Meter to enother
        elif unit_from == 'Meter':

            if unit_to == 'Milimeter':
                result = value_from * 1000
            elif unit_to == 'Centimeter':
                result = value_from * 100
            elif unit_to == 'Meter':
                result = value_from
            elif unit_to == 'Kilometer':
                result = value_from / 1000
            elif unit_to == 'Mile':
                result = value_from / 1609
            elif unit_to == 'Yard':
                result = value_from / 0.9144
            elif unit_to == 'Inch':
                result = value_from / 0.0254
            elif unit_to == 'Foot':
                result = value_from / 0.3048

        # Kilometer to another
        elif unit_from == 'Kilometer':

            if unit_to == 'Milimeter':
                result = value_from * 1000000
            elif unit_to == 'Centimeter':
                result = value_from * 100000
            elif unit_to == 'Meter':
                result = value_from * 1000
            elif unit_to == 'Kilometer':
                result = value_from    
            elif unit_to == 'Mile':
                result = value_from / 1.609
            elif unit_to == 'Yard':
                result = value_from / 0.0009144
            elif unit_to == 'Inch':
                result = value_from / 0.0000254
            elif unit_to == 'Foot':
                result = value_from / 0.0003048

        # Mile to another
        elif unit_from == 'Mile':

            if unit_to == 'Milimeter':
                result = value_from * 1609000
            elif unit_to == 'Centimeter':
                result = value_from * 160900
            elif unit_to == 'Meter':
                result = value_from * 1609
            elif unit_to == 'Kilometer':
                result = value_from * 1.609
            elif unit_to == 'Mile':
                result = value_from
            elif unit_to == 'Yard':
                result = value_from * 1760
            elif unit_to == 'Inch':
                result = value_from * 63360
            elif unit_to == 'Foot':
                result = value_from * 5280

        # Yard to another
        elif unit_from == 'Yard':

            if unit_to == 'Milimeter':
                result = value_from * 914.4
            elif unit_to == 'Centimeter':
                result = value_from * 91.44
            elif unit_to == 'Meter':
                result = value_from * 0.9144
            elif unit_to == 'Kilometer':
                result = value_from * 0.0009144 
            elif unit_to == 'Mile':
                result = value_from / 1760
            elif unit_to == 'Yard':
                result = value_from
            elif unit_to == 'Inch':
                result = value_from * 36
            elif unit_to == 'Foot':
                result = value_from * 3

        # Inch to another
        elif unit_from == 'Inch':

            if unit_to == 'Milimeter':
                result = value_from * 25.4
            elif unit_to == 'Centimeter':
                result = value_from * 2.54
            elif unit_to == 'Meter':
                result = value_from * 0.0254
            elif unit_to == 'Kilometer':
                result = value_from * 0.0000254  
            elif unit_to == 'Mile':
                result = value_from / 63360
            elif unit_to == 'Yard':
                result = value_from / 36
            elif unit_to == 'Inch':
                result = value_from
            elif unit_to == 'Foot':
                result = value_from / 12

        # Foot to another
        elif unit_from == 'Foot':

            if unit_to == 'Milimeter':
                result = value_from * 304.8
            elif unit_to == 'Centimeter':
                result = value_from * 30.48
            elif unit_to == 'Meter':
                result = value_from * 0.3048
            elif unit_to == 'Kilometer':
                result = value_from * 0.0003048 
            elif unit_to == 'Mile':
                result = value_from / 5280
            elif unit_to == 'Yard':
                result = value_from / 3
            elif unit_to == 'Inch':
                result = value_from * 12
            elif unit_to == 'Foot':
                result = value_from

        # Show result
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
list_box_from.insert(END,'Milimeter')
list_box_from.insert(END,'Centimeter')
list_box_from.insert(END,'Meter')
list_box_from.insert(END,'Kilometer')
list_box_from.insert(END,'Mile')
list_box_from.insert(END,'Yard')
list_box_from.insert(END,'Inch')
list_box_from.insert(END,'Foot')

# Insert to from_listbox
list_box_to.insert(END,'Milimeter')
list_box_to.insert(END,'Centimeter')
list_box_to.insert(END,'Meter')
list_box_to.insert(END,'Kilometer')
list_box_to.insert(END,'Mile')
list_box_to.insert(END,'Yard')
list_box_to.insert(END,'Inch')
list_box_to.insert(END,'Foot')

# Create calculate button & grid of him
button = Button(root,text='Calculate',font=font_1,bg='#5ec0ff',fg='#e8e6e4',activebackground='light gray',activeforeground='blue',command=calcualte_unit)
button.grid(row=3,column=0,columnspan=2,sticky=W+E,padx=1,pady=5)

# Finish order
root.mainloop()
