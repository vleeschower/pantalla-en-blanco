import tkinter as tk
raiz = tk.Tk()
raiz.title("Primera Ventana") #Cambiar el nombre de la ventana
raiz.geometry("520x480")#Configurar tamaño


entrada=tk.Entry()
entrada.place(x=50,y=50, width=150)
boton=tk.Button(text="Aceptar")
boton.place(x=50, y=100)

raiz.mainloop()
