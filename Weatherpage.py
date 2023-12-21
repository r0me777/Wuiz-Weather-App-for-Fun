from tkinter import *
from Homepage import searchinput

#zipcode = int(h) #imports input from homepage

main = Tk() #main window
main.geometry("1000x700") #Starting Size of the window
main.title("Current Weather Data") #Title of Window


# Back Button at corner => to homepage

backbutton = Button(main, text="Back", fg="black", font=("Helvetica", 10), width=30) #Back button does nothing
backbutton.pack(side=TOP,anchor=NW) #Back button, put on the top left of the window

#Top Label "Current Location Weather Data"

mylabel = Label(main, text="Current Location Weather Data", fg="black", font=("Helvetica", 20), padx=20,pady=20) #Label
mylabel.pack() #might use grid but pack seems to work

#print(main.winfo_width()) ignore

tempday_frame = Frame(main, width=400, height=200, background= "white", border=10, pady=30, padx=30) #Frame might not be the best but oh well
tempday_frame.pack()

# 7 Widgets that represent Mon - Sun and corresponding temps for each

Days = ["Mon","Tus", "Wed", "Thurs", "Fri"] #String of Days
weeklist = []

for i in range(0,4): #Creates buttons that represent days
    weeklist.append(Button(tempday_frame, text=Days[i], fg="black", font=("Helvetica", 10), width=30, height=10),)

for i in range(0,4): #packs buttons to temday_frame
    weeklist[i].pack(side='left') #All pack in horizontly gots to fix.

# Temp and Time Graph made from data ranges of tempature from Mon - Sun

tempdaygraph_frame = Frame(main, width=600, height=200, background= "white", border=10, pady=30, padx=30) #Frame might not be the best but oh well
tempdaygraph_frame.pack() #Graph frame from temp data

tempgraph = Canvas(tempdaygraph_frame, width=850, height=200, background="light grey", border=10)
tempgraph.pack() #Canvas in frame, its just a place holder
#Info graphic button



# Center Weather Icon / Image
    #  Need to create

main.mainloop()
#Should be generated based of zip code of Homepage, will look into python weather module.