#!/bin/bash
COMMAND="\"

python3 block_destructive_commands.py "\"
EXIT_CODE=\True

if [ \ -eq 1 ]; then
    echo "Comando bloqueado por política de seguridad."
    exit 1
else
    echo "Comando aprobado."
    exit 0
fi
