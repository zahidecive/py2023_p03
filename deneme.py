from tkinter import *
from PIL import ImageTk, Image

pencere = Tk()
pencere.title("Sabahattin Ali'nin Kitapları")
#pencere.iconbitmap("ico/kitap.ico")
pencere.geometry("750x650")

pencere1 = Toplevel(pencere)
pencere1.title("Veri Seti Analizi - 2. Sayfa")
pencere1.geometry("400x300")


gorsel = ImageTk.PhotoImage(Image.open("img/kitap_01.jpg"))

def fotoTutucu():
    gorselTutucu = Label(image=gorsel)
    gorselTutucu.pack()

    butonum = Button(pencere, text="Foto Göster", command=fotoTutucu)
    butonum.pack()

    pencere.mainloop()
def yenipencere():
    pencere = Toplevel()
    buton2 = Button(pencere2, text="Önceki sayfaya dön", width=20, height=5, fg="red", bg="green")
    buton4 = Button(pencere2, text="Sonraki sayfaya git", fg="black", bg="green", width=20, height=5)

    buton2.pack()
    buton4.pack()


buton1 = Button(text="Menü", command=yenipencere)
buton3 = Button(text="Çıkış", fg="white", bg="red", command=pencere.quit)
buton1.pack()
buton3.pack()

pencere.mainloop()
pencere2.mainloop()