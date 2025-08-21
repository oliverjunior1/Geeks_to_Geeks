from tkinter import Label, Button

from customtkinter import CTk

def mudar_texto():
    rotulo.config(text="Texto alternado!")

window = CTk()
window.title("Botão Interativo")

rotulo = Label(window, text="Texto original")
rotulo.pack()

botao = Button(window, text="Click aqui", command=mudar_texto)
botao.pack()

window.mainloop()