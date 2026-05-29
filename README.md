# 🚀 Mxnmap - Nmap Multitool Bundle

**Mxnmap** es un empaquetado listo para usar de **Nmap + Nping + Ncat + Ndiff + Zenmap** con un toque casero. Ideal para pentesters, administradores y curiosos.

## 📦 Instalación

### Linux / Termux
```bash
git clone https://github.com/Falconmx1/Mxnmap.git
cd Mxnmap
chmod +x install.sh
./install.sh

Windows
git clone https://github.com/Falconmx1/Mxnmap.git
cd Mxnmap
install.bat

🎮 Uso
mxnmap nmap -sV scanme.org
mxnmap nping --tcp -p 80 google.com
mxnmap ncat -lvp 4444
mxnmap ndiff escaneo1.xml escaneo2.xml
mxnmap zenmap
