import customtkinter as ctk

window = ctk.CTk()
window.title("Minha primeira Janela")
window.geometry("380x200")

text = ctk.CTkLabel(window,text="Jesus is the light of the world!")
text.pack()

window.mainloop()