import tkinter as tk
from tkinter import filedialog, Text
import os

import jpgtopdf


#Creating window
root = tk.Tk()
root.title("PDF Converter")
root.resizable(False, False)


#Backgroud
canvas = tk.Canvas(root, height= 800, width= 600, bg="#5b5d66", border=False)
canvas.pack()


#Display
frame= tk.Frame(root, bg='#48454a')
frame.place(relwidth=0.87, relheight= 0.75, relx=0.05, rely=0.05)

#Variables
flipped = True
date_color1 = "#22a112"
date_color2 = "#c91818"
NAME = tk.StringVar()
NAME.set("Name")
loaded_img = []
display_name = []
elements_list = []


#Classes
class BlockElement():
    def __init__(self, name, path):
        self.path = path
        self.name = name
        self.xcord = 0.05
        self.BlockFrame = tk.Frame(frame, bg="#b1b6bd")
        self.text = tk.Label(self.BlockFrame, text=self.name, font=("Calibri", 11), bg="#ebf1fa")
    
    def create(self, ycord):
        self.BlockFrame.place(relx = self.xcord, rely = ycord, relheight= 0.07, relwidth=0.9)
        self.text.place(relx = self.xcord, rely= 0.22)
        
#Functions
def print_conent(event):
    print(f'NAME === > {NAME.get()}')




#Entry
nameEntry  = tk.Entry(root, bg="#b5b5c4", border=False, fg="#010412")
nameEntry.place(relwidth=0.2, relheight = 0.04, relx=0.14, rely= 0.85)

nameEntry["textvariable"] = NAME
nameEntry.bind('<Key-Return>', print_conent)


#Text
text = tk.Label(root, text="PDF Name:", font=("Calibri", 11), bg="#5b5d66")
text.place(relx=0.014, rely= 0.854)


#Buttons


text2 = tk.Label(root, text="Include DATE", font=("Calibri", 11), bg=date_color1, bd=2)
text2.place(relwidth=0.2, relheight = 0.04, relx=0.14, rely= 0.92)

def change_color():
    global flipped
    if(flipped):
        text2.configure(text="Exclude DATE", bg=date_color2)
        flipped = False
    else:
        text2.configure(text="Include DATE", bg=date_color1)
        flipped= True


switchButton = tk.Button(root, text="On/off Date", bg="#9fa83d", command=change_color)
switchButton.place(relx=0.014, rely= 0.924)

def loadimg():
    for widget in frame.winfo_children():
        widget.destroy()

    filenames = filedialog.askopenfilenames(initialdir="/", title="Select Images", filetypes=(("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("All files", "*.*")))
    loaded_img.extend(filenames)
    display_name = []

    for x in loaded_img:
        display_name.append(x.split("/")[-1])

    print(display_name)

    elements_list = []
    for i, namejd in enumerate(display_name):
        beee = BlockElement(namejd, loaded_img[i])
        beee.create(0.08*i + 0.04)
        elements_list.append(beee)



fileButton = tk.Button(root, text="Load Files", command=loadimg)
fileButton.place(relx=0.56, rely= 0.842, relheight= 0.052, relwidth = 0.28)


def make_pdf():
    jpgtopdf.create_pdf(loaded_img, NAME.get(), flipped)


pdfButton = tk.Button(root, text="Make PDF", command=make_pdf)
pdfButton.place(relx=0.56, rely= 0.918, relheight= 0.052, relwidth = 0.28)


#RUN app
root.mainloop()