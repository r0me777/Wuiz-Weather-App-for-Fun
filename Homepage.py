from tkinter import *
root = Tk()

#main intital window, going to comprise of big font of name of app: WUIZ
#Smaller text below is going to say: "Search where you want to see your Weather"
#Below this text there is going to be a search bar. (Input Bar)

root.geometry("700x700")
root.title('Wuiz')

mylabel = Label(root, text="WUIZ", fg="black", font=("Helvetica", 50), padx=50,pady=50)
mylabel2 = Label(root, text="Search where you want to see your Weather", fg="black", font=("Helvetica", 20), padx=50,pady=50)
searchinput = Entry(root,background='light grey',borderwidth=5, width=50,)

def funcclickzip(event):
    print("Zip Code is: " + searchinput.get()) #Gets value of input box when you press enter button

root.bind('<Return>', funcclickzip) #very rought but still


mylabel.pack()
mylabel2.pack()
searchinput.pack()

root.mainloop()
