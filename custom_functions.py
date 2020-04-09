import os
import tkinter as tk
from PIL import Image, ImageTk
import datetime
import math

def create_pdf(pathlist, name, isDate, outputpath):
    n = len(pathlist)
    imglist = []

    if n == 1:
        img  = Image.open(pathlist[0])
        img.convert('RGB')
        if isDate:
            img.save(outputpath + r"\\" + name + r"_" + str(datetime.datetime.now())[:10] + r".pdf")
        else:
            img.save(outputpath + r"\\" + name + r".pdf")
    else:
        img1 = Image.open(pathlist[0])
        img1.convert('RGB')
        for x in range(1, n):
            img = Image.open(pathlist[x])
            imglist.append(img.convert('RGB'))

        if isDate:
            img1.save(outputpath + r"\\" + name + r"_" + str(datetime.datetime.now())[:10] + r".pdf", save_all=True, append_images=imglist)
        else:
            img1.save(outputpath + r"\\" + name + r".pdf", save_all=True, append_images=imglist)

def resize(width, height, img_loaded):
    a = math.ceil(width / 1080)
    b = math.ceil(height / 720)
    if a >= b:
        new_width = round(width / a)
        new_height = round(height /a)
    else:
        new_width = round(width / b)
        new_height = round(height /b)

    return img_loaded.resize((new_width, new_height), Image.ANTIALIAS)

def preview(new_path1):
    new_root = tk.Tk()
    new_root.resizable(False, False)
    load = Image.open(new_path1)

    if load.size[0] > 1080 or load.size[1] > 720 : 
        load = resize(load.size[0], load.size[1], load)

    new_frame = tk.Frame(new_root, height= load.size[1], width= load.size[0], borderwidth=0)
    new_frame.pack()
    render = ImageTk.PhotoImage(load, master = new_frame)
    img = tk.Label(new_frame, image=render, borderwidth=0)
    img.image = render
    img.place(x=0, y=0)

    new_root.title("Image Preview")
    new_root.mainloop()
