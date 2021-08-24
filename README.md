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

![Alt text](https://github.com/Paythlos/GIAResearch/blob/main/images/IV2.png)

Para la parte de procesos electroquimicos, por ahora hay una [primera documentacion por revisar](https://pubs.rsc.org/en/content/chapterhtml/2018/bk9781782625551-00001?isbn=978-1-78262-555-1&sercode=bk) donde muestran las interacciones en la superficie y su conexion con el modelo de semiconductores.

Las propiedades del TiO2 encontradas para la simulacion son:
  1. Band Gap: 2.95-3 eV [1]
  2. Nc (aun por definir bien): me* = 2.2 / me* = 0.083 [2]
  3. Nv (aun por definir bien): mh* = 0.171 [2]
  4. Epsilon = 86 perpendicular al eje optico/170 paralelo al eje optico [2][3]
  5. Movilidad de e: 0.1 - 10 cm^2/Vs [2]
  6. movilidad de h: ?? [2]
  7. Et: 0
  8. tau_e: 100 - 1000 ns [4]
  9. tau_h: 100 - 1000 ns [4]
  10. Afinidad electronica: 4.9 [4]
  11. alpha: #x10^5 
  12. Densidad de donadores: 9.2x10^18 cm^-3 [5]

Referencias para los datos de los materiales:
1.	Hossain, F. M., Sheppard, L., Nowotny, J., & Murch, G. E. (2008). Optical properties of anatase and rutile titanium dioxide: Ab initio calculations for pure and anion-doped material. Journal of Physics and Chemistry of Solids, 69(7), 1820–1828. doi: 10.1016/j.jpcs.2008.01.017
2.	Bally, A. (1999). Electronic properties of nano-crystalline titanium dioxide thin films. 2094, 140. http://biblion.epfl.ch/EPFL/theses/1999/2094/EPFL_TH2094.pdf
3.	Matweb
4.	Blanca Argentina, B. (2015). “Estudio de las propiedades del TiO 2 modificado como soporte de reacciones catalíticas” CECILIA INÉS NORA MORGADE.
5.	https://link.springer.com/content/pdf/10.1023/A:1004667631837.pdf

