#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mxnmap - Nmap Multitool Bundle
Autor: Falconmx1 (Maik)
Descripción: Herramienta que empaqueta Nmap, Nping, Ncat, Ndiff y Zenmap
             con un toque personal y modo demo incluido.
"""

import os
import sys
import subprocess
import platform

# ==================== CONFIGURACIÓN DE COLORES ====================
# Colores ANSI para terminal (funciona en Linux, Termux y Windows 10+)
try:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    MAGENTA = '\033[95m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
except:
    # Si no soporta colores, se desactivan
    CYAN = GREEN = YELLOW = RED = MAGENTA = RESET = BOLD = DIM = ''

# ==================== MODO DEMO ====================
DEMO_MODE = False  # Cambiar a True para modo demo (simula comandos sin instalar nada)

# ==================== BANNER PRINCIPAL ====================
BANNER = f"""
{BOLD}{CYAN}    ╔═══════════════════════════════════════════════════════╗
    ║                                                           ║
    ║     MMMMM  X   X  N   N  M   M  A   PPP  M   M  A   PPP  ║
    ║     M   M   X X   NN  N  MM MM  A A P P  MM MM  A A P P  ║
    ║     M   M    X    N N N  M M M  AAA PPP  M M M  AAA PPP  ║
    ║     M   M   X X   N  NN  M   M  A A P    M   M  A A P    ║
    ║     MMMMM  X   X  N   N  M   M  A A P    M   M  A A P    ║
    ║                                                           ║
    ║   {YELLOW}Mxnmap - Nmap Multitool Bundle{RESET}{BOLD}{CYAN}                     ║
    ║   {GREEN}"Pa' chambear como los grandes"{RESET}{BOLD}{CYAN}                  ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝{RESET}
"""

# ==================== MENSAJE DE BIENVENIDA ====================
def mostrar_bienvenida():
    """Muestra un mensaje de bienvenida personalizado según el sistema."""
    sistema = platform.system()
    arquitectura = platform.machine()
    python_version = platform.python_version()
    
    print(f"{DIM}{'='*55}{RESET}")
    
    if sistema == "Windows":
        print(f"{GREEN}💻 ¡Listo pa' chambear en Windows, mi rey!{RESET}")
        print(f"{CYAN}   Versión: {platform.version()}{RESET}")
    elif sistema == "Linux":
        # Detectar si es Termux o Linux normal
        try:
            if os.path.exists("/data/data/com.termux"):
                print(f"{GREEN}📱 Termux detectado - ¡Modo callejero activado!{RESET}")
                print(f"{CYAN}   Escaneando desde tu Android como un campeón{RESET}")
                DEMO_MODE = False
            else:
                print(f"{GREEN}🐧 Linux detectado - Modo Hacker profesional ON{RESET}")
                try:
                    with open("/etc/os-release") as f:
                        for line in f:
                            if "PRETTY_NAME" in line:
                                distro = line.split("=")[1].strip().strip('"')
                                print(f"{CYAN}   Distribución: {distro}{RESET}")
                                break
                except:
                    pass
        except:
            print(f"{GREEN}🐧 Linux detectado - Modo Hacker profesional ON{RESET}")
    elif sistema == "Darwin":
        print(f"{GREEN}🍎 MacOS detectado - ¡Estás en la manzana!{RESET}")
    else:
        print(f"{GREEN}❓ Sistema detectado: {sistema}{RESET}")
    
    print(f"{CYAN}   Arquitectura: {arquitectura}{RESET}")
    print(f"{CYAN}   Python {python_version}{RESET}")
    
    if DEMO_MODE:
        print(f"{YELLOW}⚠️  MODO DEMO ACTIVADO - Los comandos se simularán{RESET}")
    else:
        print(f"{GREEN}✅ Modo real activado - A chambear se ha dicho{RESET}")
    
    print(f"{DIM}{'='*55}{RESET}\n")

# ==================== MOSTRAR AYUDA ====================
def show_help():
    """Muestra la ayuda de la herramienta."""
    help_text = f"""
{BOLD}{YELLOW}┌─────────────────────────────────────────────────────────────┐
│                     GUÍA DE USO MXNMAP                     │
└─────────────────────────────────────────────────────────────┘{RESET}

