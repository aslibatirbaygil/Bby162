__author__ = "Aslı Batırbaygil"

import random
from tkinter import Tk, Label, Button

class GununKitabi:
    def __init__(self, anaSayfa):
        self.anaSayfa= anaSayfa
        anaSayfa.title=("Günün Kitabı")

        self.label= Label(anaSayfa, text="❆ Günün Kitabı ❆",font=("Arial",15),bg="light green")
        self.label.pack()

        self.kitap= Button(anaSayfa, text="Merhabalar",font=("arial",12), command= self.bilgi,bg="pink")
        self.kitap.pack()

        self.kitap_butonu= Button(anaSayfa, text="Günün Kitabını Göster",font=("arial",12),command=self.gunun_bilgisi,bg="orange")
        self.kitap_butonu.pack()

        self.kapat=Button(anaSayfa, text="Çıkış",font=("arial",12),command= anaSayfa.quit,bg="light blue")
        self.kapat.pack()

    def bilgi(self):
        print("Hoşgeldiniz!")

    def gunun_bilgisi(self):
        bilgiler=("The Dice Man / Zar Adam - Luke Rhinehart", "La Nausee / Bulantı - Jean-Paul Sartre", "The Unbearable Lightness of Being / Varolmanın Dayanılmaz Hafifliği - Milan Kundera","The Master and Margarita / Usta İle Margarita - Mikhail Bulgakov","On the Road / Yolda - Jack Kerouac","A Clockwork Orange / Otomatik Portakal - Anthony Burgess")
        secilenBilgi=random.choice(bilgiler)
        self.bilgiler= Label(self.anaSayfa, text=secilenBilgi)
        self.bilgiler.pack()

root=Tk()
my_gui=GununKitabi(root)
root.mainloop()