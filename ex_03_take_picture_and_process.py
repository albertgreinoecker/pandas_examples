from tkinter import *
from PIL import Image, ImageTk
import cv2

root = Tk()
root.geometry("1600x1600")

label = Label(root)
label.frame_num = 0
label.grid(row=0, column=0)
cap= cv2.VideoCapture(0)

text = Text(root, height=5, width=130)
text.insert(END, "Dieser Text soll verschlüsselt werden")
text.grid(row=0, column=1)

img1 = Image.open('out/campic.png')
img1 = ImageTk.PhotoImage(img1)
labeli1 = Label(root, image=img1)
labeli1.grid(row=2, column=0)

img2 = Image.open('out/campic-msg.png')
img2 = ImageTk.PhotoImage(img2)
labeli2 = Label(root, image=img2)
labeli2.grid(row=2, column=1)

def take_pic():
    file_name = "out/campic.png"
    imagetk = label.imgtk
    imgpil = ImageTk.getimage( imagetk )
    imgpil.save(file_name, "PNG")
    imgpil.close()

start = Button(root, text="start", command=take_pic)
start.grid(row=1, column=1)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

def show_frames():
   cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
   img = Image.fromarray(cv2image)
   imgtk = ImageTk.PhotoImage(image = img)
   label.imgtk = imgtk
   label.frame_num += 1.
   label.configure(image=imgtk)
   label.after(20, show_frames)

def key_pressed(event):
   take_pic()

show_frames()
root.bind("p", key_pressed)
root.mainloop()