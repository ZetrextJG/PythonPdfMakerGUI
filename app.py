import tkinter as tk
from tkinter import filedialog, Text
import os

import custom_functions


#Creating window
root = tk.Tk()
root.title("PDF Converter")
root.resizable(False, False)


#Backgroud
canvas = tk.Canvas(root, height= 800, width= 600, bg="#5b5d66", border=False)
canvas.pack()


#Display
frame= tk.Frame(root, bg='#48454a')
frame.place(relwidth=0.88, relheight= 0.75, relx=0.06, rely=0.045)


#Variables
flipped = True
date_color1 = "#22a112"
date_color2 = "#c91818"
folder_path = os.getcwd()
NAME = tk.StringVar()
NAME.set("Name")

block_elements_list = []


#Functions
def update_board():
    for j in range(0, len(block_elements_list)):
        block_elements_list[j].number = j
        block_elements_list[j].create(0.08*j + 0.04)

def clear_board():
    for widget in frame.winfo_children():
            widget.place_forget()


#Classes
class BlockElement():
    
    def __init__(self, name, path, number):
        self.number = number
        self.path = path
        self.name = name
        self.xcord = 0.05
        self.BlockFrame = tk.Frame(frame, bg="#b1b6bd")
        self.text = tk.Label(self.BlockFrame, text=self.name, font=("Calibri", 11), bg="#ebf1fa")
        self.previewe_button = tk.Button(self.BlockFrame, text="Preview", command=self.initialize_preview)
        self.remove_button = tk.Button(self.BlockFrame, text="Remove", command=self.remove_element)
        self.upButton = tk.Button(self.BlockFrame, text="Up", command=self.moveUp)
        self.downButton = tk.Button(self.BlockFrame, text="Down", command=self.moveDown)

    def initialize_preview(self):
        custom_functions.preview(self.path)

    def remove_element(self):
        clear_board()
        global block_elements_list
        new_block_ele_list = []
        for x in block_elements_list:
            if not x.number == self.number:
                new_block_ele_list.append(x)
        block_elements_list = new_block_ele_list
        update_board()
        self.BlockFrame.destroy()

    def moveUp(self):
        if self.number != 0:
            clear_board()
            global block_elements_list
            temp = block_elements_list[self.number - 1]
            block_elements_list[self.number - 1] = block_elements_list[self.number]
            block_elements_list[self.number] = temp
            update_board()

    def moveDown(self):
        global block_elements_list
        if self.number != len(block_elements_list) - 1:
            clear_board()
            temp = block_elements_list[self.number + 1]
            block_elements_list[self.number + 1] = block_elements_list[self.number]
            block_elements_list[self.number] = temp
            update_board()


    def create(self, ycord):
        self.BlockFrame.place(relx = self.xcord, rely = ycord, relheight= 0.07, relwidth= 0.9)
        self.text.place(relx = self.xcord, rely= 0.22)
        self.previewe_button.place(relx = 0.52, rely= 0.22)
        self.remove_button.place(relx = 0.65, rely= 0.22)
        self.upButton.place(relx=0.785, rely=0.22)
        self.downButton.place(relx=0.86, rely=0.22)


#Entry
nameEntry  = tk.Entry(root, bg="#b5b5c4", border=False, fg="#010412")
nameEntry.place(relwidth=0.2, relheight = 0.04, relx=0.14, rely= 0.82)
nameEntry["textvariable"] = NAME


#Text
text = tk.Label(root, text="PDF Name:", font=("Calibri", 11), bg="#5b5d66")
text.place(relx=0.014, rely= 0.824)

text_output_dir = tk.Label(root, text=os.getcwd(), font=("Calibri", 13), bg="#5b5d66")
text_output_dir.place(relx=0.21, rely=0.949)

text2 = tk.Label(root, text="Include DATE", font=("Calibri", 11), bg=date_color1, bd=2)
text2.place(relwidth=0.2, relheight = 0.04, relx=0.14, rely= 0.88)


#Buttons
def change_color():
    global flipped
    if(flipped):
        text2.configure(text="Exclude DATE", bg=date_color2)
        flipped = False
    else:
        text2.configure(text="Include DATE", bg=date_color1)
        flipped= True

switchButton = tk.Button(root, text="On/off Date", bg="#9fa83d", command=change_color)
switchButton.place(relx=0.014, rely= 0.884)


def change_output_dir():
    global folder_path
    folder_path = filedialog.askdirectory(initialdir=os.getcwd(), title="Choose output directory")
    text_output_dir.configure(text=folder_path)

outputdirButton = tk.Button(root, text="Choose output dir",command=change_output_dir)
outputdirButton.place(relx=0.014, rely=0.95)


def loadimg():
    clear_board()

    filenames = filedialog.askopenfilenames(initialdir="/", title="Select Images", filetypes=(("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("All files", "*.*")))
    for i, one_path in enumerate(filenames):
        temp_name = one_path.split("/")[-1]
        if len(temp_name) > 24:
            temp_name = temp_name[:20] + "..." + temp_name[-4:]
        one_element = BlockElement(temp_name, one_path, i)
        block_elements_list.append(one_element)
    
    update_board()

fileButton = tk.Button(root, text="Load Files", command=loadimg)
fileButton.place(relx=0.56, rely= 0.812, relheight= 0.052, relwidth = 0.28)


def make_pdf():
    global block_elements_list

    if len(block_elements_list) == 0:
        pass
    else:
        loaded_img = [x.path for x in block_elements_list]
        custom_functions.create_pdf(loaded_img, NAME.get(), flipped, outputpath=folder_path)

        for widget in frame.winfo_children():
            widget.destroy()
        
        block_elements_list = []
        NAME.set("Name")

pdfButton = tk.Button(root, text="Make PDF", command=make_pdf)
pdfButton.place(relx=0.56, rely= 0.888, relheight= 0.052, relwidth = 0.28)


#RUN app
root.mainloop()