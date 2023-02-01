**Práctica II: problemas de optimización y ecuaciones no lineales.**

Antes de iniciar a trabajar: **Sólo una persona de cada equipo debe darle click a la liga de gh-classroom** que está indicada en la publicación de canvas. Una vez que le dé click a la liga de gh-classroom tal persona **invite** a sus integrantes de su equipo como **Admin**. Para invitar a su integrante ir dentro del repo de gh-classroom a Settings -> Manage Access y enviar la invitación ingresando user de github de su integrante.    
    

# Instrucciones

Resolver lo indicado en 

Entregar:

* Módulos de *Python*.

* *Notebook* de *Jupyter* en el que muestren los resultados de sus módulos y referencias utilizadas. Nombren a su reporte como: `reporte_equipo_<aquí colocar el número de su equipo>_practica_2.ipynb`.

**Fecha límite de entrega: 10 de diciembre 23:59**

# Dinámica

Dividir a su equipo para realizar tres tareas. **Ustedes deciden qué integrante resuelve qué tarea pero les sugiero que hagan una rotación respecto a la entrega anterior para que diferentes integrantes hagan distintas tareas**:

1. 2 personas que programen y resuelvan el ejercicio asignado (esto para un equipo de 3 o 4 personas, entonces en el equipo de 3 una persona tiene dos roles) .

2. 1 persona que programe un *test* que revise que se está resolviendo correctamente el ejercicio. Hagan la prueba para las aproximaciones **con dimensiones pequeñas**: matrices del orden de decenas (multiplicación entre renglones y columnas) y utilicen funciones de su lenguaje de programación para hacer la comparación. Debe usarse la funcionalidad de **de *Autograding* con *Actions* de Github para los *tests*. Utilicen `ubuntu:20.04` como ambiente para el testing.** No utilizar ambientes `macos` o `windows` únicamente `ubuntu`. Ver ejemplos en [example-github-actions](https://github.com/palmoreck/example-github-actions). **Si en su *testing* utilizan matrices medianas o grandes (del orden de centenas o mayores) se les restará puntos a la persona que programa el *test* y al equipo.**

3. 1 persona que coordine el reporte en un *notebook* de *jupyter* y sea *project manager* (más detalles de este rol en las notas).

Entre todos los y las integrantes tienen que dar *feedback* si es necesario en la resolución de las tareas que haya duda entre ustedes. El *feedback* consiste en resolver/explicar las dudas que existan. **Las personas asignadas a la tarea correspondiente son las que realizan los *commits* una vez resueltas las dudas**.

Los puntos 1, 2 y 3 anteriores los realizan de forma iterativa hasta finalizar las tareas y que estén en acuerdo las y los integrantes de cada equipo con las soluciones.

**Deben usar `git` o los botones de Github para llevar la historia de cambios en la realización de sus *notebooks* o cualquier otro archivo y subirlos a sus repos. No se revisarán aquellos archivos que tengan un commit con todas las respuestas. El trabajo es incremental.**

**Deben usar la funcionalidad de github**: *issues*, *milestones*, *projects*, *reviewers*, *asignees* o lo que ustedes consideren de github que les ayudará a comunicarse/organizarse (no tienen que usar todas las funcionalidades anteriores y cada equipo decide qué usar). Ver por [ejemplo video para crear proyectos en github](https://youtu.be/z4Xpif7HI04).

**Deben trabajar con instancias de AWS (utilicen las configuraciones que hicimos al inicio del curso, más información en las notas respecto a cómo comprobar que sí usaron la nube)**.


# Lenguajes de programación

Todos los equipos deben usar *Python*.

# Calificación

Se asgina una calificación individual por tarea asignada y una calificación por equipo. Se calificará de acuerdo a los *commits* realizados que realizan en su trabajo incremental.

# Notas

* Todas las personas integrantes del equipo contribuyen a la escritura del reporte (incluso si se es *project manager*). La calificación del reporte entra como parte de la calificación por equipo.

* Renombren este archivo `README.md` por `old_README.md` para que guarden su contenido y creen otro `README.md` donde escriban:

    * División de su equipo en una tabla que contenga en una columna *user* de github, en otra la(s) tarea(s) a realizar y en otra los roles asignados.
    * Referencias utilizadas.
