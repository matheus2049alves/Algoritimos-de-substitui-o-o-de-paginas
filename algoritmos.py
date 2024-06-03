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
    global root
    global linha 
    global taxa_falha
    global coluna
    

    inicializar()
    registrar_falhas = []
    sem_falhas = []
    frames = [c for c in range(num_referencias + 3)]

    nova_janela(num_referencias)
    for ii in frames:
        if ii == 0:
          registrar_falhas.append(0)
          sem_falhas.append(0)
          continue
        s = set()
        front = 0
        indexes = []
        falha_pagina = 0
        falha = []
        for i in range(num_frames):
            if (len(s) < ii):
                if (paginas[i] not in s):
                    s.add(paginas[i])
                    page_faults += 1
                    falha.append(True)
                    indexes.append(paginas[i])
                else:
                    falha.append(False)
            else:
                if (paginas[i] not in s):
                    s.remove(indexes[front])
                    s.add(paginas[i])
                    indexes[front] = paginas[i]
                    falha_pagina += 1
                    falha.append(True)
                    front+=1
                    if(front>ii-1):
                        front=0
                else:
                    falha.append(False)
            if ii == num_referencias:
                taxa_falha = float((falha_pagina) / num_frames)
                imaginario = indexes
                animar(num_referencias, paginas[i], imaginario, falha[i], taxa_falha, num_frames, frames, registrar_falhas, sem_falhas)
                coluna += 1
        registrar_falhas.append(falha_pagina)
        sem_falhas.append(num_frames-falha_pagina)
    
def nova_janela(capacity):
    global root
    root = Tk()
    Basic_design(capacity)
    root.geometry("1600x660")

#Função espaço vazio - Leo

def espaco_vazio():
    global root
    global linha
    global coluna
    L = Label(root, text=" ", height="1", width="1")
    L.grid(row=linha, column=coluna)
    linha += 1

#Função para quadradinhos - Leo

def quadro(elemento):
    global root
    global linha
    global coluna
    L = Label(root, text=elemento, padx=20,pady=10,bd=1,fg="green", relief=SOLID,anchor="center")
    L.configure(font=("Century Gothic", 12))
    L.grid(row=linha, column=coluna)
    linha += 1


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

def animar(num_referencias, paginas, imaginario, falha, taxa_falha, num_frames, frames, registrar_falhas, sem_falhas):
    global root
    global linha
    global coluna
    row = 0
    L = Label(root, text=paginas, pady=10, fg="green")
    L.configure(font=("Century Gothic", 15))
    L.grid(row=linha, column=coluna)
    linha += 1
    ls = []
    ls = imaginario
    for i in range(num_referencias - len(ls)):
        espaco_vazio()

    for i in reversed(ls):
        quadro(i)

    build_EmptyLabel()

    if (falha == True):
        falha = "Falha"
        L1 = Label(root, text=teste_falha, fg="red")
        L1.configure(font=("Century Gothic", 12, 'bold'))
        L1.grid(row=linha, column=coluna - 1)
        linha += 1
    else:
        teste_falha = "Sucesso"
        L1 = Label(root, text=teste_falha, font="Questrial", fg="green")
        L1.configure(font=("Century Gothic", 12, 'bold'))
        L1.grid(row=row, column=col - 1)
        row += 1
    FrameRatio(taxa_falha, num_frames, frames, registrar_falhas, sem_falhas)






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
