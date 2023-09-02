def etl1():
    import pandas as pd
    from unidecode import unidecode
    import pymysql
    from funciones import insert_data, change_values

    df = pd.read_csv("../tfm_datos/houses_Madrid.csv", index_col="Unnamed: 0")

    orientation_df = df[["id", "is_orientation_north", "is_orientation_west", "is_orientation_south", "is_orientation_east"]].fillna(False)
    orientation_df = orientation_df.melt("id",[ "is_orientation_north", "is_orientation_west", "is_orientation_south", "is_orientation_east"], var_name="orientation", value_name="value")
    max_orientation_df = orientation_df.groupby("id")["value"].idxmax()
    orientation_df = orientation_df.loc[max_orientation_df].drop("value", axis=1)
    df_tmp = df.melt("id", ["rent_price", "buy_price"], "tipo", "price")
    df = df.merge(df_tmp, on="id", how="inner")
    df.drop(["rent_price", "buy_price"], inplace=True, axis=1)
    df = df.merge(orientation_df, on="id", how="inner")
    df.dropna(subset=["house_type_id", "sq_mt_built"], inplace=True)
    cols_inmueble = [["tipo_propiedad", "superficie", "exterior", "num_habitaciones", "num_lavabos", "descripcion", "has_lift","has_parking", "has_terrace", "has_pool", "has_balcony", "certificado_energetico", "piso", "orientacion", "id_direccion"], 
                    ["tipo_propiedad", "superficie", "exterior", "num_habitaciones", "num_lavabos", "descripcion", "ascensor","parking", "terraza", "piscina", "balcon", "certificado_energetico", "piso", "orientacion", "id_direccion"]]
    cols_direccion = [["distrito", "subdistrito"], 
                    ["distrito", "subdistrito"]]
    cols_anuncio = [["id_inmueble", "id_plataforma", "price", "tipo"], 
                    ["id_inmueble", "id_plataforma", "precio", "tipo"]]
    df = df[df.price >= 400]



    ############################## DIRECCION ##############################

    df_distrito = df.neighborhood_id.str.split(":", expand=True)
    df_distrito = df_distrito[df_distrito.columns[1:]]
    df_distrito.columns = ["subdistrito", "distrito"]
    df_distrito.subdistrito = df_distrito.subdistrito.str.split("(").str[0]
    df_distrito.subdistrito = df_distrito.subdistrito.str.lower().str.strip()
    df_distrito.subdistrito = df_distrito.subdistrito.apply(lambda x: unidecode(x))
    df_distrito.distrito = df_distrito.distrito.str.lower().str.strip()
    df_distrito.distrito = df_distrito.distrito.apply(lambda x: unidecode(x))
    df.drop("neighborhood_id", axis=1, inplace=True)
    df = df.join(df_distrito)
    df_direccion = df[cols_direccion[0]]
    df_direccion.columns = cols_direccion[1]
    df_direccion["ciudad"] = "madrid"
    df_direccion.drop_duplicates(inplace=True)
    url = '../tfm_datos/CALLEJERO_VIGENTE_NUMERACIONES_202305.csv'
    df_zip_codes = pd.read_csv(url, sep=';', encoding='latin-1')
    df_zip_codes = df_zip_codes[["Nombre del distrito", "Nombre del barrio", "Codigo postal"]]
    df_zip_codes['Nombre del distrito'] = df_zip_codes['Nombre del distrito'].str.lower().str.strip()
    df_zip_codes['Nombre del barrio'] = df_zip_codes['Nombre del barrio'].str.lower().str.strip()
    df_zip_codes["Nombre del distrito"] = df_zip_codes["Nombre del distrito"].apply(lambda x: unidecode(x))
    df_zip_codes["Nombre del barrio"] = df_zip_codes["Nombre del barrio"].apply(lambda x: unidecode(x))
    df_zip_codes.columns = ["distrito", "subdistrito", "codigo_postal"]
    df_zip_codes.distrito = df_zip_codes.distrito.str.split("-").str[0]
    df_direccion = change_values(df_direccion)
    df_direccion = df_direccion.merge(df_zip_codes[["distrito", "subdistrito", "codigo_postal"]], on=["distrito", "subdistrito"], how="left")
    df_direccion.dropna(inplace=True)
    df_direccion.drop_duplicates(inplace=True)
    df_direccion["id_direccion"] = range(1,df_direccion.shape[0]+1)
    path2 = "../tfm_datos/03_SuperficieZonasVerdesDistritosCalles_2022.csv"
    df_zonasverdes = pd.read_csv(path2, sep=";")
    df_zonasverdes.dropna(inplace=True)
    df_zonasverdes.columns = ["num_distrito", "distrito", "m2_zonasverdes", "ha_zonasverdes"]
    df_zonasverdes.distrito = df_zonasverdes.distrito.apply(lambda x: unidecode(x)).str.lower()
    df_zonasverdes.distrito = df_zonasverdes.distrito.str.split("-").str[0].str.strip()
    df_zonasverdes.ha_zonasverdes = df_zonasverdes["ha_zonasverdes"].str.replace(",", ".").astype(float)

    df_direccion = df_direccion.merge(df_zonasverdes[["distrito", "ha_zonasverdes"]], on="distrito", how="left")



    ############################## INMUEBLE ##############################

    df = change_values(df)
    df = df.merge(df_direccion[['distrito', 'subdistrito', 'id_direccion']], on=['distrito', 'subdistrito'], how="left")
    df.fillna(False, inplace=True)
    df["tipo_propiedad"] = df.house_type_id.str.split(":").str[-1]
    df["tipo_propiedad"] = df.tipo_propiedad.apply(lambda x: unidecode(x)).str.lower().str.strip()
    df["orientacion"] = df.orientation.str.split("_").str[-1]
    translation_map = {'west': 'oeste', 'east': 'este', 'north': 'norte', 'south': 'sur'}
    df['orientacion'] = df.orientacion.replace(translation_map)
    df["superficie"] = df.sq_mt_built.astype(int)
    df["num_lavabos"] = df.n_bathrooms.astype(int)
    df["num_habitaciones"] = df.n_rooms.astype(int)
    df["exterior"] = df.is_exterior.fillna(False)
    df["certificado_energetico"] = df.energy_certificate.apply(lambda x: unidecode(x)).str.lower().str.strip()
    df["descripcion"] = df.title.apply(lambda x: unidecode(x)).str.lower().str.strip()
    df["piso"] = df.floor.str.lower().replace({"bajo":"0", ".*sótano.*":"0"}, regex=True)
    df["piso"] = pd.to_numeric(df.piso, errors='coerce')
    df_inmueble = df[cols_inmueble[0]]
    df_inmueble.columns = cols_inmueble[1]
    df_inmueble.dropna(inplace=True)
    df_inmueble["piso"] = df_inmueble.piso.astype(int)
    df_inmueble.drop_duplicates(inplace=True)
    df_inmueble["id_inmueble"] = range(1, df_inmueble.shape[0]+1)
    df_inmueble["exterior"] = df_inmueble.exterior.astype(int)
    df_inmueble["ascensor"] = df_inmueble.ascensor.astype(int)
    df_inmueble["terraza"] = df_inmueble.terraza.astype(int)
    df_inmueble["parking"] = df_inmueble.parking.astype(int)
    df_inmueble["piscina"] = df_inmueble.piscina.astype(int)
    df_inmueble["balcon"] = df_inmueble.balcon.astype(int)



    ############################## PLATAFORMA ##############################

    df["id_plataforma"] = 1
    df_plataforma = pd.DataFrame({"id_plataforma": [1],"nombre": ["idealista"], "num_inmuebles": [df_inmueble.shape[0]]})



    ############################## ANUNCIO ##############################

    df_inmueble2 = df_inmueble
    cols = df_inmueble2.columns[df_inmueble2.dtypes == bool]
    df_inmueble2[cols] = df_inmueble2[cols].astype(str)
    df.rename(columns={'has_lift': 'ascensor', "has_parking":"parking", "has_terrace":"terraza", "has_pool":"piscina", "has_balcony":"balcon"}, inplace=True)
    df[cols] = df[cols].astype(str)
    df = df.merge(df_inmueble2, 
        on=['tipo_propiedad', 'superficie', 'num_habitaciones',
        'num_lavabos', 'descripcion', 'ascensor', 'parking', 'terraza',
        'piscina', 'balcon', 'certificado_energetico', 'piso', 'orientacion',
        'exterior', 'id_direccion'], 
        how="left")
    df.dropna(subset=["id_inmueble"], inplace=True)
    df_anuncio = df[cols_anuncio[0]]
    df_anuncio.columns = cols_anuncio[1]
    df_anuncio["id_inmueble"] = df_anuncio.id_inmueble.astype(int)
    df_anuncio.tipo = df_anuncio.tipo.str.split("_").str[0]
    translation_map = {'rent': 'alquiler', 'buy': 'compra'}
    df_anuncio['tipo'] = df_anuncio['tipo'].replace(translation_map)
    df_anuncio["id_anuncio"] = range(1, df_anuncio.shape[0]+1)


    ############################## INSERT DATA ##############################
    conn = pymysql.connect(host='localhost', user='tfm_user', password='tfmdatabase1234', db='tfm_database')
    cursor = conn.cursor()
    print("\n--conexion con la base de datos establecida--\n")
    cursor = conn.cursor()
    insert_data(df_direccion, "direccion", cursor)
    conn.commit()
    print("\n--inserción datos tabla direccion completado--\n")
    cursor = conn.cursor()
    insert_data(df_plataforma, "plataforma", cursor)
    conn.commit()
    print("\n--inserción datos tabla plataforma completado--\n")
    insert_data(df_inmueble, "inmueble", cursor)
    conn.commit()
    print("\n--inserción datos tabla inmueble completado--\n")
    cursor = conn.cursor()
    insert_data(df_anuncio, "anuncio", cursor)
    conn.commit()
    print("\n--inserción datos tabla anuncio completado--\n")