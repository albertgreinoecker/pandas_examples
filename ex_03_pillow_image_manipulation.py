import numpy as np
from PIL import Image

# Als Graystufenbild speichern
#Weitere Modi: "1", 'L', 'P', 'RGB', 'RGBA', 'CMYK', 'YCbCr', 'HSV', "I", 'F'
# im = np.array(Image.open('img/htl-logo.png').convert('L'))
# #ist jetzt ein numpy-Array
# print(im.shape) #(x,y)
# print(im[0][0])
# gr_im= Image.fromarray(im).save('img/htl-logo-gray.png')


#größe Ändern
img_small = np.array(Image.open('img/htl-logo.png').resize((200,200)))
Image.fromarray(img_small).save('img/htl-logo-small.png')


#Trimming (Bildausschnitt)
im = np.array(Image.open('img/htl-logo.png'))
im_trim = im[150:300, 330:1350]
Image.fromarray(im_trim).save('img/htl-logo-trim.png')