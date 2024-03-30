Este programa es una interfaz gráfica de usuario (GUI) simple que permite al usuario seleccionar uno o varios archivos y eliminar sus metadatos. Aquí está el desglose paso a paso:
![Captura de pantalla_2024-03-30_10-32-48](https://github.com/f3nixhack/clean-metadata/assets/50671074/0672c5cf-aabb-47c5-9631-a139f10458d5)

1. Se importan las bibliotecas necesarias:
   - `tkinter` para crear la interfaz gráfica.
   - `filedialog` y `messagebox` de `tkinter` para interactuar con el sistema de archivos y mostrar mensajes.
   - `subprocess` para ejecutar procesos externos, en este caso, para llamar al programa `exiftool` que se utiliza para manipular los metadatos de archivos.

2. Se definen tres funciones principales:

   - `escanear_metadatos(archivo)`: Esta función utiliza `subprocess.run` para ejecutar el comando `exiftool` en el archivo especificado y obtener los metadatos. Luego devuelve la salida del comando.
   
   - `eliminar_metadatos(archivo)`: Esta función utiliza la función `escanear_metadatos` para obtener los metadatos antes y después de eliminarlos del archivo especificado. Luego, utilizando `subprocess.run`, elimina todos los metadatos del archivo. Finalmente, compara los metadatos antes y después para determinar qué metadatos se eliminaron y los devuelve.
   
   - `seleccionar_archivos()`: Esta función se activa cuando se presiona el botón "Seleccionar Archivos". Abre un cuadro de diálogo que permite al usuario seleccionar uno o varios archivos. Luego llama a `eliminar_metadatos` para cada archivo seleccionado y muestra un mensaje informando si se eliminaron metadatos o no.

3. Se crea la ventana principal de la aplicación (`ventana`).

4. Se crea un botón (`boton_seleccionar`) que al ser presionado activa la función `seleccionar_archivos`.

5. Se empaqueta el botón en la ventana usando `pack()`.

6. Se inicia el bucle de eventos (`mainloop()`), que esencialmente mantiene la ventana abierta y escuchando eventos del usuario hasta que se cierra la ventana.

En resumen, este programa proporciona una forma simple para que los usuarios seleccionen archivos y eliminen sus metadatos utilizando la herramienta `exiftool`, mostrando mensajes informativos sobre los cambios realizados.
