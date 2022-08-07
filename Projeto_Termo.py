import sqlite3
from cProfile import label
from tkinter import *
from tkinter import ttk
from tkinter.tix import COLUMN



root=Tk()

class Funcs():
    def limpa_tela(self):
         self.Nome_entry.delete(0,END)
         self.CPF_entry.delete(0,END)
         self.Equipamento_entry.delete(0,END)
         self.Serial_entry.delete(0,END)
         self.Patrimônio_entry.delete(0,END)
   
    def conecta_bd(self):
        self.conn = sqlite3.connect("funcionarios.db")
        self.cursor = self.conn.cursor(); print("Conectando ao banco de dados")
    def desconecta_bd(self):
        self.conn.close(); print("Desconectando ao banco de dados")
    def montaTabelas(self):
        self.conecta_bd()
        ###Criação da tabela 
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS funcionario (
               Nome CHAR(40) NOT NULL,
               CPF CHAR(14) NOT NULL,
               Equipamento CHAR(40) NOT NULL,
               Serial CHAR(15) NOT NULL,
               Patrimônio CHAR(10) NOT NULL
            );
        """)         
        self.conn.commit();print("Banco de dados criado")
        self.desconecta_bd()
    
    def add_funcionario(self): 
        self.Nome = self.Nome_entry.get()
        self.CPF = self.CPF_entry.get()
        self.Equipamento = self.Equipamento_entry.get()
        self.Serial = self.Serial_entry.get()
        self.Patrimônio = self.Patrimônio_entry.get()
        self.conecta_bd()
        
        self.cursor.execute(""" insert into funcionario (Nome, CPF, Equipamento, Serial, Patrimônio)
        Values (?, ?, ?, ?, ?)""", (self.Nome, self.CPF, self.Equipamento, self.Serial, self.Patrimônio))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_tela()

    def select_lista(self):
        self.listaCli.delete(* self.listaCli.get_children())
        self.conecta_bd()
        lista = self.cursor.execute(""" SELECT Nome, CPF, Equipamento, Serial, Patrimônio FROM funcionario ORDER BY Nome ASC;   """)

        for i in lista:
            self.listaCli.insert("", END, values=i)
            self.desconecta_bd()

root.configure(background="#F4A460")
class Application(Funcs):
    def __init__(self):
        self.root = root   
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
        self.montaTabelas()
        self.select_lista()
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
        self.bt_novo=Button(self.frame_1,text="Novo",bd=3,bg="#FFFFFF", font= ("verdana",10, "bold" ), command=self.add_funcionario)
        self.bt_novo.place(relx=0.4,rely=0.1,relwidth=0.1,relheight=0.15)
        ###botão alterar
        self.bt_alterar=Button(self.frame_1,text="Alterar",bd=3,bg="#FFFFFF", font= ("verdana",10, "bold" ))
        self.bt_alterar.place(relx=0.5,rely=0.1,relwidth=0.1,relheight=0.15)
        ###botão apagar
        self.bt_apagar=Button(self.frame_1,text="Apagar",bd=3,bg="#FFFFFF", font= ("verdana",10, "bold" ))
        self.bt_apagar.place(relx=0.6,rely=0.1,relwidth=0.1,relheight=0.15)        
        
  

        ###Criação da label e entrada do nome 
        self.lb_Nome=Label(self.frame_1, text="Nome",bg="#F4A460",font= ("verdana",10, "bold" ))
        self.lb_Nome.place(relx=0.05, rely=0.30)
        self.Nome_entry=Entry(self.frame_1)
        self.Nome_entry.place(relx=0.05,rely=0.37,relwidth=0.8)
        ###Criação da label e entrada do CPF 
        self.lb_CPF=Label(self.frame_1, text="CPF",bg="#F4A460",font= ("verdana",10, "bold" ))
        self.lb_CPF.place(relx=0.05, rely=0.48)
        self.CPF_entry=Entry(self.frame_1)
        self.CPF_entry.place(relx=0.05,rely=0.55,relwidth=0.2)
        ###Criação da label e entrada do Modelo Equipamento
        self.lb_Equipamento=Label(self.frame_1, text="Equipamento",bg="#F4A460",font= ("verdana",10, "bold" ))
        self.lb_Equipamento.place(relx=0.05, rely=0.65)
        self.Equipamento_entry=Entry(self.frame_1)
        self.Equipamento_entry.place(relx=0.05,rely=0.71,relwidth=0.8)
        ###Criação da label de entrada do Serial
        self.lb_Serial=Label(self.frame_1,text="Serial",bg="#F4A460",font= ("verdana",10, "bold" ))
        self.lb_Serial.place(relx=0.05,rely=0.82)
        self.Serial_entry = Entry(self.frame_1)
        self.Serial_entry.place(relx=0.05, rely=0.89,relwidth=0.1)           
        ###Criação da label e entrada do Nº Etiqueta 
        self.lb_Patrimônio=Label(self.frame_1, text="Patrimônio",bg="#F4A460",font= ("verdana",10, "bold" ))
        self.lb_Patrimônio.place(relx=0.2, rely=0.82)
        self.Patrimônio_entry=Entry(self.frame_1)
        self.Patrimônio_entry.place(relx=0.2,rely=0.89,relwidth=0.1)
        ###Lista Frame 2 
    def lista_frame2(self):
        self.listaCli=ttk.Treeview(self.frame_2,height= 3, column=("col1","col2","col3","col4","col5","col6"))  
        
        self.listaCli.heading("#0",text="")
        self.listaCli.heading("#1",text="Nome")
        self.listaCli.heading("#2",text="CPF")
        self.listaCli.heading("#3",text="Equipamento")
        self.listaCli.heading("#4",text="Serial")
        self.listaCli.heading("#5",text="Patrimônio")

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