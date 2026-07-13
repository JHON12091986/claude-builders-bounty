\# Pre-tool-use Hook para Claude Code



Este hook previene la ejecución de comandos peligrosos en Claude Code.



\## Instalación



1\. Coloca los archivos en `\~/.claude/hooks/`.

2\. Dale permisos de ejecución: `chmod +x \~/.claude/hooks/claude\_hook.sh`.



\## Uso



El hook se ejecuta automáticamente antes de cada comando.



\## Comandos bloqueados



\- `rm -rf /`

\- `dd if=/dev/zero of=/dev/sdX`

\- `mkfs`

\- Fork bombs

\- `chmod 777 /`

\- `curl ... | bash`

\- `wget ... | bash`

\- `python -c "import os; os.system(...)"`

