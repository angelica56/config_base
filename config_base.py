config_base = {
    "host": "localhost",
    "port": 3306,
    "debug": False
}

config_desarrollo = {
    "debug": True,
    "log_level": "verbose"
}

config_produccion = {
    "host": "192.168.1.10",
    "log_level": "error"
}

# 1️⃣ Configuración final desarrollo
config_final_dev = {**config_base, **config_desarrollo}

print("Configuración desarrollo:")
print(config_final_dev)


# 2️⃣ Configuración final producción
config_final_prod = {**config_base, **config_produccion}

print(f"Configuración producción:")
print(config_final_prod)


# 3️⃣ Función conectar normal
def conectar(host, port, debug, log_level="info"):
    print(f"Conectando con parámetros:")
    print("Host:", host)
    print("Port:", port)
    print("Debug:", debug)
    print("Log level:", log_level)

# Llamada usando unpacking
conectar(**config_final_dev)


# 4️⃣ Función con kwargs
def conectar_flexible(**kwargs):
    print(f"Conexión flexible:")
    for clave, valor in kwargs.items():
        print(clave, ":", valor)

# Llamada usando unpacking
conectar_flexible(**config_final_prod)
