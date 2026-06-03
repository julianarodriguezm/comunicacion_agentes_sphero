# Comunicación entre agentes con Spheros
Repositorio para código fuente de programa de comunicación entre agentes con spheros.

## Configuración del entorno
Ejecutar:

	python3 -m pip install --upgrade pip
		
	python3 -m pip install spherov2

## Tomar en cuenta
Para conectarse a un robot específico, podemos reemplazar esta parte del código

	toy = scanner.find_toy()

Por esta:

	toy = scanner.find_toy(toy_name="SB-1234")

Reemplazando el código de toy_name por el deseado.
