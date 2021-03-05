# GIAResearch
Interaccion radiacion-materia entre luz UV-Visible proveniente del sol y un anodo de una celda fotoelectroquimica, buscando simular los efectos del semiconductor donde una curva I-V es deseada, luego usando estos voltajes generados en un modelo de una celda electroquimica se determinara la generacion de especies oxigeno-activas. Por el momento se usa el paquete de sesame para simular parte de la interaccion radiacion-semiconductor, proximamente se introducira la parte electroquimica.

## Modulo de modelacion de semiconductores
El paquete que se usara es el de [Sesame](https://sesame.readthedocs.io/en/latest/) el cual se basara en el modelo de [homounion pn en 1-dimension](https://sesame.readthedocs.io/en/latest/tutorial/tuto1.html). Las propiedades del material necesarias son las siguientes:

  1. Nc: Densidad de estados efectiva en la banda de conduccion (cm^-3)
  2. Nv: Densidad de estados efectiva en la banda de valencia (cm^-3)
  3. Eg: Bandgap del material (eV)
  4. epsilon: Constante dielectrica del material 
  5. mu_e: movilidad de electrones (cm^2/V s)
  6. mu_h: movilidad de huecos (cm^2/V s)
  7. Et: Nivel energetico de recombinacion de defectos en el bulk, medido como el nivel intrinseco
  8. tau_e: Tiempo de vida de los electrones en el bulk
  9. tau_h: Tiempo de vida de los huecos en el bulk
  10. affinity: Afinidad electronica (eV)

El codigo generara unos archivos .gzip que son los que contienen los datos numericos de la simulacion, estos se pueden cargar para generar diferentes resultados como la bandas de energias. Con esto se simula el material semiconductor, para generar las curvas I-V:

![Alt text](https://github.com/Paythlos/GIAResearch/blob/main/images/IV.png)

Para la parte de procesos electroquimicos, por ahora hay una [primera documentacion por revisar](https://pubs.rsc.org/en/content/chapterhtml/2018/bk9781782625551-00001?isbn=978-1-78262-555-1&sercode=bk) donde muestran las interacciones en la superficie y su conexion con el modelo de semiconductores
