import pandas as pd
import pymysql
from funciones import insert_data


path = "../house_price_madrid_14_08_2022.csv"
df = pd.read_csv(path)
df_sin_nulos = df.dropna()
id_column = list(range(1, df_sin_nulos.shape[0] + 1))
cols_groupby = ["house_type", "house_type_2", "rooms", "m2", "elevator", "garage", "neighborhood", "district"]
df_sin_nulos.loc[:, "id_inmueble"] = df_sin_nulos.groupby(cols_groupby).ngroup() + 1


#Preparar tabla inmueble
cols_inmueble=['house_type_2','rooms','m2','elevator','garage']
df_inmueble = df_sin_nulos.drop_duplicates(subset="id_inmueble")
df_inmueble = df_inmueble[cols_inmueble].copy()
df_inmueble.columns = ["exterior", "num_habitaciones", "superficie", "ascensor", "parking"]

#Preparar tabla anuncio
cols_anuncio = ["id_inmueble", "price"]
df_anuncio = df_sin_nulos[cols_anuncio].copy()
df_anuncio.columns = ["id_inmueble", "precio"]
df_anuncio["id_plataforma"] = 1
columnas_ordenadas_anuncio =  ["id_inmueble", "id_plataforma", "precio"]
df_anuncio = df_anuncio.reindex(columns = columnas_ordenadas_anuncio)

#Preparar tabla plataforma
df_plataforma = pd.DataFrame(index=[0])
df_plataforma["nombre"] = "idealista"


#Insertar datos
conn = pymysql.connect(host='localhost', user='tfm_user', password='tfmdatabase1234', db='tfm_database')
cursor = conn.cursor()
print("\n--conexion con la base de datos establecida--\n")

insert_data(df_inmueble, "inmueble", cursor)
conn.commit()
print("\n--inserción datos tabla inmueble completado--\n")

cursor = conn.cursor()
insert_data(df_plataforma, "plataforma", cursor)
conn.commit()
print("\n--inserción datos tabla plataforma completado--\n")

cursor = conn.cursor()
insert_data(df_anuncio, "anuncio", cursor)
conn.commit()
print("\n--inserción datos tabla anuncio completado--\n")
