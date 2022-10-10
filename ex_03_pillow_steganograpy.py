from PIL import Image
import numpy as np
import bitarray as ba # Here used for conversion from string to bit  and vice versa

def encode_text(text, encoding='utf-8'):
    arr = ba.bitarray()
    arr.frombytes(text.encode(encoding)) # read string as bytes and convert to bytearray
    return arr.tolist() # We need a normal python list

def decode_text(bits, encoding='utf-8'):
    bits = bits.astype(str) #we need strings of the bites
    x = ''.join(bits) #make one string
    return ba.bitarray(x).tobytes().decode(encoding) # make bytes out of bits and decode them to string

def encode_in_image(filename, text_message):
    input_im = Image.open(filename, 'r').convert("RGB")
    img =  np.asarray(input_im) # is now a 3-dim numpy array

    extracted = np.bitwise_and(img ,254) # remove the last bits from each 3-dim matrix entry
    encoded_text = encode_text(text_message + "<STOP>") # encode the text to bits
    encoded_text = np.resize(encoded_text,img.shape).astype('b') # text bits have now the same shape as the image (bits of strings are repeated automatically)

    img_with_msg = np.bitwise_or(extracted, encoded_text) # first seven bits from image - the last one from text
    return Image.fromarray(np.uint8(img_with_msg)).convert('RGB') # generate an image out of the ndarray

def extract_from_image(filename):
    encoded_im = np.asarray(Image.open(filename, 'r').convert("RGB")) # read dnarray from image
    extracted_bits = np.bitwise_and(encoded_im, 1).flatten() # take the last bit and write all in a one-dim array
    return decode_text(extracted_bits).split('<STOP>')[0] # text is stored repeated until end. Take the first occurrence

encoded_im = encode_in_image('out/campic.png', "HTL is supercool!*")
encoded_im.save('out/campic-msg.png')

msg = extract_from_image('out/campic-msg.png')
print(msg)