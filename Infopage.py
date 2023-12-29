from tkinterappfile import *
import tkinter as tk

class Infopage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # self.pack(expand=True, fill="both")
        backbutton = Button(self, text="Back", fg="black", font=("Helvetica", 10), command=parent.go_back)  # Back button does nothing
        backbutton.pack(side=TOP, anchor=NW, padx=15, pady=10)  # Back button, put on the top left of the window

        # Top Label "Current Location Weather Data"
        label_frame = LabelFrame(self, background="#003f39", padx=5, pady=5, foreground="#5c9aef")
        label_frame.pack()
        mylabel = Label(label_frame, text="Infographics: '..............' ", font=("Georgia", 12), background="#5c9aef")  # Label
        mylabel.pack()  # might use grid but pack seems to work

        # print(main.winfo_width()) ignore

        tempday_frame = Frame(self, width=700, height=700, background="#79A7D3", border=10, pady=30,
                              padx=30)  # Frame might not be the best but oh well
        tempday_frame.pack()

        # 7 Widgets that represent Mon - Sun and corresponding temps for each
        count = 0
        Questions = ["A ", "B ", "C", "D"]  # String of Days
        weeklist = []

        for i in range(0, 3):  # Creates buttons that represent days
            weeklist.append(Button(tempday_frame, text="A", fg="black", font=("Georgia", 30), width=10, height=4, padx=10, pady=10).grid(row=0, column=i))

        for i in range(0, 3):  # packs buttons to temday_frame
            #weeklist[i]  # All pack in horizontly gots to fix.
            print(i)

        # Center Weather Icon / Image
        #  Need to create
