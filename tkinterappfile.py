import tkinter as tk
from tkinter import *
from Weatherpage import Weatherpage
from Homepage1 import Homepage
from Infopage import Infopage



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


