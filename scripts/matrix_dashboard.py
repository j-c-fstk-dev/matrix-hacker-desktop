#!/usr/bin/env python3
"""
Matrix Hacker Dashboard
Sistema de monitoramento interativo com visual Matrix
Otimizado para hardware antigo
"""

import os
import sys
import time
import psutil
import platform
from datetime import datetime

try:
    from pyfiglet import figlet_format
    HAS_FIGLET = True
except ImportError:
    HAS_FIGLET = False

try:
    from termcolor import colored
    HAS_COLOR = True
except ImportError:
    HAS_COLOR = False

# Cores Matrix
GREEN = '\033[92m'
DARK_GREEN = '\033[32m'
BLACK = '\033[30m'
RESET = '\033[0m'
BOLD = '\033[1m'
CLEAR = '\033[2J\033[H'

def clear_screen():
    """Limpa a tela"""
    print(CLEAR, end='')

def print_header():
    """Imprime o cabeçalho Matrix"""
    if HAS_FIGLET and HAS_COLOR:
        banner = figlet_format("MATRIX OS", font='small')
        print(colored(banner, 'green', attrs=['bold']))
    else:
        print(f"{GREEN}{BOLD}")
        print("╔═══════════════════════════════════════════════════════════╗")
        print("║                                                           ║")
        print("║   ███╗   ███╗ █████╗ ████████╗██████╗ ██╗██╗  ██╗       ║")
        print("║   ████╗ ████║██╔══██╗╚══██╔══╝██╔══██╗██║╚██╗██╔╝       ║")
        print("║   ██╔████╔██║███████║   ██║   ██████╔╝██║ ╚███╔╝        ║")
        print("║   ██║╚██╔╝██║██╔══██║   ██║   ██╔══██╗██║ ██╔██╗        ║")
        print("║   ██║ ╚═╝ ██║██║  ██║   ██║   ██║  ██║██║██╔╝ ██╗       ║")
        print("║   ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝       ║")
        print("║                                                           ║")
        print("║            HACKER DESKTOP - SYSTEM MONITOR               ║")
        print("║                                                           ║")
        print("╚═══════════════════════════════════════════════════════════╝")
        print(f"{RESET}")

def get_size(bytes, suffix="B"):
    """Converte bytes para formato legível"""
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def print_system_info():
    """Imprime informações do sistema"""
    uname = platform.uname()
    
    print(f"{GREEN}┌─[ SYSTEM INFO ]─────────────────────────────────────────┐{RESET}")
    print(f"{DARK_GREEN}│{RESET} System    : {GREEN}{uname.system}{RESET}")
    print(f"{DARK_GREEN}│{RESET} Node      : {GREEN}{uname.node}{RESET}")
    print(f"{DARK_GREEN}│{RESET} Release   : {GREEN}{uname.release}{RESET}")
    print(f"{DARK_GREEN}│{RESET} Machine   : {GREEN}{uname.machine}{RESET}")
    print(f"{DARK_GREEN}│{RESET} Processor : {GREEN}{uname.processor}{RESET}")
    print(f"{GREEN}└─────────────────────────────────────────────────────────┘{RESET}")
    print()

def print_cpu_info():
    """Imprime informações de CPU"""
    print(f"{GREEN}┌─[ CPU STATUS ]──────────────────────────────────────────┐{RESET}")
    print(f"{DARK_GREEN}│{RESET} Physical cores : {GREEN}{psutil.cpu_count(logical=False)}{RESET}")
    print(f"{DARK_GREEN}│{RESET} Total cores    : {GREEN}{psutil.cpu_count(logical=True)}{RESET}")
    
    cpufreq = psutil.cpu_freq()
    if cpufreq:
        print(f"{DARK_GREEN}│{RESET} Max Frequency  : {GREEN}{cpufreq.max:.2f}Mhz{RESET}")
        print(f"{DARK_GREEN}│{RESET} Current Freq   : {GREEN}{cpufreq.current:.2f}Mhz{RESET}")
    
    print(f"{DARK_GREEN}│{RESET} CPU Usage      : {GREEN}{psutil.cpu_percent()}%{RESET}")
    
    # Uso por core
    print(f"{DARK_GREEN}│{RESET} Per-core usage :{RESET}")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        bar_length = int(percentage / 5)  # Barra de 20 caracteres
        bar = "█" * bar_length + "░" * (20 - bar_length)
        print(f"{DARK_GREEN}│{RESET}   Core {i:02d} [{GREEN}{bar}{RESET}] {GREEN}{percentage:>5.1f}%{RESET}")
    
    print(f"{GREEN}└─────────────────────────────────────────────────────────┘{RESET}")
    print()

def print_memory_info():
    """Imprime informações de memória"""
    svmem = psutil.virtual_memory()
    swap = psutil.swap_memory()
    
    print(f"{GREEN}┌─[ MEMORY STATUS ]───────────────────────────────────────┐{RESET}")
    print(f"{DARK_GREEN}│{RESET} RAM Total     : {GREEN}{get_size(svmem.total)}{RESET}")
    print(f"{DARK_GREEN}│{RESET} RAM Available : {GREEN}{get_size(svmem.available)}{RESET}")
    print(f"{DARK_GREEN}│{RESET} RAM Used      : {GREEN}{get_size(svmem.used)}{RESET}")
    print(f"{DARK_GREEN}│{RESET} RAM Percent   : {GREEN}{svmem.percent}%{RESET}")
    
    # Barra de uso
    bar_length = int(svmem.percent / 5)
    bar = "█" * bar_length + "░" * (20 - bar_length)
    print(f"{DARK_GREEN}│{RESET} RAM Usage [{GREEN}{bar}{RESET}]")
    
    print(f"{DARK_GREEN}│{RESET}")
    print(f"{DARK_GREEN}│{RESET} SWAP Total    : {GREEN}{get_size(swap.total)}{RESET}")
    print(f"{DARK_GREEN}│{RESET} SWAP Used     : {GREEN}{get_size(swap.used)}{RESET}")
    print(f"{DARK_GREEN}│{RESET} SWAP Percent  : {GREEN}{swap.percent}%{RESET}")
    print(f"{GREEN}└─────────────────────────────────────────────────────────┘{RESET}")
    print()

