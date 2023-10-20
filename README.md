# Posicionamiento Satelital
Notas de software de las clases de Posicionamiento Satelital de la Maestría en Geomática de la UNLP

## Software

* Hatanaka Decomprensor ejecutado desde python
* ``` pip install hatanaka ```
* ``` pip install pytest```
* ```pytest --pyargs hatanaka ```

en la consola ```python hatanakaDecompress.py ```

* teqc https://www.unavco.org/software/data-processing/teqc/teqc.html#support
Ejemplo del uso de teqc ( tener en cuenta que se ejecuta desde donde esta el archivo descargado)
En consola ejecutar ```teqc -st 00:00:00 +dh 2 tgta2740.23o > tgta2740_2.23o ``` ahi le dividi de 0 a 2 horas
