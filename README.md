Para poder ejecutar este programa necesitaremos la ayuda de la libreria nmap, la instalaremos usando el siguente comando:
pip install python-nmap

Una vez que ya tenemos la dependencia instalada y el archivo del programa en nuestra computadora procederemos a ejecutarlo y para eso usaremos el siguente comando:
python3 scrypt_nmap.py

Una vez que el programa se haya iniciado aparecera el siguente mensaje:
Ingrese los hosts (por ejemplo, 192.168.1.1 o 192.168.1.1-254): <IP Host>
Donde en <IP Host> pondremos las IP de los host a escanear 

Cuando presionemos enter nos saldra el sieguente mensaje:
Ingrese los puertos (por ejemplo, 22,80 o 1-1024): <Port>
Donde <Port> puede ser cualquier puerto o un rango de puertos a escanear

Y por ultimo nos pedira lo siguente:
Ingrese los argumentos adicionales (por ejemplo, -sS -O): <Arguments>
Donde <Arguments> debera ser el argumento a o el comando de nmap que queramos ejecutar 
