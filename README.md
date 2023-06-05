# TFM EAE

### requirements.txt 
    - paquetes necesarios para ejecutar el código correctamente.

### main.py 
    - código Python que ejecuta todas las operaciones necesarias para crear la base de datos

### create_database.py 
    - código Python que se conecta a la base de datos de MySQL y ejecuta database_schema.sql

### database_schema.sql
    - código SQL que permite crear las tablas en la base de datos (esquema de la base de datos)

### etl1.py
    - código python que mediante pandas lee el archivo house_price_madrid_14_08_2022.csv y transforma la información en el formato de las tablas de la base de datos para ser
      insertado en sus respectivas tablas.

### funciones.py
    - código repetido de Python encapsulado en funciones para ser ejecutado por las ETL
      
### install_spark.py
    - código Python que descarga la distribución de spark 3.4.0, la descomprime, y realiza
      los cambios en el sistema necesarios para configurar spark, y con ello poder ejecutar
      pyspark.
