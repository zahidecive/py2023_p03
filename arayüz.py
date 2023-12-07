from tkinter import *
from PIL import ImageTk, Image

pencere = Tk()
pencere.title("Resim Albümü")
pencere.geometry('750x750')

baslik = Label(pencere, text="Veri Bilimi Kitapları")
baslik.grid(row=0, column=0, padx= 10, pady=10)
baslik.config(font=("Arial", 30))

kapaklar = ["img/kitap_01.jpg", "img/kitap_02.jpg", "img/kitap_03.jpg", "img/kitap_04.jpg", "img/kitap_05.jpg"]

kapak = 0

def goster():
    gorsel = ImageTk.PhotoImage(Image.open(kapaklar[kapak]))
    cerceve = Label(image=gorsel)
    cerceve.image = gorsel
    cerceve.grid(row=1, column=0, padx= 10, pady=10)

goster()

metinLabel = Label(pencere, text="Metin", wraplength=400)
metinLabel.grid(row=2, column=0, padx=10, pady=10)
metinLabel.config(font=('Arial',20))

def navigasyon(direction):
    global kapak
    if direction == 'ileri':
        kapak = (kapak+1)% len(kapaklar)
    elif direction == 'geri':
        kapak = (kapak-1)% len(kapaklar)

    goster()

metinLabel.config(text="Görüntülenen resim: " + kapaklar[kapak])


ileriButon = Button(pencere,text= 'İleri', command=lambda: navigasyon('ileri'))
geriButon = Button(pencere,text= 'Geri', command=lambda: navigasyon('geri'))


buton = Button(text= 'Diğer Kitapları', command=lambda: navigasyon('ileri'))
buton.grid(row=2, column=0, padx=10, pady=10)
buton.config(font=('Arial',20))
ileriButon.grid(row=1, column=1, padx=0, pady=10)
geriButon.grid(row=1, column=2, padx=100, pady=100)


pencere.mainloop()