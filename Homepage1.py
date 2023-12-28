from tkinterappfile import *
from PIL import Image, ImageTk


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
                themeButton.config(image=moonIcon, text="Dark Mode")
                currentTheme = "dark"
            else:
                self.config(bg="white")
                mylabel.config(bg="white", fg="black")
                mylabel2.config(bg="white", fg="black")
                searchinput.config(bg="light grey", fg="black")
                themeButton.config(image=sunIcon, text="Light Mode")
                currentTheme = "light"

        currentTheme = "light"

        sunImage = Image.open("Pngs/sun.png").resize((30, 30))
        moonImage = Image.open("Pngs/moon.png").resize((30, 30))


        sunIcon = ImageTk.PhotoImage(sunImage)
        moonIcon = ImageTk.PhotoImage(moonImage)


        # label1 = tk.Label(self,background="White").pack(fill="both", expand=True)

        # Labels and Search Box in Homepage
        themeButton = Button(self, text="Light Mode", command=changeTheme)
        themeButton.config(image=sunIcon, text="Light Mode")
        mylabel = tk.Label(self, text="WUIZ", fg="black", font=("Helvetica", 50), padx=50, pady=50)
        mylabel2 = tk.Label(self, text="Search where you want to see your Weather", fg="black", font=("Helvetica", 20),
                            padx=50, pady=50)
        searchinput = tk.Entry(self, background='light grey', borderwidth=5, width=50, )

        # moves the button to the top right corner

        themeButton.pack(side="top", anchor="ne", padx=10, pady=10)
        # packs color button into frame
        mylabel.pack()  # packs label into frame
        mylabel2.pack()  # packs label into frame
        searchinput.pack()  # packs search into frame

        #Set Homepage a starting point, but I set Weather app as homepage, and then backbutton removes the current page from
        #the window and then packs the page its going to.
        #self.pack(expand=True, fill="both")  # packs the frame on the root window, very important remember to put this
