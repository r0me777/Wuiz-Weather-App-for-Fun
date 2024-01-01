import tkinter
from tkinterappfile import *
from PIL import Image, ImageTk


class Homepage(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)

        #setting the background
        self.backGroundImage = self.resize_image("Pngs/backGroundMaybe.png")
        
        self.background = Label(self, image=self.backGroundImage)
        self.background.place(relwidth=1, relheight=1)
        
        #creating the canvis to place the items
        self.canvas = Canvas(self, width=520, height=600,bg="white")
        self.canvas.place(x=150,y=100)
        
        
        #make sure the canvas is placed on the background regardless if we move screen size
        # Make sure the canvas is placed on the background regardless of screen size
        self.place_canvas_in_center()

        # Bind the window resizing event to update the canvas position
        self.bind("<Configure>", self.on_window_resize)

        

        
        
        
        
        # changes the color of the background b/w light and dark mode
        #commenting out the change theme incase we need it

        #def changeTheme():
            #nonlocal currentTheme
            #if currentTheme == "light":
                # mylabel.config(bg="black", fg="white")
                #mylabel2.config(bg="black", fg="white")
                #searchinput.config(bg="dark grey", fg="white")
                #themeButton.config(image=moonIcon, text="Dark Mode")
                #currentTheme = "dark"
            #else:
                #self.config(bg="white")
                #mylabel.config(bg="white", fg="black")
                #mylabel2.config(bg="white", fg="black")
                #searchinput.config(bg="light grey", fg="black")
                #themeButton.config(image=sunIcon, text="Light Mode")
                #currentTheme = "light"

        currentTheme = "light"

        sunImage = Image.open("Pngs/sun.png").resize((30, 30))
        moonImage = Image.open("Pngs/moon.png").resize((30, 30))


        sunIcon = ImageTk.PhotoImage(sunImage)
        moonIcon = ImageTk.PhotoImage(moonImage)


        # label1 = tk.Label(self,background="White").pack(fill="both", expand=True)

        # Labels and Search Box in Homepage
        themeButton = Button(self, text="Light Mode")
        themeButton.config(image=sunIcon, text="Light Mode")
        title_frame = tk.Frame(self.canvas, bg="")
        title_frame.place(relx=0.5, rely=0.2, anchor="n")

        # Labels
        Title = tk.Label(title_frame, text="WUIZ", font=("Helvetica", 80), fg="#ADD8E6",bg="white")
        
        labelToAskForZipCode = tk.Label(self, text="Enter Zip Code", font=("Helvetica", 20),
                            padx=50, pady=50,fg="#ADD8E6",bg="white")
        searchinput = tk.Entry(self, borderwidth=5, width=10,bg="white",fg="black" )

        # moves the button to the top right corner

        themeButton.pack(side="top", anchor="ne", padx=10, pady=10)
        Title.pack()
        # Forward Button at corner => to homepage
        forwardbutton = Button(self, text="Next", command=parent.go_forward)

        forwardbutton.pack(side="top", anchor=NE, pady=15, padx=15)  # Back button, put on the top left of the window

        # packs color button into frame
        

        # Packs label into frame

        labelToAskForZipCode.place(relx=0.5, rely=0.5, anchor="center")

        # Packs search into frame
        searchinput.place(relx=0.5, rely=0.6, anchor="center")


        #Set Homepage a starting point, but I set Weather app as homepage, and then backbutton removes the current page from
        #the window and then packs the page its going to.
        #self.pack(expand=True, fill="both")  # packs the frame on the root window, very important remember to put this

    def place_canvas_in_center(self):

            self.background.update_idletasks()  # Ensure the label has its actual size
            label_width = self.background.winfo_width()
            label_height = self.background.winfo_height()

            canvas_width = self.canvas.winfo_reqwidth()
            canvas_height = self.canvas.winfo_reqheight()

            x_position = (label_width - canvas_width) // 2
            y_position = (label_height - canvas_height) // 2

            self.canvas.place(x=x_position, y=y_position)

    def on_window_resize(self, event):
        self.place_canvas_in_center()
        # Update the canvas position when the window is resized
        self.place_canvas_in_center()
        
    def resize_image(self, image_path):
        # Get the screen width and height
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Open and resize the image based on screen size
        original_image = Image.open(image_path)
        resized_image = original_image.resize((screen_width, screen_height), Image.ANTIALIAS)

        return ImageTk.PhotoImage(resized_image)