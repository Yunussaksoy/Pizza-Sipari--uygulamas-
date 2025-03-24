import tkinter
from tkinter import *
PhotoImage
root = tkinter.Tk()
root.title("EHLİYET YAŞ BELİRLEME")
root.geometry("920x750")
root.configure(bg="DARK ORANGE")


def giriş():
    name = username_entry.get()
    date_of_birth = int(birthday_entry.get())
    current_year = 2024
    age = (current_year - date_of_birth)
    if age >= 18:
        print("SAYIN", name, age, "YAŞINDASINIZ", "EHLİYET ALABİLİRSİNİZ")
    else:
        print("SAYIN", name, age, "YAŞINDASINIZ", "EHLİYET İÇİN YAŞINIZ YETERLİ DEĞİL")


Label(root, text=" DOĞRU SÜRÜCÜ KURSU", font="ARİAL 50", fg="black", bg="yellow").pack()
Label(root, text="  ", width="11", bg="DARK ORANGE", height="1").pack()
##image = PhotoImage(file="C:\\Users\\EXCALIBUR\\Desktop\\batmansürücü.png") ##RESİM EKLEME 
##label = tkinter.Label(root, image=image)  ## KODUN ÇALIŞMASI İÇİN BU ALAN YORUMLANDI
##label.pack()
Label(root, text="  ", width="11", bg="DARK ORANGE", height="1").pack()
Label(root, text="EHLİYET YAŞ  FORMU", font="  ARİAL 30", fg="black", bg="yellow").pack()
Label(root, text="", width="11", bg="DARK ORANGE").pack()
Label(root, text="AD SOYAD GİRİNİZ :", bg="DARK ORANGE").pack()
username_entry = tkinter.Entry(root, width="70")
username_entry.pack()

Label(root, text="", width="11", bg="DARK ORANGE").pack()
Label(root, text="DOĞUM TARİHİNİZİ GİRİNİZ(YYY):", bg="DARK ORANGE").pack()
birthday_entry = tkinter.Entry(root, width="70")
birthday_entry.pack()
Label(root, text="", width="11", bg="DARK ORANGE").pack()

tkinter.Button(root, text="BAŞVURU YAP ", bg="GREEN", fg="white", font="verdana 10", width="20",
               command=giriş).pack()

root.mainloop()
