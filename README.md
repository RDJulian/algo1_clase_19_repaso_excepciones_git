# Clase 19: Repaso, Excepciones y Git (introducción)

## Repaso:

Algoritmos de ordenamiento:

1. BubbleSort (optimizado)
2. InsertionSort
3. SelectionSort

Complejidad: O(N^2)

## Recursividad:

Ejercicio:<br>

Programar una funcion potencia que tenga como parametro una base y un exponente enteros, y devuelva el resultado.
NO SE PUEDE resolver con iteraciones. Debe ser una funcion recursiva.

Claves:

1. Encontrar casos base
2. Resolver el problema inicial con una instancia más pequeña del mismo problema. En nuestro caso, dividir el exponente
   en dos.
3. Verificar todos los casos para no entrar en bucles infinitos.

## Excepciones:

Claves:

1. raise para levantar una excepcion (de Python o una personalizada).
2. try para declarar un bloque de codigo a ejecutar, el cual puede lanzar una excepcion.
3. except **excepcion** para declarar qué excepcion esperar, y que líneas ejecutar en caso de atraparla.
4. finally para declarar líneas que se ejecutaran **siempre**, aun si no se atrapó ninguna excepcion.

## Git:

Lo basico:
<ol>
<li>Instalar Git: https://git-scm.com/downloads</li>
<li>Crear una cuenta de GitHub.</li>
<li>Cargar las credenciales con:<br>

> git config --global user.name "NOMBRE_USUARIO"<br>
> git config --global user.email mail@fi.uba.ar
</li>
<li>Clonar o crear un repositorio con:

> git clone ENLACE_REPOSITORIO.git

o
> git init
</li>
<li>git add . o ARCHIVO</li>
<li>git commit -m "MENSAJE"</li>
<li>git pull</li>
<li>Resolver conflictos de ser necesario.</li>
<li>git push</li>
<li>Si se pushea codigo por primera vez, la terminal va a pedir credenciales. Generar un token en Settings > 
Developer Settings > Token e ingresarlo cuando pida contraseña.</li>
</ol>