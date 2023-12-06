from tkinter import *
import xml.etree.ElementTree as ET
from PIL import ImageTk, Image

pencere = Tk()
pencere.title("XML Project")
pencere.geometry("850x600")

navigasyon = 0

def navigasyon(direction):
    global kapak
    if direction == 'ileri':
        kapak = (kapak+1)% len(kapaklar)
    elif direction == 'geri':
        kapak = (kapak-1)% len(kapaklar)

        goster()

def ileriGit():
    global navigasyon
    navigasyon +=1
    goster(navigasyon)

def geriGit():
    global navigasyon
    navigasyon -=1
    goster(navigasyon)

tree = ET.parse('veriseti.xml')
root = tree.getroot()

def goster(navigasyon):
    resim = root[navigasyon][1].text
    icerik = root[navigasyon][0].text
    print(root[navigasyon][0].text)

    gorsel = ImageTk.PhotoImage(Image.open(resim))
    cerceve = Label(image=gorsel)
    cerceve.image = gorsel
    cerceve.grid(row=3, columnspan=2, padx= 10, pady=10)

    metin = Label(pencere, text=icerik)
    metin.grid(row=2, columnspan=2, padx= 10, pady=10)

ileriButon = Button(pencere, text="İleri", command=ileriGit)
geriButon = Button(pencere, text="Geri", command=geriGit)

ileriButon.grid(row=1, column=1, padx= 10, pady=10)
geriButon.grid(row=1, column=0, padx= 10, pady=10)

goster(navigasyon)

pencere.mainloop()