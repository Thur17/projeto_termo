from cProfile import label
from tkinter import *
from tkinter import ttk
from tkinter.tix import COLUMN
import sqlite3

root=Tk()

class Funcs():
    def limpa_tela(self):
         self.nome_entry.delete(0,END)
         self.cpf_entry.delete(0,END)
         self.equipamento_entry.delete(0,END)
         self.serial_entry.delete(0,END)
         self.etiqueta_entry.delete(0,END)
    def conecta_bd(self):
        self.conn = sqlite3.connect("funcionarios.bd")
        self.cursor = self.conn.cursor()
    def desconecta_bd(self):
        self.conn.close()
    def montarTabelas(self):
        self.conecta_bd(); print("Conectando ao banco de dados")
        ###Criação da tabela 
        self.cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS funcionario (
               nome_Completo CHAR(40) NOT NULL,
               CPF CHAR(14) NOT NULL,
               Modelo_equipamento CHAR(40) NOT NULL,
               Serial CHAR(15) NOT NULL,
               Patrimonio CHAR(10) NOT NULL,
            );
        """)         
        self.conn.commit();print("Banco de dados criado")
        self.desconecta_bd()

root.configure(background="#F4A460")

class Application(Funcs):
    def __init__(self):
        self.root = root   
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
        self.montarTabelas()
        root.mainloop()
    def tela(self):
        self.root.title("Preenchimento de termo de Ativos")
        self.root.configure(background="#F4A460")
        self.root.geometry("1000x800")
        self.root.wm_resizable(True,True)
        self.root.maxsize(width=1000, height=900)
        self.root.minsize(width=400, height=300)
    def frames_da_tela(self):
        self.frame_1=Frame(self.root, bd=4, bg="#F4A460", highlightthickness=3 ) 
        self.frame_1.place(relx=0.02,rely=0.02,relwidth=0.96,relheight=0.46)
        self.frame_2=Frame(self.root, bd=4, bg="#F4A460", highlightthickness=3 ) 
        self.frame_2.place(relx=0.02,rely=0.5,relwidth=0.96,relheight=0.46)
    def widgets_frame1(self):
        ###botão limpar 
        self.bt_limpar=Button(self.frame_1,text="Limpar",bd=3,bg="#FFFFFF", font= ("verdana",10, "bold" ), command= self.limpa_tela)
        self.bt_limpar.place(relx=0.2,rely=0.1,relwidth=0.1,relheight=0.15)
        ###botão Busacar
        self.bt_buscar=Button(self.frame_1,text="Buscar",bd=3,bg="#FFFFFF", font= ("verdana",10, "bold" ))
        self.bt_buscar.place(relx=0.3,rely=0.1,relwidth=0.1,relheight=0.15)
        ###botão novo
        self.bt_novo=Button(self.frame_1,text="Novo",bd=3,bg="#FFFFFF", font= ("verdana",10, "bold" ))
        self.bt_novo.place(relx=0.4,rely=0.1,relwidth=0.1,relheight=0.15)
        ###botão alterar
        self.bt_alterar=Button(self.frame_1,text="Alterar",bd=3,bg="#FFFFFF", font= ("verdana",10, "bold" ))
        self.bt_alterar.place(relx=0.5,rely=0.1,relwidth=0.1,relheight=0.15)
        ###botão apagar
        self.bt_apagar=Button(self.frame_1,text="Apagar",bd=3,bg="#FFFFFF", font= ("verdana",10, "bold" ))
        self.bt_apagar.place(relx=0.6,rely=0.1,relwidth=0.1,relheight=0.15)        
        
        ###Criação da label e entrada do nome 
        self.lb_nome=Label(self.frame_1, text="Nome Completo",bg="#F4A460",font= ("verdana",10, "bold" ))
        self.lb_nome.place(relx=0.05, rely=0.30)
        self.nome_entry=Entry(self.frame_1)
        self.nome_entry.place(relx=0.05,rely=0.37,relwidth=0.8)
        ###Criação da label e entrada do CPF 
        self.lb_cpf=Label(self.frame_1, text="CPF",bg="#F4A460",font= ("verdana",10, "bold" ))
        self.lb_cpf.place(relx=0.05, rely=0.48)
        self.cpf_entry=Entry(self.frame_1)
        self.cpf_entry.place(relx=0.05,rely=0.55,relwidth=0.2)
        ###Criação da label e entrada do Modelo Equipamento
        self.lb_equipamento=Label(self.frame_1, text="Modelo Equipamento",bg="#F4A460",font= ("verdana",10, "bold" ))
        self.lb_equipamento.place(relx=0.05, rely=0.65)
        self.equipamento_entry=Entry(self.frame_1)
        self.equipamento_entry.place(relx=0.05,rely=0.71,relwidth=0.8)
        ###Criação da label de entrada do Serial
        self.lb_serial=Label(self.frame_1,text="Nº Serial",bg="#F4A460",font= ("verdana",10, "bold" ))
        self.lb_serial.place(relx=0.05,rely=0.82)
        self.serial_entry = Entry(self.frame_1)
        self.serial_entry.place(relx=0.05, rely=0.89,relwidth=0.1)           
        ###Criação da label e entrada do Nº Etiqueta 
        self.lb_etiqueta=Label(self.frame_1, text="Nº Patrimônio",bg="#F4A460",font= ("verdana",10, "bold" ))
        self.lb_etiqueta.place(relx=0.2, rely=0.82)
        self.etiqueta_entry=Entry(self.frame_1)
        self.etiqueta_entry.place(relx=0.2,rely=0.89,relwidth=0.1)
        ###Lista Frame 2 
    def lista_frame2(self):
        self.listaCli=ttk.Treeview(self.frame_2,height= 3, column=("col1","col2","col3","col4","col5"))  
        
        self.listaCli.heading("#0",text="")
        self.listaCli.heading("#1",text="Nome")
        self.listaCli.heading("#2",text="CPF")
        self.listaCli.heading("#3",text="Equipamento")
        self.listaCli.heading("#4",text="Nº Serial")
        self.listaCli.heading("#5",text="Nº Patrimônio")

        self.listaCli.column("#0", width=1)
        self.listaCli.column("#1", width=150)
        self.listaCli.column("#2", width=70)
        self.listaCli.column("#3", width=150)
        self.listaCli.column("#4", width=35)
        self.listaCli.column("#5", width=60)
        self.listaCli.place(relx=0.01,rely=0.1, relwidth=0.95, relheight=0.85)
        
        self.scroolLista = Scrollbar(self.frame_2, orient="vertical")
        self.listaCli.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.02, relheight=0.85 )
        

Application()