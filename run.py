from contextlib import nullcontext
from inspect import formatannotationrelativeto
from tkinter import *
from yeelight import *


class YeeLight:
    dict = discover_bulbs()
    bulbs = []
    bulb = ""


    if(bool(dict.count)):
        bulbs.append(', '.join(d['ip'] for d in dict))

    def onselect(event):
        w = event.widget
        idx = int(w.curselection()[0])
        value = w.get(idx)
        # if(value[0] != nullcontext):
        global bulb
        bulb = Bulb(value[0])

    def toggle():
        try:
            global bulb
            bulb.toggle()
        except:
            print('No bulb selected')

    # GUI
    root = Tk()  # Main Window
    root.title("YeeLight - Bulb Controller Tool")
    root.geometry('300x400')
    root.resizable(FALSE, FALSE)

    l1 = Label(root, text="Discovered bulbs:",
               justify='center', wraplength=120)
    l1.pack()

    # List of detected bulks
    bl = Listbox(root, selectmode='single')
    bl.selectedindex = 0
    bl.pack()
    bl.insert(END, bulbs)
    bl.bind('<<ListboxSelect>>', onselect)

    l2 = Label(root, text="If your device is not on the list, please make sure it's enabled and connected to same network with computer.",
               justify='center', wraplength=250)
    l2.pack()

    bt1 = Button(root, text="Toggle", justify='center', command=toggle)
    bt1.pack()

    # all widgets will be here
    # Execute Tkinter
    root.mainloop()
