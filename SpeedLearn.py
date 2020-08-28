from tkinter import *
# * This is used for highlighting
# ? Used for Questions
# ! Used for Warnings
# TODO used for Todo items
# // used for strike throughs 
"""
TODOs
- Function to link to the calc button
- Function should delete previous entrys & display results
- Function Should convert the hours into minutes (60 * Hours)
- Function should add up the total minutes 
- Function should divide the total minutes by the playback time (mins / playback speed)
- Function should convert the new minutes to display the hours or minutes it should now take 
"""














# * USER INTERFACE: This is the GUI for the program to
root = Tk()
root.title('Speed Learning Time Converter')
root.minsize(600,400)
root.maxsize(600,400)

titleLabel = Label(text = 'Time Converter', width = 20, font = ('Agency FB', 16, 'bold'),relief = RAISED)
titleLabel.grid(row = 0, column = 0, sticky = N, columnspan = 5, padx = 10, pady = 15, ipadx = 177)


normalPlaybackSpeedLabel = Label(text = 'What is the Normal Playback Time', font = ('Agency FB', 14), relief = GROOVE)
normalPlaybackSpeedLabel.grid(row = 1, pady = 30, column = 1, columnspan = 1, padx = 5, sticky = W)


hoursEntry = Entry(width = 10)
hoursEntry.grid(row = 1, column = 2, columnspan = 1, pady = 20, padx = 10)
hoursLabel = Label(text = "Hours", font = ('Agency FB', 12, 'italic'))
hoursLabel.grid(row = 1, column = 2, columnspan = 1, pady = 2, padx = 10, sticky = S)

minutesEntry = Entry(width = 10)
minutesEntry.grid(row = 1, column = 3, columnspan = 1, pady = 20, padx = 10)
minutesLabel = Label(text = "Minutes", font = ('Agency FB', 12, 'italic'))
minutesLabel.grid(row = 1, column = 3, columnspan = 1, pady = 2, padx = 10, sticky = S)


playbackSpeedLabel = Label(text = 'Playback Speed', font = ('Agency FB', 14), relief = GROOVE)
playbackSpeedLabel.grid(row = 2, pady = 30, column = 1, columnspan = 1, padx = 5, sticky = W, ipadx = 57)


playbackSpeedEntry = Entry(width = 10)
playbackSpeedEntry.grid(row = 2, column = 2, columnspan = 5, pady = 20, padx = 47, ipadx = 40, sticky = W)
playbackSpeedLabel = Label(text = "(e.g. 1.5)", font = ('Agency FB', 12, 'italic'))
playbackSpeedLabel.grid(row = 2, column = 2, columnspan = 5, pady = 2, padx = 105, sticky = SW)

calculateBtn = Button(text = 'CALCULATE', font = ('Agency FB', 14,' bold'))
calculateBtn.grid(row = 3, columnspan = 5, column = 1, padx = 95, pady = 30,rowspan = 3, ipadx = 120, sticky = W)

resultEnt = Entry(state = 'readonly', font = ('Agency FB', 12))
resultEnt.grid(row = 6, columnspan = 5, column = 1, padx = 5, pady = 25, ipadx = 180, sticky = SW)

resultsLabel = Label(text = 'Results', font = ('Agency FB', 14, 'bold'))
resultsLabel.grid(row = 6, columnspan = 5, column = 1, padx = 55, ipadx = 180, sticky = NW)









#! Allows the User Interface to show (WITHOUT THIS LINE IT WILL NOT SHOW)
root.mainloop()