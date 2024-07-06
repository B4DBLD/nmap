import nmap
import os

def get_user_input():
    hosts = input("Ingrese los hosts (por ejemplo, 192.168.1.1 o 192.168.1.1-254): ")
    ports = input("Ingrese los puertos (por ejemplo, 22,80 o 1-1024): ")
    arguments = input("Ingrese los argumentos adicionales (por ejemplo, -sS -O): ")
    run_as_sudo = input("¿Desea ejecutar como superusuario? (s/n): ").strip().lower()

    return hosts, ports, arguments, run_as_sudo == "s"

def run_nmap_scan(hosts, ports, arguments, run_as_sudo):
    sudo_prefix = "sudo " if run_as_sudo else ""
    command = f"{sudo_prefix}nmap {arguments} -p {ports} {hosts}"
    
    print(f"Ejecutando: {command}")
    
    # Ejecutar el comando nmap directamente si se requiere sudo, o utilizar la API de python-nmap si no
    if run_as_sudo:
        os.system(command)
    else:
        try:
            nm = nmap.PortScanner()
            nm.scan(hosts=hosts, ports=ports, arguments=arguments)
            display_results(nm)
        except nmap.PortScannerError as e:
            print(f"Error al ejecutar nmap: {e}")

def display_results(nm):
    for host in nm.all_hosts():
        print(f"\nHost: {host} ({nm[host].hostname()})")
        print(f"Estado: {nm[host].state()}")
        
        for proto in nm[host].all_protocols():
            print(f"\nProtocolo: {proto}")
            lport = nm[host][proto].keys()
            for port in lport:
                print(f"Puerto: {port}\tEstado: {nm[host][proto][port]['state']}")

if __name__ == "__main__":
    hosts, ports, arguments, run_as_sudo = get_user_input()
    run_nmap_scan(hosts, ports, arguments, run_as_sudo)
