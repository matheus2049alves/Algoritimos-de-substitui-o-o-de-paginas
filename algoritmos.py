from tkinter import *
import matplotlib as plt

def inicializar():
    global root
    global linha
    global coluna
    global taxa_falha
    linha = 0
    coluna = 1
    taxa_falha = 0

def fifo (num_frames, paginas, num_referencias):
    inicializar()
    registrar_falhas = []
    sem_falhas = []
    frames = [c for c in range(num_referencias + 3)]

    if animation is True:
        new_window(txt, capacity)
    
def nova_janela(capacity):
    global root
    root = Tk()
    Basic_design(capacity)
    root.geometry("1600x660")

def configura_tabela(N):
    k=N

    referencia_Label= Label(root,text="Páginas referenciadas")
    referencia_Label.configure(font=("Helvetica", 15))
    referencia_Label.grid(row=0,column=0,padx=20,pady=10)
    
    for i in range(N):
        label_frame= Label(root,text="Frame "+str(k),pady=10,padx=20,fg="black")
        label_frame.configure(font=("Helvetica", 15))
        label_frame.grid(row=i+1,column=0)
        k-=1
    falha_Label= Label(root,text="Page Faults")
    falha_Label.configure(font=("Helvetica", 15))
    falha_Label.grid(row=N+1,column=0,padx=20,pady=10)


def Visualisar(tipo, num_frames, referencias):
    nFrames = (int)(num_frames)
    paginas = list(map(int, referencias.split(" ")))
    num_referencias = len(referencias)

    if tipo == "FIFO":
        fifo(nFrames, paginas, num_referencias)







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

visualizar_botao = Button(frame1, text="visualizar", width="20",command=lambda : Visualisar(tipo_algoritmo.get(),num_frames.get(),referências.get() ) )
visualizar_botao.pack(pady="25")
Menu.mainloop()
