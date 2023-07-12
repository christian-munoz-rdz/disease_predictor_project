import tkinter as tk

def boton1_click():
    print("Botón 1 presionado")

def boton2_click():
    print("Botón 2 presionado")

# Crear una ventana
ventana = tk.Tk()

# Establecer dimensiones de la ventana
ventana.geometry("400x400")

# Crear los botones
boton1 = tk.Button(ventana, text="Botón 1", command=boton1_click, width=20, height=2)
boton2 = tk.Button(ventana, text="Botón 2", command=boton2_click, width=20, height=2)

# Colocar los botones en la ventana con el sistema grid
boton1.grid(row=0, column=0, pady=(200, 50))
boton2.grid(row=1, column=0, pady=50)

# Centrar los botones verticalmente en la ventana
ventana.grid_rowconfigure(0, weight=1)
ventana.grid_rowconfigure(1, weight=1)
ventana.grid_columnconfigure(0, weight=1)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()


