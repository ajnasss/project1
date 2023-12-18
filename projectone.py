from tkinter import *
from functools import reduce
from collections import Counter
deger=Tk()
deger.title("console menu")
canvas=Canvas(deger,height=700,width=900)
canvas.pack()
frame1=Frame(deger,bg="#add8e6")
frame1.place(relx=0.1,rely=0.09,relwidth=0.75,relheight=0.05)
etiket=Label(frame1,bg="#add8e6",font="Verdana 12 bold")
etiket.pack()
frame2=Frame(deger,bg="#add8e6")
frame2.place(relx=0.1,rely=0.16,relwidth=0.75,relheight=0.05)
etiket2=Label(frame2,bg="#add8e6",font="Verdana 12 bold")
etiket2.pack()
frame3=Frame(deger,bg="#add8e6")
frame3.place(relx=0.1,rely=0.23,relwidth=0.75,relheight=0.05)
etiket3=Label(frame3,bg="#add8e6",font="Verdana 12 bold")
etiket3.pack()
frame4=Frame(deger,bg="#add8e6")
frame4.place(relx=0.1,rely=0.3,relwidth=0.75,relheight=0.05)
etiket4=Label(frame4,bg="#add8e6",font="Verdana 12 bold")
etiket4.pack()
frame5=Frame(deger,bg="#add8e6")
frame5.place(relx=0.1,rely=0.37,relwidth=0.75,relheight=0.05)
etiket5=Label(frame5,bg="#add8e6",font="Verdana 12 bold")
etiket5.pack()
frame6=Frame(deger,bg="#add8e6")
frame6.place(relx=0.1,rely=0.45,relwidth=0.75,relheight=0.05)
etiket6=Label(frame6,bg="#add8e6",font="Verdana 12 bold")
etiket6.pack()
frame7=Frame(deger,bg="#add8e6")
frame7.place(relx=0.1,rely=0.52,relwidth=0.75,relheight=0.05)
etiket7=Label(frame7,bg="#add8e6",font="Verdana 12 bold")
etiket7.pack()
frame8=Frame(deger,bg="#add8e6")
frame8.place(relx=0.1,rely=0.59,relwidth=0.75,relheight=0.05)
etiket8=Label(frame8,bg="#add8e6",font="Verdana 12 bold")
etiket8.pack()
frame9=Frame(deger,bg="#add8e6")
frame9.place(relx=0.1,rely=0.65,relwidth=0.75,relheight=0.05)
etiket9=Label(frame9,bg="#add8e6",font="Verdana 12 bold")
etiket9.pack()
frame10=Frame(deger,bg="#add8e6")
frame10.place(relx=0.1,rely=0.72,relwidth=0.75,relheight=0.05)
etiket10=Label(frame10,bg="#add8e6",font="Verdana 12 bold")
etiket10.pack()
frame11=Frame(deger,bg="#add8e6")
frame11.place(relx=0.1,rely=0.79,relwidth=0.75,relheight=0.05)
etiket11=Label(frame11,bg="#add8e6",font="Verdana 12 bold")
etiket11.pack()

def k_kucuk():
    aranansira=int(input('listenin kacinci siradaki elemanini ariyorsunuz: '))
    lista=int(input('listede kac sayi olmasini istiyorsunuz: '))
    liste=[]
    for i in range(0,lista):
        aa=int(input('liste icin istediginiz sayi:'))
        liste.append(aa)
    k=sorted(liste)
    print(k[aranansira-1])
    return
def tekrareden_sayılar():
    lista=int(input('listede kac sayi olmasini istiyorsunuz: '))
    liste=[]
    for i in range(0,lista):
        aa=int(input('liste icin istediginiz sayi:'))
        liste.append(aa)
    return print([eleman for eleman in set(liste) if liste.count(eleman) > 1])
def kelime_frekanslari_bul():
    with open('giris_metni.txt', 'r', encoding='utf-8') as dosya:
        metin = dosya.read()
        kelimeler = metin.split()
        frekanslar = reduce(lambda x, y: Counter(x) + Counter(y), map(lambda kelime: [kelime], kelimeler))
        kelimefrekanslari=dict(frekanslar)
        for kelime, frekans in kelimefrekanslari.items():
            print(f"{kelime}: {frekans}")
    return
def enkucukdeger():
    lista = int(input('listede kac sayi olmasini istiyorsunuz: '))
    liste = []
    for i in range(0, lista):
        aa = int(input('liste icin istediginiz sayi:'))
        liste.append(aa)
    if len(liste)==0:
        return None
    enkucuk=liste[0]

    for eleman in liste:
        if eleman < enkucuk:
            enkucuk=eleman
    print(enkucuk)
    return
def en_yakin_cift():
    hedef_sayi=int(input('yakin olmasini istediginiz sayiyi giriniz: '))
    lista = int(input('listede kac sayi olmasini istiyorsunuz: '))
    liste = []
    for i in range(0, lista):
        aa = int(input('liste icin istediginiz sayi:'))
        liste.append(aa)
    liste.sort()
    en_yakin_cift = None
    en_kucuk_fark = float('inf')

    for i in range(len(liste) - 1):
        for j in range(i + 1, len(liste)):
            toplam = liste[i] + liste[j]
            fark = abs( hedef_sayi- toplam)
            if fark < en_kucuk_fark:
                en_kucuk_fark = fark
                en_yakin_cift = (liste[i], liste[j])

    return print(en_yakin_cift)
