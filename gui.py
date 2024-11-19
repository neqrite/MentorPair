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