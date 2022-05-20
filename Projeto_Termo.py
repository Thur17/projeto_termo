from cProfile import label
from email.mime import image
from tkinter import *

root=Tk()

root.configure(background="#F4A460")


class Application():
    def __init__(self):
        self.root = root   
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        root.mainloop()
    def tela(self):
        self.root.title("Preenchimento de termo de Ativos")
        self.root.configure(background="#F4A460")
        self.root.geometry("1000x800")
        self.root.wm_resizable(True,True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=400, height=300)
    def frames_da_tela(self):
        self.frame_1=Frame(self.root, bd=4, bg="#F4A460", highlightthickness=3 ) 
        self.frame_1.place(relx=0.02,rely=0.02,relwidth=0.96,relheight=0.46)
        self.frame_2=Frame(self.root, bd=4, bg="#F4A460", highlightthickness=3 ) 
        self.frame_2.place(relx=0.02,rely=0.5,relwidth=0.96,relheight=0.46)
    def widgets_frame1(self):
        ###botão limpar 
        self.bt_limpar=Button(self.frame_1,text="Limpar")
        self.bt_limpar.place(relx=0.2,rely=0.1,relwidth=0.1,relheight=0.15)
        ###botão Busacar
        self.bt_buscar=Button(self.frame_1,text="Buscar")
        self.bt_buscar.place(relx=0.3,rely=0.1,relwidth=0.1,relheight=0.15)
        ###botão novo
        self.bt_novo=Button(self.frame_1,text="Novo")
        self.bt_novo.place(relx=0.6,rely=0.1,relwidth=0.1,relheight=0.15)
        ###botão alterar
        self.bt_alterar=Button(self.frame_1,text="Alterar")
        self.bt_alterar.place(relx=0.7,rely=0.1,relwidth=0.1,relheight=0.15)
        ###botão apagar
        self.bt_apagar=Button(self.frame_1,text="Apagar")
        self.bt_apagar.place(relx=0.8,rely=0.1,relwidth=0.1,relheight=0.15)
        ###Criação da label de entrada do codigo
        self.lb_codigo=Label(self.frame_1,text="Serial")
        self.lb_codigo.place(relx=0.05,rely=0.05)

        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.05, rely=0.15)


Application()