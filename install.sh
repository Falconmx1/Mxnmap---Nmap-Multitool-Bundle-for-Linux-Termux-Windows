#!/bin/bash

# Colores para output
GREEN='\033[0;32m'
NC='\033[0m'

echo -e "${GREEN}[+] Iniciando instalación de Mxnmap...${NC}"

# Detectar si es Termux o Linux
if [ -d "/data/data/com.termux" ]; then
    echo "[*] Termux detectado"
    pkg update -y
    pkg install -y nmap nmap-nping ncat ndiff
    pkg install -y python
else
    echo "[*] Linux detectado"
    sudo apt update
    sudo apt install -y nmap nping ncat ndiff python3 python3-tk
    # Zenmap para Linux (si está en repos)
    sudo apt install -y zenmap || echo "[!] Zenmap no encontrado, instalando manual..."
fi

# Crear directorio de la herramienta
mkdir -p ~/.mxnmap/bin
cp mxnmap.py ~/.mxnmap/
cp config/banner.txt ~/.mxnmap/

# Crear alias/script global
echo '#!/bin/bash' > ~/.local/bin/mxnmap
echo "python3 ~/.mxnmap/mxnmap.py \"\$@\"" >> ~/.local/bin/mxnmap
chmod +x ~/.local/bin/mxnmap

echo -e "${GREEN}[✔] Mxnmap instalado. Ejecuta: mxnmap --help${NC}"
