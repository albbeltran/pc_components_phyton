import time
import psutil
import platform

print("Sistema operativo:", platform.system())
print("Version:", platform.release())
print("Arquitectura:", platform.machine())
print("Núcleos logicos:", psutil.cpu_count(logical=True))
print("Núcleos fisicos:", psutil.cpu_count(logical=False))
print("Frecuencia actual de la CPU:", psutil.cpu_freq().current, "MHz")
print('Uso del CPU: ', psutil.cpu_percent())
print('Memoria RAM total: ', psutil.virtual_memory().total)
print('Memoria RAM disponible: ', psutil.virtual_memory().available)
print('Memoria RAM libre: ', psutil.virtual_memory().free)
print('Memoria RAM en uso', psutil.virtual_memory().percent)
print(psutil.disk_usage('C:./'))
print(psutil.disk_usage('D:/'))
print(psutil.users()[0].name)

""" Si hubiera mas usuarios:
    
user_list = psutil.users()
user_names = [user.name for user in user_list]
print(user_names)
"""

"""
print(psutil.net_connections())

for proc in psutil.process_iter(['pid', 'name', 'username']):
    print(proc.info)
"""
    
print("\n")
    
def display_usage(cpu_usage, mem_usage, bars=50):
    cpu_percent = (cpu_usage / 100.0)
    cpu_bar = '█' * int(cpu_percent * bars) + '░' * (bars - int(cpu_percent * bars))
    mem_percent = (mem_usage / 100.0)
    mem_bar = '█' * int(mem_percent * bars) + '░' * (bars - int(mem_percent * bars))
        
    print(f"\rCPU en uso: |{cpu_bar}| {cpu_usage: .2f}%  ", end="")
    print(f"MEM en uso: |{mem_bar}| {mem_usage:.2f}%  ", end="\r")
    
while True:
    display_usage(psutil.cpu_percent(), psutil.virtual_memory().percent, 30)
    time.sleep(0.5)
