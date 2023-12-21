import tkinter as tk
from tkinter import *

LARGEFONT = ("Helvetica", 35)

class tkinterApp(tk.Tk): #Root Window
    def __init__(self):
        #main set up
        super().__init__()
        self.geometry("700x700")
        self.title('Wuiz')

        #widgets
        # Current working on switching between "frames" for right now you have to comment one out if you want to work on it.
        #For example everything but the Weatherpage, is commeted out so the weather page is the only thing displaying
        #self.Homepage = Homepage(self).pack(expand=True, fill="both")

        self.Homepage = Homepage(self) #self = tkinterApp = master/parent
        self.Weatherpage = Weatherpage(self)
        self.Infopage = Infopage(self)

        self.current_frame = self.Infopage
        self.show_frame()

        self.mainloop()

    def show_frame(self):
        for frame in [self.Homepage, self.Weatherpage, self.Infopage]:
            if frame == self.current_frame:
                frame.pack(expand=True, fill="both")
            else:
                frame.pack_forget()



    def go_back(self):
        # Switch to the previous frame
        if self.current_frame == self.Homepage:
            self.current_frame = self.Infopage
        elif self.current_frame == self.Weatherpage:
            self.current_frame = self.Homepage
        elif self.current_frame == self.Infopage:
            self.current_frame = self.Weatherpage

        self.show_frame()




class Homepage(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)

        # changes the color of the background b/w light and dark mode

        def changeTheme():
            nonlocal currentTheme
            if currentTheme == "light":
                self.config(bg="black")
                mylabel.config(bg="black", fg="white")
                mylabel2.config(bg="black", fg="white")
                searchinput.config(bg="dark grey", fg="white")
                currentTheme = "dark"
            else:
                self.config(bg="white")
                mylabel.config(bg="white", fg="black")
                mylabel2.config(bg="white", fg="black")
                searchinput.config(bg="light grey", fg="black")
                currentTheme = "light"

        currentTheme = "light"

        # label1 = tk.Label(self,background="White").pack(fill="both", expand=True)

        # Labels and Search Box in Homepage
        themeButton = Button(self, text="Change Theme", command=changeTheme)
        mylabel = tk.Label(self, text="WUIZ", fg="black", font=("Helvetica", 50), padx=50, pady=50)
        mylabel2 = tk.Label(self, text="Search where you want to see your Weather", fg="black", font=("Helvetica", 20),
                            padx=50, pady=50)
        searchinput = tk.Entry(self, background='light grey', borderwidth=5, width=50, )

        # moves the button to the top right corner

        themeButton.pack(side="top", anchor="ne", padx=10, pady=10)  # packs color button into frame
        mylabel.pack()  # packs label into frame
        mylabel2.pack()  # packs label into frame
        searchinput.pack()  # packs search into frame

        #Set Homepage a starting point, but I set Weather app as homepage, and then backbutton removes the current page from
        #the window and then packs the page its going to.
        #self.pack(expand=True, fill="both")  # packs the frame on the root window, very important remember to put this


class Weatherpage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Back Button at corner => to homepage

        backbutton = Button(self, text="Back", fg="black", font=("Helvetica", 10), width=30,command=parent.go_back)

        backbutton.pack(side=TOP, anchor=NW)  # Back button, put on the top left of the window
        # Top Label "Current Location Weather Data"
        mylabel = Label(self, text="Current Location Weather Data", fg="black", font=("Helvetica", 20), padx=20,
                        pady=20)
        mylabel.pack()

        tempday_frame = Frame(self, width=400, height=200, background="white", border=10, pady=30,
                              padx=30)  # Frame might not be the best but oh well
        tempday_frame.pack()

        # 7 Widgets that represent Mon - Sun and corresponding temps for each
        Days = ["Mon", "Tus", "Wed", "Thurs", "Fri"]  # String of Days
        weeklist = []
        for i in range(0, len(Days)):  # Creates buttons that represent days
            weeklist.append(
                Button(tempday_frame, text=Days[i], fg="black", font=("Helvetica", 10), width=30, height=10), )

        for i in range(0, len(Days)):  # packs buttons to temday_frame
            weeklist[i].pack(side='left')  # All pack in horizontly gots to fix.

        # Temp and Time Graph made from data ranges of tempature from Mon - Sun
        tempdaygraph_frame = Frame(self, width=600, height=200, background="white", border=10, pady=30,
                                   padx=30)  # Frame might not be the best but oh well
        tempdaygraph_frame.pack()  # Graph frame from temp data
        tempgraph = Canvas(tempdaygraph_frame, width=850, height=200, background="light grey", border=10)
        tempgraph.pack()  # Canvas in frame, its just a place holder


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


if __name__ == '__main__':
    tkinterApp()






