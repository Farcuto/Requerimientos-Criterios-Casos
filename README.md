# Requerimientos-Criterios-Casos

~~~
Requerimintos para correr el archivo  de pruebas(test_converted.py):

pip install  pytest
~~~

## 1.  ¿Qué es un Coding Dojo?

De acuerdo al conocimiento obtenido después de consultar algunas fuentes, Coding Dojo, básicamente es una actividad que realiza un grupo de personas con el propósito de resolver un reto, por igual, en una sesión de coding dojo puede existir un público que puede estar como simples espectadores aprendiendo nuevas técnicas de programación y/o tecnologías, sin embargo, en otros casos ese público puede tener participación en la resolución del problema planteado en la sección.

Algo característico que se pudo observar es que el coding dojo tiene un enfoque no competitivo y el mismo es colaborativo. El coding dojo tiene dos modalidades que pude investigar las cuales son “Codekata” en la cual un participante muestra la solución del desafío y “Randori” en la cual se soluciona el reto en parejas.
## 2. Diferencia entre Requerimientos, Criterios de Aceptación y Escenarios de Prueba. Dar ejemplos a partir de un problema distinto a la referencia. Referencia https://lorenzosolano.com/requirements-acceptance-criteria-and/

Bien de acuerdo a lo investigado para explicar la diferencia entre criterios de aceptación, requerimientos y escenarios de prueba primero tendríamos que definirlos.

## Requerimientos: 

Los requerimientos son cada una de las características que debe tener el software desarrollado, existen dos tipos de requerimientos, funcionales y no funcionales. En el caso de los funcionales tenemos cada una de las acciones que debería poder realizar el software desarrollado como en el caso de la calculadora sería sumar, restar, multiplicar y dividir, en el caso de los requerimientos no funcionales se pueden definir como las las propiedades del sistema como usabilidad, eficiencia, entre otros.

## Criterios de aceptación: 
Los criterios de aceptación se pueden definir como una lista de requisitos solicitados por el cliente en el cual se especifican los requerimientos tanto funcionales como no funcionales.

## Escenarios de prueba: Los 
escenarios de prueba son situaciones que se plantean para ver que el programa desarrollado está funcionando de la manera en la que debería un ejemplo seria que se introduzca 2+1 o 1+2 y en ambos casos la respuesta debería ser la misma.

## Entonces estableciendo la diferencia entre requerimientos, criterios de aceptación y escenarios. Es que los requerimientos son cada una de las funcionalidades que debe tener el software desarrollado, en el caso de criterios de aceptación existe un conjunto de requerimientos realizados por el cliente en el cual estos no pueden ser ambiguos o estar libres a la interpretación y los escenarios nos sirven para tener unos datos de entrada y los datos de salida deberían ser los esperados.

## 3. De dos ejemplos de requerimientos no-funcionales, y especifique cuál es su categoría (seguridad, performance, portabilidad, etc.)

En el caso de una calculadora dos ejemplos serían:
La interfaz de usuario o GUI debe ser intuitiva o amigable.(usabilidad)
El tiempo de respuesta al momento de hacer una operacion aritmetica debe ser 0.5 segundos o menor.(performance)

# 4. ¿Qué es TDD?
TDD o Test Driven Development, es una manera de desarrollar código en el que primero se realizan las pruebas unitarias antes de escribir el código, el fin de esto es escribir un código más limpio y logran una reducción de los errores. Al momento de escribir código usando esta metodología se asegura de que el código pase las pruebas unitarias y el desarrollo llegue a su etapa final más rápido ya que si se desarrolla de manera tradicional y luego se realizan las pruebas unitarias y el código no cumple de manera satisfactoria se debe reescribir código causando una pérdida de tiempo y aparición de posibles errores.