def print_disk_info():
    """Imprime informações de disco"""
    print(f"{GREEN}┌─[ DISK STATUS ]─────────────────────────────────────────┐{RESET}")
    
    partitions = psutil.disk_partitions()
    for partition in partitions:
        print(f"{DARK_GREEN}│{RESET} Device    : {GREEN}{partition.device}{RESET}")
        print(f"{DARK_GREEN}│{RESET} Mountpoint: {GREEN}{partition.mountpoint}{RESET}")
        print(f"{DARK_GREEN}│{RESET} Type      : {GREEN}{partition.fstype}{RESET}")
        
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
            print(f"{DARK_GREEN}│{RESET} Total     : {GREEN}{get_size(partition_usage.total)}{RESET}")
            print(f"{DARK_GREEN}│{RESET} Used      : {GREEN}{get_size(partition_usage.used)}{RESET}")
            print(f"{DARK_GREEN}│{RESET} Free      : {GREEN}{get_size(partition_usage.free)}{RESET}")
            print(f"{DARK_GREEN}│{RESET} Percent   : {GREEN}{partition_usage.percent}%{RESET}")
            
            # Barra de uso
            bar_length = int(partition_usage.percent / 5)
            bar = "█" * bar_length + "░" * (20 - bar_length)
            print(f"{DARK_GREEN}│{RESET} Usage [{GREEN}{bar}{RESET}]")
            print(f"{DARK_GREEN}│{RESET}")
        except PermissionError:
            continue
    
    print(f"{GREEN}└─────────────────────────────────────────────────────────┘{RESET}")
    print()

def print_network_info():
    """Imprime informações de rede"""
    print(f"{GREEN}┌─[ NETWORK STATUS ]──────────────────────────────────────┐{RESET}")
    
    if_addrs = psutil.net_if_addrs()
    for interface_name, interface_addresses in if_addrs.items():
        for address in interface_addresses:
            if str(address.family) == 'AddressFamily.AF_INET':
                print(f"{DARK_GREEN}│{RESET} Interface : {GREEN}{interface_name}{RESET}")
                print(f"{DARK_GREEN}│{RESET} IP Address: {GREEN}{address.address}{RESET}")
                print(f"{DARK_GREEN}│{RESET} Netmask   : {GREEN}{address.netmask}{RESET}")
                print(f"{DARK_GREEN}│{RESET}")
    
    net_io = psutil.net_io_counters()
    print(f"{DARK_GREEN}│{RESET} Bytes Sent    : {GREEN}{get_size(net_io.bytes_sent)}{RESET}")
    print(f"{DARK_GREEN}│{RESET} Bytes Received: {GREEN}{get_size(net_io.bytes_recv)}{RESET}")
    
    print(f"{GREEN}└─────────────────────────────────────────────────────────┘{RESET}")
    print()

def print_process_info():
    """Imprime top 5 processos"""
    print(f"{GREEN}┌─[ TOP PROCESSES ]───────────────────────────────────────┐{RESET}")
    
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    
    # Ordenar por uso de CPU
    processes = sorted(processes, key=lambda p: p['cpu_percent'] or 0, reverse=True)[:5]
    
    print(f"{DARK_GREEN}│{RESET} {'PID':<8} {'NAME':<20} {'CPU%':<8} {'MEM%':<8}{RESET}")
    print(f"{DARK_GREEN}│{RESET} {'-'*8} {'-'*20} {'-'*8} {'-'*8}{RESET}")
    
    for proc in processes:
        pid = proc['pid']
        name = proc['name'][:20]
        cpu = proc['cpu_percent'] or 0
        mem = proc['memory_percent'] or 0
        print(f"{DARK_GREEN}│{RESET} {GREEN}{pid:<8} {name:<20} {cpu:<8.1f} {mem:<8.1f}{RESET}")
    
    print(f"{GREEN}└─────────────────────────────────────────────────────────┘{RESET}")
    print()

def print_time():
    """Imprime data e hora"""
    now = datetime.now()
    print(f"{GREEN}┌─[ SYSTEM TIME ]─────────────────────────────────────────┐{RESET}")
    print(f"{DARK_GREEN}│{RESET} Date: {GREEN}{now.strftime('%Y-%m-%d')}{RESET}")
    print(f"{DARK_GREEN}│{RESET} Time: {GREEN}{now.strftime('%H:%M:%S')}{RESET}")
    print(f"{GREEN}└─────────────────────────────────────────────────────────┘{RESET}")
    print()

def main():
    """Função principal"""
    try:
        while True:
            clear_screen()
            print_header()
            print_time()
            print_system_info()
            print_cpu_info()
            print_memory_info()
            print_disk_info()
            print_network_info()
            print_process_info()
            
            print(f"{GREEN}Press Ctrl+C to exit...{RESET}")
            time.sleep(5)  # Atualiza a cada 5 segundos
            
    except KeyboardInterrupt:
        clear_screen()
        print(f"\n{GREEN}Exiting Matrix Dashboard...{RESET}\n")
        sys.exit(0)

if __name__ == "__main__":
    main()
