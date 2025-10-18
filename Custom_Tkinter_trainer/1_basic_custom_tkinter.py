import customtkinter as ctk

window = ctk.CTk()
window.title("Minha primeira janela")
window.geometry("380x200")

rotulo = ctk.CTkLabel(window, text="Jesus is the light!")
rotulo.pack()

window.mainloop()