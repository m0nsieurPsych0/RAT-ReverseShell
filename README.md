```


 ██▒   █▓▓█████  ██▀███            ██▓    ███▄    █      █████▒    ▒█████      ██▀███      ███▄ ▄███▓    ▄▄▄         ▄▄▄█████▓    ██▓     █████      █    ██    ▓█████ 
▓██░   █▒▓█   ▀ ▓██ ▒ ██▒         ▓██▒    ██ ▀█   █    ▓██   ▒    ▒██▒  ██▒   ▓██ ▒ ██▒   ▓██▒▀█▀ ██▒   ▒████▄       ▓  ██▒ ▓▒   ▓██▒   ▒██▓  ██▒    ██  ▓██▒   ▓█   ▀ 
 ▓██  █▒░▒███   ▓██ ░▄█ ▒         ▒██▒   ▓██  ▀█ ██▒   ▒████ ░    ▒██░  ██▒   ▓██ ░▄█ ▒   ▓██    ▓██░   ▒██  ▀█▄     ▒ ▓██░ ▒░   ▒██▒   ▒██▒  ██░   ▓██  ▒██░   ▒███   
  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄           ░██░   ▓██▒  ▐▌██▒   ░▓█▒  ░    ▒██   ██░   ▒██▀▀█▄     ▒██    ▒██    ░██▄▄▄▄██    ░ ▓██▓ ░    ░██░   ░██  █▀ ░   ▓▓█  ░██░   ▒▓█  ▄ 
   ▒▀█░  ░▒████▒░██▓ ▒██▒         ░██░   ▒██░   ▓██░   ░▒█░       ░ ████▓▒░   ░██▓ ▒██▒   ▒██▒   ░██▒    ▓█   ▓██▒     ▒██▒ ░    ░██░   ░▒███▒█▄    ▒▒█████▓    ░▒████▒
   ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░         ░▓     ░ ▒░   ▒ ▒     ▒ ░       ░ ▒░▒░▒░    ░ ▒▓ ░▒▓░   ░ ▒░   ░  ░    ▒▒   ▓▒█░     ▒ ░░      ░▓     ░░ ▒▒░ ▒    ░▒▓▒ ▒ ▒    ░░ ▒░ ░
   ░ ░░   ░ ░  ░  ░▒ ░ ▒░          ▒ ░   ░ ░░   ░ ▒░    ░           ░ ▒ ▒░      ░▒ ░ ▒░   ░  ░      ░     ▒   ▒▒ ░       ░        ▒ ░    ░ ▒░  ░    ░░▒░ ░ ░     ░ ░  ░
     ░░     ░     ░░   ░           ▒ ░      ░   ░ ░     ░ ░       ░ ░ ░ ▒       ░░   ░    ░      ░        ░   ▒        ░          ▒ ░      ░   ░     ░░░ ░ ░       ░   
      ░     ░  ░   ░               ░              ░                   ░ ░        ░               ░            ░  ░                ░         ░          ░           ░  ░
     ░                                                                                                                                                                 
```



# Installation
Ce projet ne necessite aucune librairie Python externe.
Donc qu'une installation de base de python est nécessaire.

Installation en une commande powershell:

    [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12 ; Invoke-WebRequest -Uri "https://www.python.org/ftp/python/3.9.5/python-3.9.5-amd64-webinstall.exe" -OutFile "$($Env:TEMP)/python-3.9.5-amd64-webinstall.exe" ; Start-Process -NoNewWindow -Filepath "$($Env:TEMP)/python-3.9.5-amd64-webinstall.exe" -ArgumentList "/quiet InstallAllUsers=0 PrependPath=1 Include_test=0"


# Utilisation
Il y a deux modules principaux à ce projet:

### 1- Serveur: Dans le dossier CommandNcontrol
On démarre le server en entrant:
    
    python.exe .\main.py -s

on peut sortir des information de la base de donnée en entrant:

    python.exe .\main.py -d

on peut demander de l'aide sur les commandes en entrant:

    python.exe .\main.py --help

### 2- Client: Dans le dossier reproduction
On démarre le client en entrant:

    python.exe .\client.py
