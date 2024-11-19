import tkinter as tk
from tkinter import filedialog

def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    print('Selected:', filename)

root = tk.Tk()
root.geometry("700x700")

button = tk.Button(root, text='Open', command=UploadAction)
button.pack()

label = tk.Label(root, text='Full name:')

root.mainloop()

'''
class pair(name, matches):
    def __init__(self):
        self.name = name
        self.matches = 0

topMatches = [] # array containing an array for each student's top matches

for i in range numStudents:
    for j in range numMentors:
        matches = 0

        for i in mentorSubjects:
            if mentorSubjects[i] in mentorSubjects:
                matches++

        # while matches > num matches in topmatches array for this student
        #   move through the array
        # insert in (if not greater do not insert.) Upon insertion if there are more than MAXSUGGESTIONS matches
        # in the array remove the least matched mentor. (Might make it so each one could be a linked list of ties as well...)


code that outputs this information
'''