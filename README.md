# 🔒 Inactivo-Tool

**Inactivo-Tool** es una multitool diseñada para pruebas de penetración, auditorías de seguridad y aprendizaje en ciberseguridad.  
Se ha creado con fines educativos y para uso **estrictamente legal** en entornos controlados.

⚠️ **Aviso**: El uso indebido de esta herramienta en sistemas sin autorización previa es ilegal.  
El autor no se hace responsable de cualquier daño o consecuencia derivada del uso incorrecto.

---

## ✨ Características
- Escaneo y análisis de redes.
- Detección de vulnerabilidades comunes.
- Herramientas de fuerza bruta controlada.
- Reconocimiento pasivo y activo.
- Funciones adaptadas para Kali Linux y Termux.

---

## 📦 Instalación en Kali Linux
1. **Actualizar paquetes**
```bash
sudo apt update && sudo apt upgrade -y
```
2. **Instalar dependencias**
```bash
sudo apt install git python3 python3-pip -y
```
3. **Clonar el repositorio**
```bash
git clone https://github.com/x4tt/Inactivo-Tool.git
```
4. **Entrar en la carpeta**
```bash
cd Inactivo-Tool
```
5. **Instalar requisitos**
```bash
pip3 install -r requirements.txt
```
6. **Ejecutar**
```bash
python3 inactivo.py
```

---

## 📱 Instalación en Termux (Android)
1. **Actualizar paquetes**
```bash
pkg update && pkg upgrade -y
```
2. **Instalar dependencias**
```bash
pkg install git python -y
```
3. **Clonar el repositorio**
```bash
git clone https://github.com/x4tt/Inactivo-Tool.git
```
4. **Entrar en la carpeta**
```bash
cd Inactivo-Tool
```
5. **Instalar requisitos**
```bash
pip install -r requirements.txt
```
6. **Ejecutar**
```bash
python inactivo.py
```

---

## 🛡 Licencia
Este proyecto está bajo la **Licencia MIT (Uso Ético)**.  
Puedes usar, modificar y distribuir el código con fines educativos y legales.  
Consulta el archivo [LICENSE](LICENSE) para más detalles.