{BOLD}{GREEN}COMANDOS DISPONIBLES:{RESET}

  {CYAN}nmap [args]{RESET}      → Escaneo de red (detección de puertos, OS, servicios)
  {CYAN}nping [args]{RESET}     → Generación de paquetes (TCP, UDP, ICMP)
  {CYAN}ncat [args]{RESET}      → Networking / reverse shells / transferencia archivos
  {CYAN}ndiff [args]{RESET}     → Comparar dos escaneos XML
  {CYAN}zenmap{RESET}            → Interfaz gráfica oficial (Windows/Linux)
  {CYAN}banner{RESET}            → Mostrar el banner nuevamente
  {CYAN}help{RESET}              → Mostrar esta ayuda
  {CYAN}demo{RESET}              → Activar/desactivar modo demo
  {CYAN}status{RESET}            → Verificar herramientas instaladas

{BOLD}{GREEN}EJEMPLOS PRÁCTICOS:{RESET}

  {DIM}# Escaneo rápido de puertos comunes{RESET}
  {BOLD}mxnmap nmap -sV -p 80,443,22 scanme.org{RESET}

  {DIM}# Generar paquetes TCP a Google{RESET}
  {BOLD}mxnmap nping --tcp -p 80 google.com{RESET}

  {DIM}# Poner un listener en puerto 4444 (para reverse shell){RESET}
  {BOLD}mxnmap ncat -lvp 4444{RESET}

  {DIM}# Conectarse a un listener remoto{RESET}
  {BOLD}mxnmap ncat 192.168.1.100 4444{RESET}

  {DIM}# Comparar resultados de dos escaneos{RESET}
  {BOLD}mxnmap ndiff antes.xml despues.xml{RESET}

  {DIM}# Lanzar Zenmap (interfaz gráfica){RESET}
  {BOLD}mxnmap zenmap{RESET}

{BOLD}{YELLOW}CONSEJOS:{RESET}
  • Usa {CYAN}mxnmap status{RESET} para ver qué herramientas tienes instaladas
  • Activa modo demo con {CYAN}mxnmap demo{RESET} para practicar sin instalar nada
  • El banner se muestra automáticamente al inicio
"""
    print(help_text)

# ==================== VERIFICAR HERRAMIENTAS INSTALADAS ====================
def check_status():
    """Verifica qué herramientas del paquete Nmap están instaladas."""
    print(f"\n{BOLD}{CYAN}🔍 VERIFICANDO HERRAMIENTAS INSTALADAS...{RESET}\n")
    
    herramientas = ["nmap", "nping", "ncat", "ndiff", "zenmap"]
    resultados = {}
    
    for tool in herramientas:
        try:
            if platform.system() == "Windows":
                # En Windows buscar en PATH
                result = subprocess.run(["where", tool], capture_output=True, text=True)
                if result.returncode == 0:
                    resultados[tool] = True
                else:
                    # Buscar en ubicación común de Nmap
                    if tool == "zenmap":
                        if os.path.exists(r"C:\Program Files (x86)\Nmap\zenmap.exe"):
                            resultados[tool] = True
                        else:
                            resultados[tool] = False
                    else:
                        resultados[tool] = False
            else:
                # En Linux/Termux
                result = subprocess.run(["which", tool], capture_output=True, text=True)
                resultados[tool] = result.returncode == 0
        except:
            resultados[tool] = False
    
    # Mostrar resultados
    for tool, installed in resultados.items():
        if installed:
            print(f"  {GREEN}✅ {tool.upper()}{RESET} - Instalado")
        else:
            print(f"  {RED}❌ {tool.upper()}{RESET} - No instalado")
    
    print(f"\n{DIM}Ejecuta el instalador de Mxnmap para instalar las herramientas faltantes{RESET}\n")

# ==================== MODO DEMO (SIMULADOR) ====================
def demo_mode_command(cmd, args):
    """Simula la ejecución de comandos en modo demo."""
    print(f"\n{YELLOW}🎬 [MODO DEMO] Ejecutando: {cmd} {' '.join(args)}{RESET}")
    print(f"{DIM}─────────────────────────────────────────────────────────────{RESET}")
    
    demos = {
        "nmap": f"""
{BOLD}{CYAN}🎯 SIMULACIÓN DE ESCANEO NMAP{RESET}

Comando real ejecutado habría sido:
  nmap {' '.join(args)}

