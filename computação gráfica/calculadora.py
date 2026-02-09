import tkinter as tk

#funções de callback
def somar():
    try:
        val1=float(num1.get())
        val2=float(num2.get())
        resultado= "Resultado: " + str(val1+val2)
        result.config(text=resultado)
    except ValueError:
        result.config(text="Erro! Valores inválidos!")

def subtrair():
    try:
        val1=float(num1.get())
        val2=float(num2.get())
        resultado= "Resultado: " + str(val1-val2)
        result.config(text=resultado)
    except ValueError:
        result.config(text="Erro! Valores inválidos!")

#definição inicial
root=tk.Tk()
root.title("Calculadora- Somar e Subtrair")
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

#definição dos widgets 
num1=tk.Entry(frame)
num2=tk.Entry(frame)
num1text=tk.Label(frame,text="Primeiro número: ")
num2text=tk.Label(frame,text="Segundo número: ")
sumbutton=tk.Button(frame,command=somar,text="Somar Números")
subbutton=tk.Button(frame,command=subtrair,text="Subtrair Números")
result=tk.Label(frame,text="Faça uma operação para obter um valor!")

#packing e mainloop
num1text.pack()
num1.pack()
num2text.pack()
num2.pack()
sumbutton.pack()
subbutton.pack()
result.pack()
root.mainloop()