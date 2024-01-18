# Un entorno virtual es la posibilidad de crear, dentro del sistema operativo,
# un mini servidor para que yo pueda instalar todo lo que yo necesite, como 
# alguna versión específica de Python o librerías, sin afectar al sistema  
# operativo completo.

# Los entornos virtuales son necesarios si en un mismo sistema operativo tienes 
# cargados distintos proyectos y sobre todo se recomienda a quienes van comenzando
# el desarrollo python 

# El código siguiente se deberá ejecutar directamente en la terminal y en la carpeta 
# donde vallamos a tener el proyecto a desarrollar

# Después de instalar virtualenv:

pip3 install virtualenv
sudo apt install python3-virtualenv

# con los comandos correspondientes podemos crear un entorno virtual:

virtualenv mi_primer_entorno

source mi_primer_entorno/bin/activate

# Automáticamente se colocará el nombre de tu entorno antes del propmt en tu terminal,
# lo cual significa que te encuentras dentro del entorno virtual y puedes desarrollar 
# dentro de éste sin afectar al sistema operativo completo con las instalaciones que 
# realices.

# Para salir del entorno virtual 

deactivate

# De esa manera ya no verás el nombre del entorno antes del prompt


# Ojo que si la carpeta que contiene el proyecto que usa entorno virtual tiene .git y 
# lo estás versionando a github, verifica siempre que la carpeta del entorno contenga 
# un archivo gitignore que ignore a todos los archivos en la carpeta