## 5. ¿Qué son pruebas unitarias automatizadas?
Las pruebas unitarias automatizadas según lo leído estas son utilizadas con el fin de confirmar que el código nuevo en un proyecto no afectan la integridad del mismo y que cada función tiene la salida esperada respecto a la entrada, de este modo se puede mantener una integración continua en los proyectos y por lo tanto una entrega continua con el fin de entregar versiones más recientes a los clientes en el menor tiempo posible.

## 6. ¿Cuál fue el 1er framework de pruebas unitarias y para cual lenguaje fue creado?
El primer framework fue Junit creado en 1997 por Kent Beck y Eric Gamma, y Junit fue creado para ser utilizado en el lenguaje de programacion Java

## 7. ¿Describa los componentes de la arquitectura xUnit?

## 8. Indique al menos tres desventajas de las pruebas unitarias automatizadas
Gran esfuerzo en el mantenimiento
Falsa percepcion de calidad
No siempre son fiables

## 9. Indique al menos tres ventajas de las pruebas unitarias automatizadas.
Evita que se cree un bucle de revisión y desarrollo entre el departamento de QA y Desarrollo
Confirman los resultados esperados de forma mucho más rápida.
Retroalimentación mucho más rapida.

## 10. Tomando el algoritmo de conversión de números arábigos o "decimales" a números Romanos:
  * Cree un documento donde se listen los Requerimientos, Criterios de Aceptación y Casos de Prueba para una aplicación de consola
  * Los casos de prueba deben ser de dos categorías: End-To-End (desde el UI) y Unitarios (caja blanca, código, bajo nivel)

## HU-001:
Como usuario de la aplicación quiero poder ingresar números enteros positivos y que la aplicación los convierta a números romanos. 

## Requerimientos:
Que el usuario pueda ingresar números enteros positivos entre 1 y 3999.
Que la aplicación valide que los valores ingresados sean números enteros positivos.

## Criterios de aceptación: 
Al momento del usuario realizar una entrada se debe validar que dicha entrada son números enteros positivos.

## Casos de prueba:

## Caja blanca:
  Realizar pruebas de funcionalidad en la cual se verifiquen cuáles valores son válidos en números romanos y que valores son inválidos.
Manejo de errores.

## Código:
Probar la función realizando distintas entradas tanto válidas como inválidas.


## HU-002:
Como usuario quiero que al momento de ingresar un valor la aplicación convierte los números decimales o arábigos en números romanos con el formato apropiado.

## Requerimientos: 
En el momento en el que el usuario ingrese un decimal este debe ser convertido en números romanos utilizando las reglas estándar( III ).

## Casos de prueba: 

## Caja blanca:
Ver que la conversión de decimales claves (1, 5, 10, 50, 100, 500 ,1000) se realice de manera apropiada.
Verificar la conversión de algún número complejo por ejemplo 1999.
Verificar la conversión de varios valores de decimales a números romanos

## Código:
Verificar la integración entre las funciones de validar los enteros positivos y convertirlos a números romanos.



	

## 11. Utilizando el lenguaje de su preferencia cree cinco o más casos de prueba unitarios automatizados utilizando un framework de automatización de pruebas para el algoritmo en cuestión.

[repositorio](https://github.com/Farcuto/Requerimientos-Criterios-Casos)


## Bibliografia:

https://www.genbeta.com/desarrollo/que-es-un-coding-dojo
https://codingdojo.org/practices/WhatIsCodingDojo/
https://lorenzosolano.com/what-is-coding-dojo/
https://lorenzosolano.com/requirements-acceptance-criteria-and/ 
https://www.gluo.mx/blog/requisitos-no-funcionales-por-que-son-importantes 
https://www.pmoinformatica.com/2015/04/requerimientos-no-funcionales-una.html 
https://intelequia.com/es/blog/post/qu%C3%A9-es-y-para-qu%C3%A9-sirve-un-tdd-o-test-driven-development 
https://www.atlassian.com/es/continuous-delivery/software-testing/automated-testing 





