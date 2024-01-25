import platform 
import psutil
import multiprocessing
import sys

# Ver cuántos cpus tiene el sistema 
print(f"número de CPU del sistema: {psutil.cpu_count()}")
print(f"número de CPU del sistema: {multiprocessing.cpu_count()}")

# Tipo de máquina que tiene

print(f"Tipo de máquina: {platform.machine()}")
print(f"Tipo de máquina: {platform.architecture()[0]}")

# Tipo de software 
print(f"Tipo de software: {platform.python_compiler()}")

# Modelo o liberación del sistema 
print(f"Modelo o liberación del sistema es: {platform.release()}")

# Hostname
print(f'Hostname: {platform.node()}')

# Plataforma base 
print(f"Plataforma base: {platform.platform()}")

# Tipo de sistema operativo SO
print(f"Tipo de SO: {platform.version()}")

# Tipo de procesador 
print(f"Tipo de procesador: {platform.processor()}")

# Información del sistema 
print(f"Información del sistema: {platform.uname()}")

# Versión de python 
print(f"Versión de python: {platform.python_version()}")

# Obtener datos de la memoria RAM

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

print("Datos Memoria")
svmem = psutil.virtual_memory()
print(f"Total: {get_size(svmem.total)} | Disponible: {get_size(svmem.available)} | Usada: {get_size(svmem.used)} | Porcentaje: {svmem.percent}%")

swap = psutil.swap_memory() # Memoria de intercambio

print(f"Total: {get_size(swap.total)} | Libre: {get_size(swap.free)} | Usada: {get_size(swap.used)} | Porcentaje: {swap.percent}%")

# Obtener datos del CPU

