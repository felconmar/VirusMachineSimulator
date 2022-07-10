VirusMachineSimulator
---------------------
## [Computing with viruses](https://www.sciencedirect.com/science/article/pii/S0304397515011457)
---------------------
## Instrucciones para la ejecución desde el entorno de desarrollo

Para la ejecución seguir los siguientes pasos:
1. Copiar la template que más se parezca al problema que queremos cargar a la raíz del directorio "src".
2. Cambiar los objetos que nos interese para adaptarlos al problema.
3. Ejecutar la template modificada.

## Guía de los objetos

* Hosts: tienen un id y un peso.

     `h1 = Host("h1", 5)`


* Instrucciones: tienen un id, primer host, condición, segundo host y canales que se abren cuando la instrucción se cumple.

    `i1 = Instruction("i1", "h1", "bigger than", "h2", ["ch1"])`

    Las condiciones soportadas actualmente son las siguientes:

    - Not empty
    - Empty
    - Bigger than
    - Smaller than
    - Equals
    - Not equals


* Canales: tienen un id, el id del host origen y el id del host destino y un peso. 

    `ch1 = Channel("ch1", "h1", "h0", 1)`

