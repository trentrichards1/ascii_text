#!/usr/bin/env python3

from PIL import Image, ImageOps
from tkinter import filedialog as fd

wPixels,brightness,step = 200,255,19

def main():

    global wPixels,brightness,step
    filename = fd.askopenfilename()
    originalImage = Image.open(filename)
    wPercent = (wPixels/float(originalImage.size[0]))
    hPixels = int((float(originalImage.size[1])*float(wPercent))*.35)
    grayImage = originalImage.resize((wPixels,hPixels), Image.Resampling.LANCZOS).convert('L')
    #resizedImage.save('mypic.png')
    #grayImage = ImageOps.grayscale(resizedImage)
    grayImage.save('mypic.png')
    pixelValues = list(grayImage.getdata())
    #print(pixelValues)
    x=0
    for i in pixelValues:
        #@%#*+=-:.
        x+=1
        # print(i)
        if x%wPixels == 0:
            print("\n", end="")
        if i >= (brightness-step*3):
            print(" ", end="")
        elif i >= (brightness-step*4):
            print(".", end="")
        elif i >= (brightness-step*5):
            print(",", end="")
        elif i >= (brightness-step*6):
            print("-", end="")
        elif i >= (brightness-step*7):
            print(":", end="")
        elif i >= (brightness-step*8):
            print("=", end="")
        elif i >= (brightness-step*9):
            print("+", end="")
        elif i >= (brightness-step*10):
            print("*", end="")
        elif i >= (brightness-step*11):
            print("#", end="")
        elif i >= (brightness-step*12):
            print("%", end="")
        else:
            print("@", end="")

main()