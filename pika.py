
import subprocess
import re

open_ports = []
target_ip = None

# ANSI color codes
YELLOW = "\033[93m"
RESET = "\033[0m"

def show_banner():
    banner = r"""
 (\__/)
 (o^.^)     ¡Pika! Hecho por edgarpwns
 z(_(")(")
"""
    print(YELLOW + banner + RESET)

def farewell_banner():
    banner = r"""
 (\__/)
 (o^.^)    Pika... ¡Hasta luego!
 z(_(")(")
"""
    print(YELLOW + banner + RESET)

def scan_hosts():
    rango = input("Introduce el rango de red (ej. 192.168.1.0/24): ")
    filename = input("Nombre del archivo para guardar el resultado (sin extensión): ") + ".txt"
    print(f"Buscando hosts en la red {rango}...")

    result = subprocess.run(["sudo", "nmap", "-sn", rango], capture_output=True, text=True)
    with open(filename, "w") as f:
        f.write(result.stdout)
    print(f"Resultado guardado en {filename}")

def scan_ports():
    global open_ports, target_ip
    target_ip = input("Introduce la IP del target: ")
    filename = input("Nombre del archivo para guardar el resultado (sin extensión): ") + ".txt"
    print(f"Escaneando puertos abiertos en {target_ip}...")

    result = subprocess.run(
        ["sudo", "nmap", "-p-", "-sS", "--min-rate", "5000", "-vvv", "-n", "-Pn", target_ip],
        capture_output=True, text=True
    )

    open_ports = re.findall(r"(\d+)/tcp\s+open", result.stdout)

    with open(filename, "w") as f:
        f.write(result.stdout)

    if open_ports:
        print("Puertos abiertos detectados:", ", ".join(open_ports))
    else:
        print("No se detectaron puertos abiertos.")
    print(f"Resultado guardado en {filename}")

def scan_vulns():
    global open_ports, target_ip

    if not open_ports or not target_ip:
        print("Primero debes escanear los puertos con la opción 2.")
        return

    filename = input("Nombre del archivo para guardar el resultado (sin extensión): ") + ".txt"
    ports_str = ",".join(open_ports)
    print(f"Escaneando servicios y vulnerabilidades en {target_ip} (puertos: {ports_str})...")

    result = subprocess.run(
        ["sudo", "nmap", "-p", ports_str, "-sCV", target_ip],
        capture_output=True, text=True
    )

    with open(filename, "w") as f:
        f.write(result.stdout)

    print(f"Resultado guardado en {filename}")

def main():
    show_banner()
    while True:
        print("\n¿Qué quieres hacer?")
        print("1. Buscar hosts en una red")
        print("2. Escaneo de puertos")
        print("3. Escaneo de versiones y vulnerabilidades")
        print("4. Salir")

        choice = input("Elige una opción (1-4): ")

        if choice == "1":
            scan_hosts()
        elif choice == "2":
            scan_ports()
        elif choice == "3":
            scan_vulns()
        elif choice == "4":
            farewell_banner()
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()

# Hecho por edgarpwns
