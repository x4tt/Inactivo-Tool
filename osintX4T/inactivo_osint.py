import os
import time
import requests
from termcolor import cprint
from colorama import init

init()

def banner():
    os.system("cls" if os.name == "nt" else "clear")
    cprint(r"""
██╗███╗   ██╗ █████╗  ██████╗████████╗██╗██╗   ██╗ ██████╗ 
██║████╗  ██║██╔══██╗██╔════╝╚══██╔══╝██║██║   ██║██╔═══██╗
██║██╔██╗ ██║███████║██║        ██║   ██║██║   ██║██║   ██║
██║██║╚██╗██║██╔══██║██║        ██║   ██║██║   ██║██║   ██║
██║██║ ╚████║██║  ██║╚██████╗   ██║   ██║╚██████╔╝╚██████╔╝
╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝   ╚═╝   ╚═╝ ╚═════╝  ╚═════╝ 
    """, "red")
    cprint("               [created by AMIN]               ", "green")
    print("\n")

def menu():
    cprint("[1] Buscar usuario en redes sociales", "cyan")
    cprint("[2] Verificar email en filtraciones (HaveIBeenPwned)", "cyan")
    cprint("[3] Whois de dominio", "cyan")
    cprint("[4] Geolocalización IP", "cyan")
    cprint("[5] Create DOX (Generar ficha PDF)", "cyan")
    cprint("[6] OSINT de Identidad (nombre, usuario, número)", "cyan")
    cprint("[7] Salir", "cyan")
    print()

def buscar_usuario(usuario):
    sitios = {
        "Instagram": f"https://www.instagram.com/{usuario}",
        "Twitter": f"https://www.twitter.com/{usuario}",
        "Facebook": f"https://www.facebook.com/{usuario}",
        "GitHub": f"https://github.com/{usuario}",
        "Reddit": f"https://www.reddit.com/user/{usuario}",
        "TikTok": f"https://www.tiktok.com/@{usuario}",
        "Pinterest": f"https://www.pinterest.com/{usuario}/",
        "YouTube": f"https://www.youtube.com/@{usuario}",
        "Discord": f"https://discord.com/users/{usuario}",  # requiere ID
        "Twitch": f"https://www.twitch.tv/{usuario}",
        "Steam": f"https://steamcommunity.com/id/{usuario}",
        "Medium": f"https://medium.com/@{usuario}",
        "VK": f"https://vk.com/{usuario}",
        "SoundCloud": f"https://soundcloud.com/{usuario}"
    }

    for nombre, url in sitios.items():
        try:
            r = requests.get(url, timeout=5)
            if r.status_code == 200:
                cprint(f"[+] {nombre}: Encontrado → {url}", "green")
            elif r.status_code == 404:
                cprint(f"[-] {nombre}: No encontrado", "red")
            else:
                cprint(f"[?] {nombre}: Estado HTTP {r.status_code}", "yellow")
        except requests.RequestException:
            cprint(f"[!] {nombre}: Error de conexión", "yellow")

def verificar_email(email):
    url = f"https://haveibeenpwned.com/unifiedsearch/{email}"
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        cprint("[!] Este email ha sido comprometido.", "red")
    elif r.status_code == 404:
        cprint("[+] Este email no aparece en filtraciones conocidas.", "green")
    else:
        cprint("[!] No se pudo verificar el email.", "yellow")

def whois_dominio(dominio):
    try:
        r = requests.get(f"https://api.hackertarget.com/whois/?q={dominio}")
        cprint(r.text, "yellow")
    except:
        cprint("[!] Error al obtener WHOIS.", "red")

def geolocalizar_ip(ip):
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}")
        data = r.json()
        for k, v in data.items():
            print(f"{k}: {v}")
    except:
        cprint("[!] Error geolocalizando IP", "red")

def sherlock_lite(usuario):
    plataformas = ["github.com", "reddit.com", "medium.com", "pastebin.com", "tiktok.com", "imgur.com"]
    for sitio in plataformas:
        url = f"https://{sitio}/{usuario}"
        try:
            r = requests.get(url)
            if r.status_code == 200:
                cprint(f"[+] Posible perfil: {url}", "green")
            else:
                cprint(f"[-] No encontrado: {url}", "red")
        except:
            cprint(f"[!] Error al verificar: {url}", "yellow")

