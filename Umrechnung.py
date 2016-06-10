# Name: Temperatureinheiten universal
# Beschreibung: Script, um die Temperatur von einer Temperatureinheit(Kelvin,
#               Celsius oder Fahrenheit) auf alle anderen zu brerechnen.
# Autoren: Markus Sünkens & Bo-Cheng Yang
# Datum: 27.05.16

from tkinter import *

fenster = Tk()
menu = Menu(fenster)
fenster.config(menu=menu)
filemenu = Menu(menu)
fenster.title("Temperatureinheiten")
fenster.geometry("400x300")
entry = Entry(fenster)
text = Label (fenster, text="")

#----Funktionen----#

def Kelvin():
    try:
        eingabe = float(entry.get())
        num_in_C = round(eingabe - 273.15,3)
        num_in_F = round(eingabe * 1.8 - 459.67,3)
        #text = Label (fenster, text=str(eingabe)+ "°K = "+ str(num_in_C)+ "°C" +
        #"\n" + str(eingabe)+ "°K = " + str(num_in_F)+"°F")
        #text.pack()
        #fenster.mainloop()
        print(str(eingabe)+ "°K = "+ str(num_in_C)+ "°C" +
        "\n" + str(eingabe)+ "°K = " + str(num_in_F)+"°F")
        
    except:
        #text = Label (fenster, text="""Du musst eine Zahl in das Eingabefeld schreiben!
        #""")
        #text.pack()
        #fenster.mainloop()
        print("""Du musst eine Zahl in das Eingabefeld schreiben!
        """)


def Celsius():
    try:
        eingabe = float(entry.get())
        num_in_K =  round(eingabe + 273.15,3)
        num_in_F = round(eingabe * 1.8 + 32,3)
        #text = Label (fenster, text=str(eingabe)+ "°C = "+str(num_in_K)+ "°K" +
        #"\n" + str(eingabe)+ "°C = " + str(num_in_F)+"°F")
        #text.pack()
        #fenster.mainloop()
        print(str(eingabe)+ "°C = "+str(num_in_K)+ "°K" +
        "\n" + str(eingabe)+ "°C = " + str(num_in_F)+"°F")
    except:
        #text = Label (fenster, text="""Du musst eine Zahl in das Eingabefeld schreiben!
        #""")
        #text.pack()
        #fenster.mainloop()
        print("""Du musst eine Zahl in das Eingabefeld schreiben!
        """)

def Fahrenheit():
    try:
        eingabe = float(entry.get())
        num_in_C = round((eingabe - 32)*(5/9),3)
        num_in_K = round((eingabe + 459.67)*(5/9),3)
        #text = Label (fenster, text=str(eingabe)+ "°F = "+ str(num_in_C)+ "°C" +
        #"\n" + str(eingabe)+ "°F = " + str(num_in_K)+"°K")
        #text.pack()
        #fenster.mainloop()
        print(str(eingabe)+ "°F = "+ str(num_in_C)+ "°C" +
        "\n" + str(eingabe)+ "°F = " + str(num_in_K)+"°K")
    except:
        #text = Label (fenster, text="""Du musst eine Zahl in das Eingabefeld schreiben!
        #""")
        #text.pack()
        #fenster.mainloop()
        print("""Du musst eine Zahl in das Eingabefeld schreiben!
        """)
        
def close():
    exit()
    
#def clear():
    

   
#Umrechnung

def Umrechnung():
    text= Label (fenster, text="""Wert in das Eingabefeld eingeben und dann die gegebene Einheit""")
    text.pack()
    entry.pack()
    kno_frame = Frame(fenster)
    knopf = Button(kno_frame, text="Celsius",command=Celsius)
    knopf.pack(side=LEFT)
    knopf = Button(kno_frame, text="Kelvin",command=Kelvin)
    knopf.pack(side=LEFT)
    knopf = Button(kno_frame, text="Fahrenheit",command=Fahrenheit)
    knopf.pack(side=LEFT)
    kno_frame.pack(side=TOP)
    menu.add_cascade(label="File", menu=filemenu)
    #filemenu.add_command(label="Clear", command=clear)
    filemenu.add_command(label="Close", command=close)
    fenster.mainloop()
    

#----.----#
print("""Umrechnung()
""")
Umrechnung()
