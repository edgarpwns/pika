
# 🐭 PIKA – Herramienta de Escaneo con Nmap

¡Una herramienta simple, útil y adorable que te ayuda a hacer escaneos de red con `nmap`… con la energía de Pikachu! ⚡

---

## ⚙️ Características

- 🔍 Descubre hosts activos en una red.
- 📡 Escanea todos los puertos de una IP.
- 🛡️ Realiza escaneos de versiones y vulnerabilidades con `-sCV`.
- 🗃️ Guarda automáticamente los resultados en archivos `.txt` con el nombre que elijas.
- 🐭 Banner de Pikachu animado y a color al iniciar y salir.

---

## 📦 Requisitos

- Python 3
- Nmap instalado
- Terminal compatible con colores ANSI (la mayoría de consolas modernas)

---

## 🧪 Instalación

1. Clona este repositorio o descarga el archivo `pika.py`:

```bash
git clone https://github.com/edgarpwns/pika.git
cd pika
```

2. Asegúrate de tener Python y Nmap:

```bash
python3 --version
nmap --version
```

3. Dale permisos de ejecución (opcional):

```bash
chmod +x pika.py
```

---

## 🚀 Uso

Ejecuta la herramienta:

```bash
python3 pika.py
```

Sigue las instrucciones del menú:

```
1. Buscar hosts en una red
2. Escaneo de puertos
3. Escaneo de versiones y vulnerabilidades
4. Salir
```

Los resultados se guardarán en archivos `.txt` en la misma carpeta.

---

## 📁 Ejemplo de uso

```bash
Elige una opción (1-4): 2
Introduce la IP del target: 192.168.1.10
Nombre del archivo para guardar el resultado: puertos_192
...
Resultado guardado en puertos_192.txt
```

---

## 🧠 Notas

- Para escanear vulnerabilidades, primero debes hacer el escaneo de puertos.
- El script guarda la IP y puertos automáticamente para usarlos en el paso siguiente.

---

## 📜 Licencia

Este proyecto está bajo la licencia MIT. Usa libremente, con crédito. ⚡

---

## 🧡 Créditos

Creado por **edgarpwns** con amor y electricidad.
