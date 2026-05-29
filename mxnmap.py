#!/usr/bin/env python3
import os
import sys
import subprocess
import platform

# Banner de Mxnmap
BANNER = """
    ╔═══════════════════════════════════════╗
    ║                                       ║
    ║    MMMMM  X   X  N   N  M   M  A   PPP║
    ║    M   M   X X   NN  N  MM MM  A A P P ║
    ║    M   M    X    N N N  M M M  AAA PPP ║
    ║    M   M   X X   N  NN  M   M  A A P   ║
    ║    MMMMM  X   X  N   N  M   M  A A P   ║
    ║                                       ║
    ║   Mxnmap - Nmap Multitool Bundle      ║
    ║   "Pa' chambear como los grandes"     ║
    ╚═══════════════════════════════════════╝
"""

def show_help():
    print("Uso: mxnmap <comando> [opciones]")
    print("\nComandos disponibles:")
    print("  nmap [args]   -> Escaneo de red")
    print("  nping [args]  -> Generación de paquetes")
    print("  ncat [args]   -> Networking / reverse shells")
    print("  ndiff [args]  -> Comparar escaneos")
    print("  zenmap        -> Interfaz gráfica (Windows/Linux)")
    print("  banner        -> Mostrar banner nuevamente")
    print("  help          -> Esta ayuda")
    print("\nEjemplo:")
    print("  mxnmap nmap -sV -p 80,443 scanme.org")

def main():
    print(BANNER)

    if len(sys.argv) == 1:
        show_help()
        return

    cmd = sys.argv[1]
    args = sys.argv[2:]

    # Mapeo de comandos a ejecutables reales
    executables = {
        "nmap": "nmap",
        "nping": "nping",
        "ncat": "ncat",
        "ndiff": "ndiff",
        "zenmap": "zenmap" if platform.system() != "Windows" else "C:\\Program Files (x86)\\Nmap\\zenmap.exe"
    }

    if cmd == "banner":
        print(BANNER)
    elif cmd == "help":
        show_help()
    elif cmd in executables:
        try:
            subprocess.run([executables[cmd]] + args)
        except FileNotFoundError:
            print(f"[!] Error: {cmd} no está instalado.")
            print("    Ejecuta el instalador de Mxnmap primero.")
    else:
        print(f"[!] Comando desconocido: {cmd}")
        show_help()

if __name__ == "__main__":
    main()
