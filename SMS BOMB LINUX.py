import os
import sys
import subprocess

BASE_DIR = os.getcwd()
TBOMB_DIR = os.path.join(BASE_DIR, "TBomb")
IMPULSE_DIR = os.path.join(BASE_DIR, "Impulse")

def run_cmd(cmd, cwd=None):
    print(f"Ejecutando comando: {cmd} en {cwd}")
    proc = subprocess.Popen(cmd, shell=True, cwd=cwd)
    proc.communicate()
    return proc.returncode

def clone_or_pull(repo_url, path):
    if os.path.isdir(path):
        print(f"Actualizando repo en {path}...")
        ret = run_cmd("git pull", cwd=path)
        if ret != 0:
            print("Error al actualizar repo.")
    else:
        print(f"Clonando repo {repo_url} en {path}...")
        ret = run_cmd(f'git clone "{repo_url}" "{path}"')
        if ret != 0:
            print("Error al clonar repo.")

def install_tbomb():
    clone_or_pull("https://github.com/TheSpeedX/TBomb.git", TBOMB_DIR)
    print("Instalando TBomb...")
    ret = run_cmd("bash install.sh", cwd=TBOMB_DIR)
    if ret != 0:
        print("Error al ejecutar install.sh")

def install_impulse():
    clone_or_pull("https://github.com/LimerBoy/Impulse.git", IMPULSE_DIR)
    print("Instalando dependencias de Impulse...")
    ret = run_cmd("pip3 install -r requirements.txt", cwd=IMPULSE_DIR)
    if ret != 0:
        print("Error al instalar dependencias")

def run_tbomb():
    print("Ejecutando TBomb...")
    run_cmd("python3 bomber.py", cwd=TBOMB_DIR)

def run_impulse():
    print("Ejecutando Impulse...")
    run_cmd("python3 impulse.py --help", cwd=IMPULSE_DIR)

def menu():
    while True:
        os.system("clear")
        print("""
███████╗███████╗████████╗███████╗███╗   ███╗███████╗
██╔════╝██╔════╝╚══██╔══╝██╔════╝████╗ ████║██╔════╝
███████╗█████╗     ██║   ███████╗██╔████╔██║███████╗
╚════██║██╔══╝     ██║   ╚════██║██║╚██╔╝██║╚════██║
███████║███████╗   ██║   ███████║██║ ╚═╝ ██║███████║
╚══════╝╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝╚══════╝
""")
        print("Seleccione una opción:\n1) Ejecutar TBomb (Spam SMS)\n2) Ejecutar Impulse (Spam SMS)\n0) Salir")
        choice = input("Opción: ").strip()
        if choice == "1":
            install_tbomb()
            run_tbomb()
            input("\nPresiona ENTER para continuar...")
        elif choice == "2":
            install_impulse()
            run_impulse()
            input("\nPresiona ENTER para continuar...")
        elif choice == "0":
            print("Saliendo...")
            sys.exit(0)
        else:
            print("Opción incorrecta.")
            input("Presiona ENTER para intentar de nuevo...")

if __name__ == "__main__":
    menu()