# 📄✨ Project-to-Text: Copy Files to Clipboard! 🚀

#### 🎯 **Descripción**

**Project-to-Text** es un script en Python diseñado para buscar archivos en tu sistema, extraer su contenido y copiarlo directamente al portapapeles, todo con un solo comando. ¡Ideal para cuando necesitas procesar rápidamente múltiples archivos y llevar su información a otro lugar!

#### 💡 **Características**:
- 📂 Recursivo: busca en carpetas y subcarpetas.
- 🔍 Admite múltiples extensiones de archivo.
- 📋 Copia al portapapeles con un encabezado de archivo.


## Instrucciones de Uso

### 1. Clona el repositorio en una carpeta

```bash
git clone git@github.com:pabloreina97/project-to-text.git
```

### 2. Crea y activa un entorno virtual

Crea un entorno virtual dentro de la carpeta del proyecto para mantener las dependencias aisladas:

```bash
python -m venv venv
```

Para activarlo:

En Windows:

```bash
venv\Scripts\activate
```

En Linux/MacOS:

```bash
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Hacer el script ejecutable desde cualquier lugar

#### Opción 1: Crear un alias en la terminal
Si quieres crear un alias para ejecutar el script fácilmente:

En Windows (PowerShell):

Abre tu archivo de perfil de PowerShell ($PROFILE) con un editor de texto, por ejemplo:
```bash
notepad $PROFILE
```
Añade la siguiente línea:

```bash
function ptotex { & "C:\ruta\a\project-to-text\venv\Scripts\python.exe" "C:\ruta\a\project-to-text\main.py" @args }
```

En Linux/MacOS:

Abre tu archivo ~/.bashrc o ~/.zshrc y añade la siguiente línea:

```bash
alias ptotex='~/project-to-text/venv/bin/python ~/project-to-text/main.py'
```

Guarda el archivo y ejecuta:

```bash
source ~/.bashrc
```

#### Opción 2: Añadir el Script a una Carpeta en el `PATH`
En Windows:

Crea un archivo `.bat` en `C:\Users\TuUsuario\AppData\Local\Microsoft\WindowsApps`, llamado `ptotext.bat`.

Añade el siguiente contenido:

```bash
@echo off
"C:\ruta\a\mi_script_global\venv\Scripts\python.exe" "C:\ruta\a\mi_script_global\mi_script.py" %*
```

En Linux/MacOS:

Crea un enlace simbólico en `/usr/local/bin`:

```bash
sudo ln -s ~/mi_script_global/venv/bin/python ~/mi_script_global/mi_script.py /usr/local/bin/mi_script
```

### 5. Ejecutar el script

Una vez configurado el alias o el enlace, puedes ejecutar el script desde cualquier carpeta en la terminal con:

```bash
ptotext .txt .md

```
Este comando buscará todos los archivos con las extensiones .txt y .md en la carpeta actual y en sus subcarpetas, y copiará su contenido al portapapeles.