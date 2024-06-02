from tkinter import *
import matplotlib as plt

# Janela principal onde ficam as entradas de número de páginas e referências de páginas
Menu = Tk()
Menu.title("Substituição de página")
Menu.geometry("700x600+0+0")
Menu.resizable(False, False)
Menu.overrideredirect(False)

label1 = Label(Menu, text="Tipo de algoritmo", font=("helvetica", 20), height=2)
label1.pack()

frame1 = Frame(bg="gray").pack()

tipo_algoritmo = StringVar(Menu)
tipo_algoritmo.set("FIFO")  # Valor padrão

seletor = OptionMenu(frame1, tipo_algoritmo, "FIFO", "NRU")
seletor.config(width=10)
seletor.pack()

label2 = Label(frame1, text="Número de frames", font=("helvetica", 20), height=2)
label2.pack()

num_frames = Entry(frame1, width="15", border=0, justify= "center")
num_frames.pack()

label3 = Label(frame1, text="Páginas referenciadas", font=("helvetica", 20), height=2)
label3.pack()

referências = Entry(frame1, width="20", border=0, justify= "center")
referências.pack()

visualizar_botao = Button(frame1, text="visualizar", width="15")
visualizar_botao.pack(pady="25")
Menu.mainloop()
