import sys
import re

DANGEROUS_PATTERNS = [
    (r"rm\s+-rf\s+/", "Eliminación recursiva de la raíz del sistema"),
    (r"dd\s+if=/dev/zero\s+of=/dev/sd[a-z]", "Sobrescritura de disco"),
    (r"mkfs\s+", "Formateo de sistema de archivos"),
    (r":\(\)\{:\|:&\};:", "Bomba fork"),
    (r"chmod\s+777\s+/", "Permisos inseguros en la raíz"),
    (r"curl\s+.*\|\s*bash", "Ejecución de script remoto"),
    (r"wget\s+.*\|\s*bash", "Ejecución de script remoto"),
    (r"python\s+-c\s+['\""]import\s+os;.*system", "Inyección de código en Python"),
]

def is_dangerous(command):
    for pattern, description in DANGEROUS_PATTERNS:
        if re.search(pattern, command):
            return True, description
    return False, None

def main():
    if len(sys.argv) < 2:
        print("Uso: python block_destructive_commands.py '<comando>'")
        sys.exit(1)

    command = sys.argv[1]
    dangerous, description = is_dangerous(command)

    if dangerous:
        print(f"Comando bloqueado: {description}")
        print(f"Comando: {command}")
        sys.exit(1)
    else:
        print("Comando permitido.")
        sys.exit(0)

if __name__ == "__main__":
    main()
