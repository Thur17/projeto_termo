from tkinter import *

root=Tk()

root.configure(background="#F4A460")

class Application():
    def __init__(self):
        self.root = root   
        self.tela()
        root.mainloop()
    def tela(self):
        self.root.title("Preenchimento de termo de Ativos")
        self.root.configure(background="#F4A460")
        self.root.geometry("1000x620")
        self.root.wm_resizable(True,True)



Application()
