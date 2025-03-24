import tkinter as tk
form=tk.Tk()
form.geometry("600x600+500+200")
form.title("Pizza Sipariş Programı")
baslik=tk.Label(text="Pizza Sipariş Programına Hoşgeldiniz",fg="black",bg="blue",font="Times 17 italic").pack()

entr=tk.StringVar()
entr1=tk.StringVar()
ad=tk.Label(form,text="Ad-Soyad",bg="pink",font="times 12 italic").place(x=10,y=40)
boyut=tk.Label(form,text="Boyut",bg="pink",font="times 12 italic").place(x=10,y=70)
icindekiler=tk.Label(form,text="İcindekiler",bg="pink",font="times 12 italic").place(x=10,y=100)
adres=tk.Label(form,text="Adres",bg="pink",font="times 12 italic").place(x=10,y=130)

enty_ad=tk.Entry(textvariable=entr).place(x=100,y=40)
enty_adres=tk.Entry(textvariable=entr1).place(x=100,y=130)

Boyut=tk.StringVar()
kucuk=tk.Radiobutton(form,text="kücük boy",activebackground="green",value="kücük boy",variable=Boyut).place(x=90,y=70)
orta=tk.Radiobutton(form,text="Orte boy",activebackground="green",value="Orta boy",variable=Boyut).place(x=150,y=70)
buyuk=tk.Radiobutton(form,text="Büyük boy",activebackground="green",value="Büyük boy",variable=Boyut).place(x=220,y=70)

deger1=tk.StringVar()
deger2=tk.StringVar()
deger3=tk.StringVar()

check1=tk.Checkbutton(form,text="sucuklu",variable=deger1,onvalue="sucuklu").place(x=90,y=100)
check2=tk.Checkbutton(form,text="Mısır",variable=deger2,onvalue="Mısır").place(x=160,y=100)
check3=tk.Checkbutton(form,text="Acı Sos",variable=deger3,onvalue="Acı Sos").place(x=210,y=100)

def siparisver():
    siparis = tk.Label(text="Siparişiniz", fg="black", bg="blue", font="Times 17 italic").place(x=50, y=230)
    ad = tk.Label(form, text="Ad-Soyad", bg="pink", font="times 12 italic").place(x=10, y=270)
    boyut = tk.Label(form, text="Boyut", bg="pink", font="times 12 italic").place(x=10, y=300)
    icindekiler = tk.Label(form, text="İcindekiler", bg="pink", font="times 12 italic").place(x=10, y=330)
    adres = tk.Label(form, text="Adres", bg="pink", font="times 12 italic").place(x=10, y=360)

    ad1 = tk.Label(form, text=entr.get(), bg="pink", font="times 12 italic").place(x=120, y=270)
    boyut2 = tk.Label(form, text=Boyut.get(), bg="pink", font="times 12 italic").place(x=120, y=300)
    icindekiler3 = tk.Label(form, text=deger1.get()+" "+deger2.get()+" "+deger3.get(), bg="pink", font="times 12 italic").place(x=120, y=330)
    adres4 = tk.Label(form, text=entr1.get(), bg="pink", font="times 12 italic").place(x=120, y=360)
def iptal():
    pass
siparis=tk.Button(form,text="Sipriş Ver",activebackground="green",command=siparisver).place(x=150,y=160)
iptal=tk.Button(form,text="İptal Et",activebackground="red",command=iptal).place(x=220,y=160)





form.mainloop()
