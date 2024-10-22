import os
import sys
import pyperclip

def copy_files_with_extensions_to_clipboard(extensions):
    # Variable que contendrá todo el contenido de los archivos
    clipboard_content = ""

    # Recorrer todos los directorios y archivos recursivamente
    for root, dirs, files in os.walk(os.getcwd()):
        for filename in files:
            # Comprobar si el archivo tiene alguna de las extensiones especificadas
            if any(filename.endswith(ext) for ext in extensions):
                # Ruta completa del archivo
                file_path = os.path.join(root, filename)
                
                # Añadir el encabezado con el nombre del archivo
                clipboard_content += f"\n---------------------\n{file_path}\n---------------------\n"
                
                # Leer el archivo y añadir su contenido
                with open(file_path, 'r') as infile:
                    clipboard_content += infile.read()
    
    # Copiar el contenido al portapapeles
    pyperclip.copy(clipboard_content)
    print("Contenido copiado al portapapeles.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python script.py <ext1> <ext2> ...")
    else:
        # Leer las extensiones de los argumentos de la línea de comandos
        extensions = sys.argv[1:]
        copy_files_with_extensions_to_clipboard(extensions)