Resultado simulado:
  Starting Nmap 7.95 ( https://nmap.org )
  Host is up (0.034s latency).
  Not shown: 997 closed tcp ports (conn-refused)
  PORT     STATE    SERVICE    VERSION
  22/tcp   open     ssh        OpenSSH 8.9p1 Ubuntu 3ubuntu0.1
  80/tcp   open     http       Apache httpd 2.4.52
  443/tcp  open     https      Apache httpd 2.4.52

  Nmap done: 1 IP address (1 host up) scanned in 2.34 seconds
{DIM}─────────────────────────────────────────────────────────────{RESET}
""",
        "nping": f"""
{BOLD}{CYAN}📡 SIMULACIÓN DE NPING{RESET}

  Enviando 5 paquetes TCP a {' '.join(args)}
  Modo demo: Se habrían enviado los paquetes con éxito
{DIM}─────────────────────────────────────────────────────────────{RESET}
""",
        "ncat": f"""
{BOLD}{CYAN}🔗 SIMULACIÓN DE NCAT{RESET}

  Conexión simulada a {' '.join(args)}
  (En modo real, ncat establecería la conexión)
{DIM}─────────────────────────────────────────────────────────────{RESET}
""",
        "ndiff": f"""
{BOLD}{CYAN}📊 SIMULACIÓN DE NDIFF{RESET}

  Comparando archivos: {' '.join(args)}
  Los escaneos son idénticos (modo demo)
{DIM}─────────────────────────────────────────────────────────────{RESET}
"""
    }
    
    # Buscar demo específico o mostrar genérico
    for key in demos:
        if cmd == key:
            print(demos[key])
            return
    
    print(f"{YELLOW}  Simulación de {cmd} {' '.join(args)}{RESET}")
    print(f"  (Compatible con modo demo)\n")

# ==================== FUNCIÓN PRINCIPAL ====================
def main():
    """Función principal de Mxnmap."""
    global DEMO_MODE
    
    # Mostrar banner
    print(BANNER)
    
    # Mostrar mensaje de bienvenida personalizado
    mostrar_bienvenida()
    
    # Si no hay argumentos, mostrar ayuda
    if len(sys.argv) == 1:
        show_help()
        return
    
    # Obtener comando y argumentos
    cmd = sys.argv[1].lower()
    args = sys.argv[2:]
    
    # Comandos especiales de Mxnmap
    if cmd == "banner":
        print(BANNER)
        return
    elif cmd == "help" or cmd == "--help" or cmd == "-h":
        show_help()
        return
    elif cmd == "status" or cmd == "--status":
        check_status()
        return
    elif cmd == "demo":
        DEMO_MODE = not DEMO_MODE
        estado = "activado" if DEMO_MODE else "desactivado"
        print(f"{GREEN}✅ Modo demo {estado}{RESET}")
        return
    
    # Mapeo de comandos a ejecutables reales
    executables = {
        "nmap": "nmap",
        "nping": "nping",
        "ncat": "ncat",
        "ndiff": "ndiff",
        "zenmap": "zenmap" if platform.system() != "Windows" else r"C:\Program Files (x86)\Nmap\zenmap.exe"
    }
    
    # Verificar si el comando es válido
    if cmd in executables:
        if DEMO_MODE:
            # Modo demo: simular ejecución
            demo_mode_command(cmd, args)
        else:
            # Modo real: ejecutar el comando
            try:
                print(f"{DIM}[*] Ejecutando: {cmd} {' '.join(args)}{RESET}\n")
                result = subprocess.run([executables[cmd]] + args)
                if result.returncode != 0:
                    print(f"{RED}[!] El comando terminó con error código {result.returncode}{RESET}")
            except FileNotFoundError:
                print(f"{RED}[!] Error: {cmd} no está instalado en el sistema.{RESET}")
                print(f"{YELLOW}    Ejecuta el instalador de Mxnmap primero o activa modo demo.{RESET}")
                print(f"    Para modo demo: {CYAN}mxnmap demo{RESET}")
            except KeyboardInterrupt:
                print(f"\n{YELLOW}[!] Comando interrumpido por el usuario{RESET}")
            except Exception as e:
                print(f"{RED}[!] Error inesperado: {e}{RESET}")
    else:
        print(f"{RED}[!] Comando desconocido: {cmd}{RESET}")
        show_help()

# ==================== PUNTO DE ENTRADA ====================
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{YELLOW}[!] Mxnmap cerrado por el usuario{RESET}")
        sys.exit(0)
    except Exception as e:
        print(f"{RED}[!] Error fatal: {e}{RESET}")
        sys.exit(1)
