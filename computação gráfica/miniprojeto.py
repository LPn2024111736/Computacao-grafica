import tkinter as tk 

#Funções de callback

#Função register() mostra uma mensagem de registo de mockup, mostrando o nome e os pronomes do utilizador se as palavras passes forem iguais e não nulas. 
def register():
    pass1=entryPass.get()
    pass2=entryCPass.get()
    name=entryName.get()
    gender=genderOption.get()
    text=name + " just registered their account! Say hi to " + gender + "!"
    if pass1==pass2:
        if pass1=="" and pass2=="":
            labelLogin.config(text="No password inserted! Please insert a password!")
        else:
            labelLogin.config(text=text)
    else:
        labelLogin.config(text="Passwords don't match, try again!")

#Função pronouns() mostra uma mensagem com os pronomes dependendo do género selecionado pelo utilizador.
def pronouns():
    gender=genderOption.get()
    match gender:
        case "Male":
            labelPronouns.config(text="Pronouns: He/Him")
        case "Female":
            labelPronouns.config(text="Pronouns: She/Her")
        case "Other":
            labelPronouns.config(text="Pronouns: They/Them")
        
#definição inicial, cada parte tem um frame para si, incluindo o botão de registar + as mensagens de texto
#O texto dentro da interface está em inglês por questões de semântica, queria colocar mais do que 2 géneros
#mas ficava estranho em termos de escrita em português.
root=tk.Tk()
root.title("Mini Projeto")
nameFrame=tk.Frame()
nameFrame.pack(padx=40,pady=10)
passwordFrame=tk.Frame()
passwordFrame.pack(padx=40,pady=10)
confirmPasswordFrame=tk.Frame()
confirmPasswordFrame.pack(padx=40,pady=10)
genderFrame=tk.Frame()
genderFrame.pack(padx=40,pady=10)
loginFrame=tk.Frame()
loginFrame.pack(padx=40,pady=10)


#Definição dos widgets e packing estão divididas por frame.
#Inserir nome
labelName = tk.Label(nameFrame, text="Insert your name:             ")
labelName.pack(side="left")
entryName=tk.Entry(nameFrame)
entryName.pack()

#Inserir password
labelPass = tk.Label(passwordFrame, text="Insert your password:      ")
labelPass.pack(side="left")
entryPass=tk.Entry(passwordFrame)
entryPass.pack()

#Confirmar password
labelCPass = tk.Label(confirmPasswordFrame, text="Confirm your password: ")
labelCPass.pack(side="left")
entryCPass=tk.Entry(confirmPasswordFrame)
entryCPass.pack()

#Selecionar género (sei que não demos radio buttons na aula mas queria utilizar por uma questão de curiosidade)
labelGender = tk.Label(genderFrame, text="              Select your gender:      ")
labelGender.pack(side="left")
genderOption=tk.StringVar(genderFrame,"him")
genderMButton=tk.Radiobutton(genderFrame,variable=genderOption,text="Male",value="him",command=pronouns)
genderMButton.pack(side="left")
genderFButton=tk.Radiobutton(genderFrame,variable=genderOption,text="Female",value="her",command=pronouns)
genderFButton.pack(side="left")
genderOButton=tk.Radiobutton(genderFrame,variable=genderOption,text="Other",value="them",command=pronouns)
genderOButton.pack(side="left")

#Botão de registar e mensagens de texto
labelPronouns= tk.Label(loginFrame, text="Pronouns: He/Him" )
labelPronouns.pack()
buttonRegister=tk.Button(command=register,text="Register")
buttonRegister.pack(pady=10)
labelLogin =tk.Label(loginFrame, text="Register to display welcome message")
labelLogin.pack()

#mainloop
root.mainloop()