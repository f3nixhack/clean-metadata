#F3NIX
import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess

def escanear_metadatos(archivo):
    try:
        resultado = subprocess.run(["exiftool", archivo], capture_output=True, text=True, check=True)
        return resultado.stdout
    except subprocess.CalledProcessError as e:
        return f"No se pudieron escanear los metadatos de {archivo}: {e}"

def eliminar_metadatos(archivo):
    try:
        resultado_anterior = escanear_metadatos(archivo)
        subprocess.run(["exiftool", "-all=", archivo], check=True)
        resultado_despues = escanear_metadatos(archivo)

        cambios = []
        for linea in resultado_anterior.split('\n'):
            if linea.strip() and linea not in resultado_despues:
                cambios.append(linea)

        return cambios
    except subprocess.CalledProcessError as e:
        return f"No se pudieron eliminar los metadatos de {archivo}: {e}"

def seleccionar_archivos():
    archivos = filedialog.askopenfilenames(title="Seleccionar archivos",
                                           filetypes=(("Todos los archivos", "*.*"),))
    for archivo in archivos:
        cambios = eliminar_metadatos(archivo)
        if cambios:
            messagebox.showinfo("Cambios Realizados", f"Se eliminaron los siguientes metadatos de {archivo}:\n\n" + '\n'.join(cambios))
        else:
            messagebox.showinfo("Sin Cambios", f"No se eliminaron metadatos de {archivo}.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Eliminar Metadatos")

# Crear un botón para seleccionar archivos
boton_seleccionar = tk.Button(ventana, text="Seleccionar Archivos", command=seleccionar_archivos)
boton_seleccionar.pack(pady=10)

# Ejecutar el bucle de eventos
ventana.mainloop()
