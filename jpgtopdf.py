import os
from PIL import Image
import datetime

def create_pdf(pathlist, name, isDate):
    n = len(pathlist)
    imglist = []
    outputpath = os.getcwd()

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

