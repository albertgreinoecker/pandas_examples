from tkinter import *
from PIL import Image, ImageTk
import cv2
from ex_03_pillow_steganograpy import encode_in_image, extract_from_image


root = Tk()
root.title("Steganographie")
root.geometry("1800x1600")

root.configure(background='lightgray')

label = Label(root)
label.frame_num = 0
label.grid(row=0, column=0)
cap= cv2.VideoCapture(0)

text = Text(root, height=20, width=80)
text.insert(END, "Any Text")
text.grid(row=0, column=1,  padx=(30, 10))



labelPic1 = Label(root, text="Bild ohne Nachricht")
labelPic1.grid(row=3, column=0)

labelPic2 = Label(root, text="Bild mit Nachricht")
labelPic2.grid(row=3, column=1)

labelResult = Label(root, text="...")
labelResult.grid(row=4, column=1)

logo = Image.open('out/wii.png')
imgL = ImageTk.PhotoImage(logo)
labelLogo = Label(root, image=imgL)
labelLogo.grid(row=5, column=0)

def take_pic():
    file_name = "out/campic.png"
    imagetk = label.imgtk
    imgpil = ImageTk.getimage( imagetk )
    imgpil.save(file_name, "PNG")
    imgpil.close()
    t = text.get("1.0",END)
    print(t)
    encoded_im = encode_in_image('out/campic.png', t)
    encoded_im.save('out/campic-msg.png')

    img1 = Image.open('out/campic.png')
    img1 = ImageTk.PhotoImage(img1)
    labeli1 = Label(root, image=img1)
    labeli1.grid(row=2, column=0)

    img2 = Image.open('out/campic-msg.png')
    img2 = ImageTk.PhotoImage(img2)
    labeli2 = Label(root, image=img2)
    labeli2.grid(row=2, column=1)

    img1 = Image.open('out/campic.png')
    img1 = ImageTk.PhotoImage(img1)
    labeli1.configure(image=img1)
    labeli1.image = img1


    img2 = Image.open('out/campic-msg.png')
    img2 = ImageTk.PhotoImage(img2)
    labeli2.configure(image=img2)
    labeli2.image = img2

def send():
    print('send')
    decoded_text = extract_from_image('out/campic-msg.png')
    print(decoded_text)
    labelResult.config(text=decoded_text)

button_frame = Frame(root, width=200, height=400, bg='grey')
button_frame.grid(row=1, column=1, padx=10, pady=5)

start = Button(button_frame, text="encode", command=take_pic).grid(row=1, column=1)
send = Button(button_frame, text="decode", command=send).grid(row=1, column=2)

if not cap.isOpened():
    print("Cannot open camera")


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