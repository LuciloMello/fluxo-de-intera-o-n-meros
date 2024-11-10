import os
os.system ('cls')

nome_arquivo = "ips.txt"

try:
    with open(nome_arquivo, "r") as arquivo:
        ips = arquivo.readlines()
except FileNotFoundError:
    print("Erro: Arquivo não encontrado.")
    ips = []
except IOError:
    print("Erro ao ler o arquivo.")
    ips = []

ips_validos = []
ips_invalidos = []

for ip in ips:
    ip = ip.strip()
    partes = ip.split('.')
    
    if len(partes) == 4:
        valido = True
        for parte in partes:
            try:
                numero = int(parte)
                if numero < 0 or numero > 255:
                    valido = False
                    break
            except ValueError:
                valido = False
                break
        if valido:
            ips_validos.append(ip)
        else:
            ips_invalidos.append(ip)
    else:
        ips_invalidos.append(ip)

print("IPs válidos:")
for ip in ips_validos:
    print(ip)

print("\nIPs inválidos:")
for ip in ips_invalidos:
    print(ip)