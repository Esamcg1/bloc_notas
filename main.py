import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog
from logic import SimpleTextEditor

root = tk.Tk()
root.title("BLoc de Notas")
root.configure(bg="lightblue")
root.geometry("350x500")

#Instancia a SimpleTextEditor
edito = SimpleTextEditor(root)

#Barra del menu
barra_menu = tk.Menu(root)

# Crear un menú desplegable
#menu 1
menu1 = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Menu 1", menu=menu1)

close_button = SimpleTextEditor.close_window(root)
#Crear submenus a partir del menu1
menu1.add_command(label="Nuevo", command=edito.new_file)
menu1.add_command(label="Abrir", command=edito.open_file)
menu1.add_command(label="Guardar", command=edito.save_file)
menu1.add_command(label="Cerrar", command=edito.close_window)

#configuracion para que que se tome barra_menu como la barra de menú principal
root.config(menu=barra_menu)
root.mainloop()
