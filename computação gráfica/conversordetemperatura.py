import tkinter as tk

#função de callback
def convertToFarenheit():
    try:
        C=int(entry.get())
        convertedTemp= str(C) + "ºC = " + str(C * 9/5 + 32) +"ºF."
        result.config(text=convertedTemp)
    except ValueError:
        result.config(text="Valor inválido.")

#definição inicial
root= tk.Tk()
root.title("Conversor de Temperaturas")
frame=tk.Frame()
frame.pack(padx=10,pady=10)

#definição dos widgets 
label=tk.Label(frame,text="Temperatura (Cº)")
result=tk.Label(frame,text="Insira um valor...")
entry=tk.Entry(frame)
button=tk.Button(frame,text="Converter",command=convertToFarenheit)

#packing e mainloop
label.pack()
entry.pack()
button.pack()
result.pack()
root.mainloop()