# 🚀 Mxnmap - Nmap Multitool Bundle

![Versión](https://img.shields.io/badge/versión-1.0-blue)
![Plataforma](https://img.shields.io/badge/plataforma-Linux%20%7C%20Termux%20%7C%20Windows-lightgrey)
![Licencia](https://img.shields.io/badge/licencia-GPLv3-green)
![Python](https://img.shields.io/badge/python-3.x-yellow)
![Estado](https://img.shields.io/badge/estado-estable-brightgreen)

> **"La navaja suiza del escaneo de redes"**  
> *Mxnmap empaqueta Nmap + nping + ncat + ndiff + zenmap en una sola herramienta portable.*

---

## ✨ Características

| Herramienta | Función | Disponible |
|:---|:---|:---:|
| 🔍 **Nmap** | Escaneo de puertos, OS, servicios | ✅ |
| 📡 **Nping** | Generación de paquetes personalizados | ✅ |
| 🔗 **Ncat** | Conexiones de red, reverse shells | ✅ |
| 📊 **Ndiff** | Comparación de escaneos | ✅ |
| 🖥️ **Zenmap** | Interfaz gráfica oficial | ✅ (Win/Linux) |
| 🎨 **Banner propio** | Estilo Mxnmap | ✅ |

---

## 📦 Instalación (solo 3 pasos)

### 🐧 Linux / 📱 Termux
```bash
git clone https://github.com/Falconmx1/Mxnmap---Nmap-Multitool-Bundle-for-Linux-Termux-Windows.git
cd Mxnmap---Nmap-Multitool-Bundle-for-Linux-Termux-Windows
chmod +x install.sh
./install.sh

🪟 Windows
git clone https://github.com/Falconmx1/Mxnmap---Nmap-Multitool-Bundle-for-Linux-Termux-Windows.git
cd Mxnmap---Nmap-Multitool-Bundle-for-Linux-Termux-Windows
install.bat

🎮 Uso (ejemplos rápidos)
# Escaneo de puertos comunes
mxnmap nmap -sV -p 80,443,22 scanme.org

# Generar paquetes TCP a Google
mxnmap nping --tcp -p 80 google.com

# Poner un listener en puerto 4444
mxnmap ncat -lvp 4444

# Comparar dos escaneos
mxnmap ndiff antes.xml despues.xml

# Lanzar interfaz gráfica (Windows/Linux)
mxnmap zenmap