def matrixcarpimi():
    satir_sayisi = int(input("1. Matrisin satır sayısını girin: "))
    sutun_sayisi = int(input("1. Matrisin sütun sayısını girin: "))
    matris1 = []
    print("1. Matrisin elemanlarını girin:")
    for i in range(satir_sayisi):
        satir = []
        for j in range(sutun_sayisi):
            eleman = int(input(f"({i + 1}, {j + 1}) elemanını girin: "))
            satir.append(eleman)
        matris1.append(satir)
    satir_sayisi2 = int(input("2. Matrisin satır sayısını girin: "))
    sutun_sayisi2 = int(input("2. Matrisin sütun sayısını girin: "))
    matris2 = []
    print("2. Matrisin elemanlarını girin:")
    for g in range(satir_sayisi2):
        satir2 = []
        for u in range(sutun_sayisi2):
            eleman2 = int(input(f"({g + 1}, {u + 1}) elemanını girin: "))
            satir2.append(eleman2)
        matris2.append(satir2)
    if sutun_sayisi != satir_sayisi2:
        print("Matrislerin çarpımı için uygun boyutlar değil!")
    else:
        carpim_matrisi = [[sum(a * b for a, b in zip(matris1_row, matris2_col)) for matris2_col in zip(*matris2)] for
                          matris1_row in matris1]
        for row in carpim_matrisi:
            print(row)
    return
def EBOB_bulma():
    sayi1 = int(input("Birinci sayıyı girin: "))
    sayi2 = int(input("İkinci sayıyı girin: "))
    while sayi2 != 0:
        sayi1, sayi2 = sayi2, sayi1 % sayi2
    return print(sayi1)
def asal_kontrol():
    sayi = int(input("Bir sayı girin: "))
    if sayi <= 1:
        return False, print('asal degil')
    for i in range(2, int(sayi**0.5) + 1):
        if sayi % i == 0:
            return False, print('asal degil')
    return True,print('asal')
def karekok():
    N=int(input("sayi giriniz: "))
    x0 = N
    maxiter = 10
    iterasyon = 0
    tol = 1e-10
    while True:
        x1 = 0.5 * (x0 + N / x0)
        hata = abs(x1 ** 2 - N)
        if hata < tol or iterasyon >= maxiter:
            break
        x0 = x1
        iterasyon += 1
    if iterasyon >= maxiter:
        print(f"{maxiter} iterasyonda sonuca ulaşılamadı. 'hata' veya 'maxiter' değerlerini değiştirin")
    else:
        print(f"{iterasyon} iterasyonda sonuca ulaşıldı.")
    karekok_sonucu = x1
    print(f"Karekök: {karekok_sonucu}")
    return
def fibonacci():
    def fib(n):
        if n <= 1:
            return n
        else:
            return fib(n - 1) + fib(n - 2)

    sayi = int(input("Kaç terimli Fibonacci dizisi oluşturmak istiyorsunuz: "))
    for i in range(sayi):
        print(fib(i), end=", ")
    print()
var=IntVar()
R1=Radiobutton(etiket,text="1) k inci kucuk eleman",variable=var,value=1,bg="#add8e6",font="Verdana 12 bold",command=k_kucuk)
R1.pack(anchor=NW,pady=5,padx=5)
R2=Radiobutton(etiket2,text="2) en yakin cifti bulma",variable=var,value=2,bg="#add8e6",font="Verdana 12 bold",command=en_yakin_cift)
R2.pack(anchor=NW,pady=5,padx=5)
R3=Radiobutton(etiket3,text="3) listenin tekrar eden elemanlarini bulma",variable=var,value=3,bg="#add8e6",font="Verdana 12 bold",command=tekrareden_sayılar)
R3.pack(anchor=NW,pady=5,padx=5)
R4=Radiobutton(etiket4,text="4) matris carpimi",variable=var,value=4,bg="#add8e6",font="Verdana 12 bold",command=matrixcarpimi)
R4.pack(anchor=NW,pady=5,padx=5)
R5=Radiobutton(etiket5,text="5) text dosyasındaki kelimelerin frekansını bulma",variable=var,value=5,bg="#add8e6",font="Verdana 12 bold",command=kelime_frekanslari_bul)
R5.pack(anchor=NW,pady=5,padx=5)
R6=Radiobutton(etiket6,text="6) liste icinde en kucuk degeri bulma",variable=var,value=6,bg="#add8e6",font="Verdana 12 bold",command=enkucukdeger)
R6.pack(anchor=NW,pady=5,padx=5)
R7=Radiobutton(etiket7,text="7) karekok fonksiyonu",variable=var,value=7,bg="#add8e6",font="Verdana 12 bold",command=karekok)
R7.pack(anchor=NW,pady=5,padx=5)
R8=Radiobutton(etiket8,text="8) en buyuk ortak boleni bulma",variable=var,value=8,bg="#add8e6",font="Verdana 12 bold",command=EBOB_bulma)
R8.pack(anchor=NW,pady=5,padx=5)
R9=Radiobutton(etiket9,text="9)asal olan sayiyi bulma",variable=var,value=9,bg="#add8e6",font="Verdana 12 bold",command=asal_kontrol)
R9.pack(anchor=NW,pady=5,padx=5)
R10=Radiobutton(etiket10,text="10) daha hızlı fibonacci hesabı",variable=var,value=10,bg="#add8e6",font="Verdana 12 bold",command=fibonacci)
R10.pack(anchor=NW,pady=5,padx=5)
R11=Radiobutton(etiket11,text="cıkıs",value=11,bg="#add8e6",font="Verdana 12 bold",command=deger.quit)
R11.pack(anchor=NW,pady=5,padx=5)
deger.mainloop()