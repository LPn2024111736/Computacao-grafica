import tkinter as tk

#funções de callback não necessárias para o exercício

#definição inicial 
root=tk.Tk()
root.title("Interface Organizada")
frame=tk.Frame()
frame.pack(padx=50,pady=10)
frame1=tk.Frame()
frame1.pack(padx=50,pady=10)

#definição de widgets
label=tk.Label(frame,text="Label 1")
label1=tk.Label(frame1,text="Label 2")
button=tk.Button(frame,text="Botão 1")
button1=tk.Button(frame1,text="Botão 2")
entry=tk.Entry(frame)
entry1=tk.Entry(frame1)

#packing e mainloop
button.pack(side="left")
label.pack(side="right")
entry.pack()
label1.pack(side="right")
button1.pack(side="left")
entry1.pack()
root.mainloop()