import subprocess
import time

# Iniciar el servidor Flask
subprocess.Popen(["python", "app.py"], shell=True)

# Esperar un poco para asegurarse de que Flask inicie primero
time.sleep(2)

# Iniciar Cloudflared para exponer el servidor local
subprocess.Popen(["cloudflared.exe", "tunnel", "--url", "http://localhost:5000"], shell=True)
