from tkinter import *
root = Tk()

currentTheme = "light"

# changes the color of the background b/w light and dark mode
def changeTheme():
    global currentTheme
    if currentTheme == "light":
        root.config(bg = "black")
        mylabel.config(bg = "black", fg = "white")
        mylabel2.config(bg = "black", fg = "white")
        searchinput.config(bg = "dark grey", fg = "white")
        currentTheme = "dark"
    else:
        root.config(bg = "white")
        mylabel.config(bg = "white", fg = "black")
        mylabel2.config(bg = "white", fg = "black")
        searchinput.config(bg = "light grey", fg = "black")
        currentTheme = "light"

#main intital window, going to comprise of big font of name of app: WUIZ
#Smaller text below is going to say: "Search where you want to see your Weather"
#Below this text there is going to be a search bar. (Input Bar)

root.geometry("700x700")
root.title('Wuiz')

mylabel = Label(root, text="WUIZ", fg="black", font=("Helvetica", 50), padx=50,pady=50)
mylabel2 = Label(root, text="Search where you want to see your Weather", fg="black", font=("Helvetica", 20), padx=50,pady=50)
searchinput = Entry(root,background='light grey',borderwidth=5, width=50,)

# creates the button that changes the theme
themeButton = Button(root, text = "Change Theme", command = changeTheme)
# moves the button to the top right corner
themeButton.pack(side = TOP, anchor = NE, padx = 10, pady = 10)

def funcclickzip(event):
    print("Zip Code is: " + searchinput.get())  #Gets value of input box when you press enter button

root.bind('<Return>', funcclickzip) #very rought but still
h = searchinput.get()


mylabel.pack()
mylabel2.pack()
searchinput.pack()
themeButton.pack()

root.mainloop()
