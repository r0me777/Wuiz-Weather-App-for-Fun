from tkinterappfile import *
from datetime import datetime
from meteostat import Hourly
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk


class Weatherpage(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        # Back Button at corner => to homepage
        backbutton = Button(self, text="Back", command=parent.go_back)

        backbutton.pack(side="top", anchor=NW, pady=15, padx=15)  # Back button, put on the top left of the window
        # Top Label "Current Location Weather Data"
        mylabel = Label(self, text="Current Location Weather Data", fg="black", font=("Helvetica", 20), padx=20, )
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
        tempdaygraph_frame = Frame(self, width=600, height=200, background="white", border=10, pady=20,
                                   padx=20)  # Frame might not be the best but oh well
        tempdaygraph_frame.pack()  # Graph frame from temp data

        self.plot_temperature_graph(tempdaygraph_frame)

    def plot_temperature_graph(self, frame):
        # Set time period
        start = datetime(2018, 1, 1)
        end = datetime(2018, 1, 7)

        # Get hourly data
        data = Hourly('10637', start, end)
        data = data.fetch()

        # Create Matplotlib figure and plot
        fig, ax = plt.subplots(figsize=(4, 3))
        data.plot(y=['temp'], ax=ax, legend=False)
        plt.xlabel('Date')
        plt.ylabel('Temperature (°C)')

        # Embed Matplotlib plot in Tkinter window
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack()
