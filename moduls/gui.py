from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk

class Interface:
    def __init__(self):
        self.main = Tk()
        self.main.title("Agenda con archivos")
        self.main.resizable(False, False)

        self.frame_main = Frame(self.main, width=750, height=450)
        self.frame_main.grid(row=0, column=0)

        self.frame_btns = Frame(self.main, width=750, height=200)
        self.frame_btns.grid(row=1, column=0)
        
        self.frame_grid = Frame(self.main, width=200, height=200)
        self.frame_grid.grid(row=2, column=0)
        self.text = ("ID" ,"Nombre y apellido :", "Correo :")

    def label_title(self, text, color, fila, col):
        title = Label(self.frame_main, text=text, fg=color, font=("Monospace Regular",15))
        title.grid(row=fila, column=col, columnspan=6, padx=10, pady=10)
    
    def label_text(self, text, color, fila, col, frame = 1):
        if ( frame ):
            title = Label(self.frame_main, text=text, fg=color, font=("Monospace Regular",8))
            title.grid(row=fila, column=col, padx=8, pady=8, sticky="w")
        else:
            title = Label(self.frame_grid, text=text, fg=color, font=("Monospace Regular",8))
            title.grid(row=fila, column=col, padx=8, pady=8)

    def text_box(self, fila, col, var):
        text_box = Entry(self.frame_main, textvariable=var)
        text_box.grid(row=fila, column=col)

    def btn(self, text, w, fila, col, colp, func, frame=1):
        if frame :
            btn = Button(self.frame_btns, width=w, text=text, command=func)
            btn.grid(row=fila, column=col, columnspan=colp)
        elif frame == 0:
            btn = Button(self.frame_grid, width=w, text=text, command=func)
            btn.grid(row=fila, column=col, columnspan=colp)
        else: 
            btn = Button(self.frame_main, width=w, text=text, command=func)
            btn.grid(row=fila, column=col, columnspan=colp)
            
    def msj(self, titulo, msj):
        messagebox.showinfo(title=titulo, message=msj)
    
    def msj_err(self, titulo, msj):
        messagebox.showerror(title=titulo, message=msj)
    
    def msj_success(self, titulo, msj):
        messagebox._show(title=titulo, message=msj)
    
    def clear(self, arr):
        for item in arr:
            item.set("")

    def dataGrid(self, data):
        self.grid = ttk.Treeview(self.frame_grid, columns=[ i for i in range(3)], show="headings")
        self.grid.grid(row=0 , column=0)
        x = 0 
        for i in self.text:
            self.grid.heading(x, text=i)
            x += 1
    
        for i in data:
            self.grid.insert('', 'end', values=i)
        
    def select_user(self):
        try:
            return [True, self.grid.item(self.grid.selection())['values'][0]]
        except:
            return [False, "Error", "Selecciones un usuario"]

    def close(self):
        self.main.mainloop() 


