# Comunicación entre agentes con Spheros
Repositorio para código fuente de programa de comunicación entre agentes con spheros utilizando JavaScript.

## Configuración del entorno
En Sphero Edu se pueden crear programas diferentes, uno para el beacon, otro para el explorador y otro para el seguidor o seguidores. Luego, se pueden copiar y pegar los códigos correspondientes en cada programa., estos se encuentran en los archivos `beacon.js`, `explorador.js` y `seguidor.js` respectivamente.

## Ejecución del programa
Se pueden iniciar todos los programas en la aplicación Sphero Edu, asegurándose de que todos los Spheros estén conectados y listos para comunicarse. El programa beacon enviará señales débiles que solo deben ser encontradas por el explorador cuando esté cercano al sphero beacon. Una vez el explorador encuentre el beacon, comenzará a hacer broadcast a los seguidores, quienes a su vez comenzarán a hacer broadcast a los demás seguidores, creando así una red de comunicación entre los Spheros. De esta manera, todos los spheros deben terminar en la misma zona.

## Creación de programa
Para crear un programa en Sphero Edu, sigue estos pasos:
1. Abre la aplicación Sphero Edu en tu dispositivo.
2. Conecta tu Sphero a la aplicación.
3. Ve a la sección de programación y selecciona "Crear nuevo programa".
4. Elige el tipo de programa y sphero ("JavaScript" y "Sphero Bolt" respectivamente).
5. Copia y pega el código correspondiente al programa beacon, explorador o seguidor en el editor de código.
6. Guarda el programa y ejecútalo para ver cómo los Spheros se comunican entre sí.