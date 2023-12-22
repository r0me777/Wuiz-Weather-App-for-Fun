from tkinterappfile import *

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