def osint_identidad():
    while True:
        banner()
        cprint(">> MÓDULO OSINT DE IDENTIDAD", "yellow")
        print()
        cprint("[1] Buscar por nombre completo", "cyan")
        cprint("[2] Buscar por número de teléfono", "cyan")
        cprint("[3] Buscar por alias / username", "cyan")
        cprint("[4] Buscar por correo electrónico", "cyan")
        cprint("[5] Reconstrucción de perfil básico", "cyan")
        cprint("[6] Volver al menú principal", "cyan")
        print()

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            nombre = input("Ingresa el nombre completo: ")
            nombre_encoded = nombre.replace(" ", "+")
            dorks = [
                f"https://www.google.com/search?q=\"{nombre_encoded}\"+site:linkedin.com",
                f"https://www.google.com/search?q=\"{nombre_encoded}\"+site:facebook.com",
                f"https://www.google.com/search?q=\"{nombre_encoded}\"+site:twitter.com",
                f"https://www.google.com/search?q=\"{nombre_encoded}\"+site:instagram.com"
            ]
            for d in dorks:
                cprint(f"[DORK] {d}", "green")

        elif opcion == "2":
            numero = input("Ingresa el número (con código país): ")
            search_url = f"https://www.google.com/search?q=\"{numero}\""
            cprint(f"[+] Búsqueda inversa en Google:", "green")
            cprint(search_url, "yellow")

        elif opcion == "3":
            alias = input("Ingresa el alias / username: ")
            sitios = [
                f"https://www.google.com/search?q=\"{alias}\"+site:pastebin.com",
                f"https://www.google.com/search?q=\"{alias}\"+site:reddit.com",
                f"https://www.google.com/search?q=\"{alias}\"+site:github.com",
                f"https://www.google.com/search?q=\"{alias}\"+site:twitter.com",
                f"https://www.google.com/search?q=\"{alias}\"+site:instagram.com"
            ]
            for url in sitios:
                cprint(f"[Alias Search] {url}", "green")

        elif opcion == "4":
            email = input("Ingresa el email: ")
            email_google = f"https://www.google.com/search?q=\"{email}\""
            gravatar_hash = __import__("hashlib").md5(email.strip().lower().encode()).hexdigest()
            gravatar_url = f"https://www.gravatar.com/avatar/{gravatar_hash}"
            cprint(f"[+] Búsqueda en Google: {email_google}", "green")
            cprint(f"[+] Posible imagen Gravatar: {gravatar_url}", "yellow")

        elif opcion == "5":
            user = input("Alias a investigar: ")
            cprint(f"[RECON] Generando perfil para: {user}", "yellow")
            urls = [
                f"https://www.instagram.com/{user}",
                f"https://www.twitter.com/{user}",
                f"https://www.facebook.com/{user}",
                f"https://github.com/{user}",
                f"https://www.reddit.com/user/{user}",
                f"https://www.tiktok.com/@{user}",
                f"https://www.pinterest.com/{user}/",
                f"https://www.youtube.com/@{user}",
                f"https://www.twitch.tv/{user}",
                f"https://steamcommunity.com/id/{user}",
                f"https://soundcloud.com/{user}"
            ]
            for url in urls:
                try:
                    r = requests.get(url, timeout=5)
                    if r.status_code == 200:
                        cprint(f"[+] Activo: {url}", "green")
                    else:
                        cprint(f"[-] Inactivo: {url}", "red")
                except:
                    cprint(f"[!] Error accediendo a {url}", "yellow")

        elif opcion == "6":
            break
        else:
            cprint("Opción inválida", "red")
        
        input("\nPresiona Enter para continuar...")

def create_dox():
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib.pagesizes import A4

    cprint("[CREATE DOX] Completa la información para el reporte", "cyan")
    nombre = input("Nombre completo: ")
    alias = input("Alias / Usuario: ")
    ip = input("IP: ")
    coordenadas = input("Coordenadas (lat, long): ")
    direccion = input("Dirección: ")
    ciudad = input("Ciudad: ")
    telefono = input("Número de teléfono: ")
    correo = input("Correo electrónico: ")
    notas = input("Notas adicionales (opcional): ")

    filename = f"dox_{alias or nombre.replace(' ', '_')}.pdf"
    doc = SimpleDocTemplate(filename, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("INACTIVO OSINT - Ficha DOX", styles['Title']))
    story.append(Spacer(1, 12))

    info = {
        "Nombre": nombre,
        "Alias / Usuario": alias,
        "IP": ip,
        "Coordenadas": coordenadas,
        "Dirección": direccion,
        "Ciudad": ciudad,
        "Teléfono": telefono,
        "Correo": correo,
        "Notas": notas
    }

    for label, value in info.items():
        story.append(Paragraph(f"<b>{label}:</b> {value}", styles['Normal']))
        story.append(Spacer(1, 8))

    doc.build(story)
    cprint(f"[+] PDF creado exitosamente: {filename}", "green")
    input("Presiona Enter para continuar...")

def main():
    while True:
        banner()
        menu()
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            user = input("Ingresa el nombre de usuario: ")
            buscar_usuario(user)
        elif opcion == "2":
            email = input("Ingresa el email: ")
            verificar_email(email)
        elif opcion == "3":
            dominio = input("Ingresa el dominio (ej: google.com): ")
            whois_dominio(dominio)
        elif opcion == "4":
            ip = input("Ingresa la IP: ")
            geolocalizar_ip(ip)
        elif opcion == "5":
            create_dox()
        elif opcion == "6":
            osint_identidad()
        elif opcion == "7":
            cprint("Saliendo de INACTIVO OSINT...", "red")
            break
        else:
            cprint("Opción inválida", "red")

        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()
