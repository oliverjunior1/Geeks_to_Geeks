import tkinter as tk
import random

def mega():
    x = random.sample(range(1,61),6)
    sorted(x)
    return label.config(text=f'The lucky number is {sorted(x)}')
def lotofacil():
    x = random.sample(range(1,26),15)
    return label.config(text=f'The lucky number is {sorted(x)}')

root = tk.Tk()
root.geometry("500x500")
label = tk.Label(root, text="Mateus 21:22 E tudo o que pedirem em oração, se crerem, vocês receberão")
label.pack()
button_mega = tk.Button(root, text="Mega", command=mega)
button_mega.pack()
button_lotofacil = tk.Button(root, text='Loto Facil', command=lotofacil)
button_lotofacil.pack()
root.mainloop()

