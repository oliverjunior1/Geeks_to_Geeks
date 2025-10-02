import customtkinter as ctk


window = ctk.CTk()
window.title("Minha primeira Janela")
window.geometry("380x200")

rotulo = ctk.CTkLabel(window, text="Olá, Joaquim")
rotulo.pack()

window.mainloop()