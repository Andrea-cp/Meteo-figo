import tkinter as tk
from tkinter import *
from tkinter import messagebox as mBox
from PIL import Image, ImageTk
from backend import *


coloreScuro='#17212B'
coloreChiaro='#80c1ff'

def chiudi():
    finestra.destroy()

def reset_variabili():
    idCitta.set("")
    nome.set("")
    lon.set("")
    lat.set("")
    nazione.set("")
    temperatura_corr.set("")
    temperatura_max.set("")
    temperatura_min.set("")
    umidita.set("")
    ultimo_aggiornamento.set("")
    txt_nome_citta.set("")
    canvas.delete("all")
    canvas.configure(bg=bg)

def cerca():

    citta = str(nome_citta.get())

    if(citta==""):
        mBox.showinfo("Errore","Campo vuoto!!")
        reset_variabili()
    else:
        meteo.setta_parametri(citta)
        if(meteo.errore==0):
            idCitta.set(meteo.id_citta)
            nome.set(meteo.nome)
            lon.set(meteo.lon+"°")
            lat.set(meteo.lat+"°")
            nazione.set(meteo.nazione)
            temperatura_corr.set(meteo.temperatura_corrente+"°")
            temperatura_max.set(meteo.temperatura_massima+"°")
            temperatura_min.set(meteo.temperatura_minima+"°")
            umidita.set(meteo.umidita)
            ultimo_aggiornamento.set(meteo.ultimo_aggiornamento)

            canvas.delete("all")
            tmp = meteo.tempo_metereologico_icon
            img = ImageTk.PhotoImage(Image.open("image_icon/" + tmp + "@2x.png"))
            canvas.create_image(0, 0, anchor='nw', image=img)
            canvas.image = img
            if(tmp[2]=="n"):
                pass
                canvas.configure(bg=coloreScuro)
            else:
                canvas.configure(bg="#2FA8F1")

        else:
            mBox.showinfo("Errore", "Città non trovata!!")
            reset_variabili()


finestra = Tk()
finestra.title("Meteo figo")
finestra.geometry('550x350')
finestra.resizable(False, False)
bg= "#B1F3F3"
finestra.configure(bg=bg , width=15, height=10)


canvas = Canvas(finestra, width=100, height=100)
canvas.configure(bg=bg,highlightbackground=bg)
canvas.place(x=220,y=150)


icona = PhotoImage(file="image_icon/icona.png")
Label(finestra,image=icona,bg=bg,highlightbackground=bg).place(x=485, y=5)


Label(finestra, text="Inserisci la città:").place(x=100, y=280)


Label(finestra, text="id citta:",justify="left",width=10,anchor=E,bg=bg).grid(row=0, column=0)
Label(finestra, text="nome:",justify="left",width=10,anchor=E,bg=bg).grid(row=1, column=0)
Label(finestra, text="lon:",justify="left",width=10,anchor=E,bg=bg).grid(row=2, column=0)
Label(finestra, text="lat:",justify="left",width=10,anchor=E,bg=bg).grid(row=3, column=0)
Label(finestra, text="nazione:",justify="left",width=10,anchor=E,bg=bg).grid(row=4, column=0)
Label(finestra, text="temperatura corrente:",justify="left",width=17,anchor=E,bg=bg).grid(row=0, column=2)
Label(finestra, text="massima:",justify="left",width=17,anchor=E,bg=bg).grid(row=1, column=2)
Label(finestra, text="minima:",justify="left",width=17,anchor=E,bg=bg).grid(row=2, column=2)
Label(finestra, text="umidità:",justify="left",width=17,anchor=E,bg=bg).grid(row=3, column=2)
Label(finestra, text="ultimo aggiornamento:",justify="left",width=17,anchor=E,bg=bg).grid(row=4, column=2)


txt_nome_citta = tk.StringVar()
nome_citta = Entry(finestra,fg='green',exportselection = 0,selectbackground='blue',state = NORMAL,textvariable=txt_nome_citta)
nome_citta.place(x=200, y=280)


idCitta = tk.StringVar()
nome = tk.StringVar()
lon = tk.StringVar()
lat = tk.StringVar()
nazione = tk.StringVar()
temperatura_corr = tk.StringVar()
temperatura_max = tk.StringVar()
temperatura_min = tk.StringVar()
umidita = tk.StringVar()
ultimo_aggiornamento = tk.StringVar()


entryIdCitta = tk.Entry(finestra, width=20, textvariable=idCitta,state = DISABLED)
entryNome = tk.Entry(finestra, width=20, textvariable=nome,state = DISABLED)
entryLon = tk.Entry(finestra, width=20, textvariable=lon,state = DISABLED)
entryLat = tk.Entry(finestra, width=20, textvariable=lat,state = DISABLED)
entryNazione = tk.Entry(finestra, width=20, textvariable=nazione,state = DISABLED)
entryTemperetura_corr = tk.Entry(finestra, width=20, textvariable=temperatura_corr,state = DISABLED)
entryTemperatura_max = tk.Entry(finestra, width=20, textvariable=temperatura_max,state = DISABLED)
entryTemperatura_min = tk.Entry(finestra, width=20, textvariable=temperatura_min,state = DISABLED)
entryUmidita = tk.Entry(finestra, width=20, textvariable=umidita,state = DISABLED)
entryUltimo_aggiornamento = tk.Entry(finestra, width=20, textvariable=ultimo_aggiornamento,state = DISABLED)


entryIdCitta.grid(column=1, row=0, padx=10)
entryNome.grid(column=1, row=1, padx=10)
entryLon.grid(column=1, row=2, padx=10)
entryLat.grid(column=1, row=3, padx=10)
entryNazione.grid(column=1, row=4, padx=10)
entryTemperetura_corr.grid(column=3, row=0, padx=10)
entryTemperatura_max.grid(column=3, row=1, padx=10)
entryTemperatura_min.grid(column=3, row=2, padx=10)
entryUmidita.grid(column=3, row=3, padx=10)
entryUltimo_aggiornamento.grid(column=3, row=4, padx=10)


Button(finestra, text="reset", command=reset_variabili).place(x=390 ,y=280)
Button(finestra, text="Cerca", command=cerca).place(x=330, y=280)
Button(finestra, text="Chiudi", command=chiudi, bg="#ff9900",fg='white',activebackground="#f34f4f",activeforeground="white",bd=1).place(x=500, y=320)


mainloop()
