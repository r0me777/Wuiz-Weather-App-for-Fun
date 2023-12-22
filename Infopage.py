from tkinterappfile import *

class Infopage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        #self.pack(expand=True, fill="both")
        backbutton = Button(self, text="Back", fg="black", font=("Helvetica", 10),
                            width=30,command=parent.go_back)  # Back button does nothing
        backbutton.pack(side=TOP, anchor=NW)  # Back button, put on the top left of the window

        # Top Label "Current Location Weather Data"

        mylabel = Label(self, text="Infographics: '..............' ", fg="black", font=("Helvetica", 20), padx=50,
                        pady=100)  # Label
        mylabel.pack()  # might use grid but pack seems to work

        # print(main.winfo_width()) ignore

        tempday_frame = Frame(self, width=700, height=700, background="white", border=10, pady=30,
                              padx=30)  # Frame might not be the best but oh well
        tempday_frame.pack()

        # 7 Widgets that represent Mon - Sun and corresponding temps for each
        count = 0
        Questions = ["A ", "B ", "C", "D"]  # String of Days
        weeklist = []

        for i in range(0, 3):  # Creates buttons that represent days
            weeklist.append(Button(tempday_frame, text="A", fg="black", font=("Helvetica", 30), width=50, height=4))

        for i in range(0, 3):  # packs buttons to temday_frame
            weeklist[i].pack()  # All pack in horizontly gots to fix.
            print(i)

        # Center Weather Icon / Image
        #  Need to create