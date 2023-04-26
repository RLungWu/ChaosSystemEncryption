from PIL import Image,ImageTk
import tkinter as tk
from tkinter.constants import *
from tkinter import filedialog
from encryption import encry
from decryption import decry


def browse_image():
    filename = filedialog.askopenfilename()
    image = Image.open(filename)
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(image=photo)
    label.image = photo
    label.pack()

def test():
    print('hi')


def main():
    window = tk.Tk()
    window.title('Chaos')
    window.geometry('420x460')
    window.resizable(False, False)
    window.iconbitmap('icon.ico')#程式的圖檔

    upload = tk.Button(text='Upload', command=browse_image)
    upload.place(x = 10,y=10)

    enc = tk.Button(text='Encryption')
    enc. place(x = 150, y = 10)

    dec = tk.Button(text='Decryption')
    dec.place(x=150, y = 40)

    download = tk.Button(text='Download')
    download.place(x=300, y=10)

    

    window.mainloop()


if __name__ == '__main__':
    main()