import numpy as np
from PIL import Image

# Als Graystufenbild speichern
#Weitere Modi: "1", 'L', 'P', 'RGB', 'RGBA', 'CMYK', 'YCbCr', 'HSV', "I", 'F'
im = np.array(Image.open('img/htl-logo.png').convert('L'))
#ist jetzt ein numpy-Array
print(im.shape) #(x,y)
print(im[0][0])
gr_im= Image.fromarray(im).save('img/htl-logo-gray.png')


#größe Ändern
img_small = np.array(Image.open('img/htl-logo.png').resize((200,200)))
Image.fromarray(img_small).save('img/htl-logo-small.png')


#Trimming (Bildausschnitt)
im = np.array(Image.open('img/htl-logo.png'))
im_trim = im[150:300, 330:1350]
Image.fromarray(im_trim).save('img/htl-logo-trim.png')

## Weitere Effekte

# Graustufen selbst berechnen
im_gray = np.mean(im, axis=2).astype(np.uint8)
Image.fromarray(im_gray).save('img/htl-logo-gray2.png')

# Schwarz-Weiß
im_gray[im_gray < 128] = 0
im_gray[im_gray >= 128] = 255
Image.fromarray(im_gray).save('img/htl-logo-bw.png')

# bild spiegeln
im_flip = np.fliplr(im)
Image.fromarray(im_flip).save('img/htl-logo-flip.png')

# Rot-Kanal abdrehen:
im_red = im.copy()
im_red[:,:,0] = 0
Image.fromarray(im_red).save('img/htl-logo-no_red.png')

# Rotes Gitter
im_raster = im.copy()
im_raster[ ::10,:,0] = 255
im_raster[ :,::10,0] = 255
Image.fromarray(im_raster).save('img/htl-logo-raster.png')


pos_red = np.where(im[:,:,0] > 128)
im_pos_red = im.copy()
print(im_pos_red.shape)
print(pos_red)
im_pos_red[pos_red[0], pos_red[1], :3] = [255,0, 0] #RGBA, alpha bleibt unverändert
print(im_pos_red.shape)
Image.fromarray(im_pos_red).save('img/htl-logo-pos_red.png')

# Schwarzes Rechteck im Zentrum
im_black_rect = im.copy()
im_black_rect[85:180, 85:180] = [0,0,0,255]  #RGBA
Image.fromarray(im_black_rect).save('img/htl-logo-black_rect.png')

