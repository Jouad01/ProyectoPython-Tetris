# ProyectoPython-Tetris

## Índice
1. [Definición](#definición)
1. [Objetivos del proyecto](#objetivos-del-proyecto)
1. [Requisitos](#requisitos)
1. [Planificación](#planificación)
1. [Creación del documento IDC](#creación-del-documento-idc)
1. [¿Cómo funciona el juego?](#¿cómo-funciona-el-juego?)
1. [Interacción del jugador con el juego](#interacción-del-jugador-con-el-juego)

## Introducción
El tetris es un juego de piezas o elementos diferentes que deben encajar entre si.

El objetivo es hacer caer piezas e ir rellenando huecos para conseguir hacer líneas. Una vez creadas, desaparecen, y nos interesa hacerlo de cuatro en cuatro en vez de una en una por los puntos que hay implicados en ello. Si consigues una de cuatro, felicidades, acabas de hacer un Tetris.

1. Descargar el repositorio de GitHub.
2. Abrir el archivo `Tetris.py` con el editor de texto de tu preferencia.
3. Descargar el pygame de la página oficial.
4. Ejecutar el archivo `Tetris.py` con el intérprete de Python.
5. Poner nombre al jugador.
6. Se abrirá una ventana con el tablero de juego.
7. Clicar cualquier tecla para empezar a jugar.
8. Se creará una pieza aleatoria. Podremos moverla con las flechas del teclado ⬅️ ⬆️ ⬇️ ➡️.
9. A jugar!

## Objetivos del proyecto

- Trabajo en equipo.    
- Aplicar los conocimientos adquiridos en clase en un proyecto real.
- Aprender a trabajar con un repositorio remoto y local en equipo.

## Requisitos 
- Incrementar un sistema workflow en git.
- Documentar el manual técnico de la aplicación.

## Planificación
Antes de iniciar el proyecto hemos realizado una planificación y lo hemos dividido en 4 fases:
- IDC, Investigación y desarrollo conceptual.
- TEP, Traslado a entorno de programa.
- CCF, Codificación y creación de funciones.
- PCE, Pruebas y corrección de errores.

## Posibles tecnologías
| Tecnologías | _workflow_ | BBDD |
|-| - | - | 
| MongoDB |  - | ✅ |
| GitHub | ✅ | - |


## Diagrama de componentes
![](img/Diagramas_Componentes.png)

Este proyecto se compone de un archivo principal llamado `tetris`. En este se accede a multiples funciones que son llamadas a cada una de ellas(`board`, `game` y `cristals`).

El archivo `board` contiene las constantes del juego, como las piezas, el tamaño del tablero, cómo caen las piezas y el color de las piezas. 

El archivo `game` contiene las funciones del juego, como dibujar el tablero, dibujar las piezas, la puntuación, cómo selecciona la pieza de forma aleatoria, guarda la máxima puntuación del jugador, etc.

El audio del juego se encuentra en el archivo `cristals`.

`Record` es el archivo donde se guarda la máxima puntuación del jugador.


## Creación del documento IDC
### Instroducción
El tetris es un juego de piezas o elementos diferentes que deben encajar entre si.

El objetivo es hacer caer piezas e ir rellenando huecos para conseguir hacer líneas. Una vez creadas, desaparecen, y nos interesa hacerlo de cuatro en cuatro en vez de una en una por los puntos que hay implicados en ello. Si consigues una de cuatro, felicidades, acabas de hacer un Tetris.

1. Descargar el repositorio de GitHub.
2. Abrir el archivo `Tetris.py` con el editor de texto de tu preferencia.
3. Descargar el pygame de la página oficial.
4. Ejecutar el archivo `Tetris.py` con el intérprete de Python.
5. Poner nombre al jugador.
6. Se abrirá una ventana con el tablero de juego.
7. Clicar cualquier tecla para empezar a jugar.
8. Se creará una pieza aleatoria. Podremos moverla con las flechas del teclado ⬅️ ⬆️ ⬇️ ➡️.
9. A jugar!


## Creación del documento TEP

Preparación
1. Descargar el pygame de la página oficial.
2. Crear un archivo `Tetris.py` con el editor de texto de tu preferencia, ese será el archivo principal del juego (el main).
3. Crear un archivo `board.py` ese será el archivo donde guardaremos las constantes del juego, en este caso las piezas del jugo, como caen .
4. Crear un archivo `game.py` ese será el archivo donde guardaremos las funciones del juego, tales como el tablero, las piezas, la puntuación,  etc.
5. Crear un archivo `record.txt` ese será el archivo donde se guarda la mejor puntuación del juego.
6. Crear un archivo `README.md` ese será el archivo donde se guardará la documentación del proyecto.

### ¿Cómo jugar?
1. Irán bajando por el tablero las piezas de forma aleatoria con una función llama `random`.
2. El jugador podrá mover las piezas con las flechas del teclado ⬅️ ⬆️ ⬇️ ➡️.
    - El jugador podrá mover las piezas a la derecha con la tecla ➡️ .
    - El jugador podrá mover las piezas a la izquierda con la tecla ⬅️  .
    - El jugador podrá rotar las piezas con la tecla  ⬆️ .
    - El jugador podrá bajar las piezas con la tecla  ⬇️ .

### Interacción del jugador con el juego

1. Se mostrará por termnal el nombre del juego.
2. Se mostrará por terminal el que el usuario debe introducir su nombre.
3. Se abrirá una ventana y el jugador clicará cualquier tecla para empezar a jugar.
4. Iniciará el juego.
5. Durante todo el juego se mostrará en pantalla la pieza del siguiente turno. 
5. Cada vez que 'caiga' una pieza comprobara si hay una línea completa.
    - Si hay una línea completa, se sumará 10 puntos a la puntuación.
    - Si no, seguirá bajando las piezas.
6. Cuando las piezas lleguen arriba(de forma vertical) el juego acaba y sale en pantalla 'GAME OVER'

### Cosas a tener en cuenta 
Si el usuario sale antes de que salga el 'GAME OVER' no se guarda la puntuación



### ¿como se genera las piezas?
### ¿Cómo sabe como hace linea?
Hay una función que se llama `clean_row` que comprueba si hay una línea completa, si la hay, se elimina o sea si no hay ninguna pieza en negro(color del tablero) sabe que se ha hecho una linea. 

Algoritmo de la función `clean_row`:

1. Se le pasa un diccionario  que almacena las piezas y una lista de listas que representa el tablero.
1. Inicializar un contador  para las filas completas.
1. Recorrer el tablero.
    1. Si no hay ningún bloque vacio en la fila aumentará el contador de filas completas.
    1.  Guardar el índice de la fila completa.
    1. Eliminar la posicion de la fila completa del diccionario de posiciones bloqueadas
1. Si el contador es mayor a 0.
    1. Recorrer las posiciones bloqueadas y ordenadas por coordenadas 
        1. Si hay alguna fila que se encuentre por encima de la fila completa
            1. Mover la posición bloqueada en el número de filas completas hacia abajo.

![](/docs/img/eliminar_filas.png)
###### `clean_row`



### ¿Cuando acaba el juego?
Se acaba la partida cuando se llena el tablero de alto con las piezas  o cuando de clica en la barra espaciadora. 





### Esquema BBDD

El esquema de la base de datos esta organizada en dos colecciones, una para los jugadores y otra para los records.

###### Validación esquema

```js 
{
    $jsonSchema: {
        bsonType: 'object',
        required: [
            'nombre',
            'puntuacion',
        ],
        properties: {
            nombre: {
                bsonType: 'string',
                description: 'nombre del jugador'
            },
            puntuacion: {
                bsonType: 'int',
                description: 'puntuacion del jugador'
            },
        }
    }
}
```
![](/docs/img/DDBB.jpeg)



## Creación del documento CCF
crear un borrador 

1. board (pantalla como caen las piezas)
2. game randon pygame importar todo del 
3. tetris import * incluido el pymongo y el pygame
como se juega con las teclas está en el main
4. cración y conexxion a la base de datos


usar clase engargada de crear las piezas





### Comparar resultados
comparar la base de datos y guarda en el txt el la puntuación máxima  y la puntuacion
## Creación del documento PCE
(Errores en las pruebas unitarias e integradas)

Fallo:
error


