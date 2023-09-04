def insert_data(df, table_name, cursor):
    cursor.execute("SET TRANSACTION ISOLATION LEVEL READ COMMITTED")

    cols = ", ".join(df.columns)
    update_columns = [f"{col} = VALUES({col})" for col in df.columns]
    update_clause = ", ".join(update_columns)
    insert_query = f"INSERT INTO {table_name} ({cols}) VALUES ({', '.join(['%s'] * len(df.columns))}) ON DUPLICATE KEY UPDATE {update_clause}"

    batch_size = 1000  # Number of rows per batch
    values = [tuple(row) for row in df.values]

    # Insert the DataFrame rows into the MySQL table in batches
    for i in range(0, len(values), batch_size):
        batch = values[i:i+batch_size]
        cursor.executemany(insert_query, batch)

def get_latest_id(cursor, table_name, id_column):
    query = f"SELECT MAX({id_column}) AS last_id FROM {table_name};"
    res = cursor.execute(query)
    return res

def change_values(dataframe):
    dataframe.loc[dataframe["subdistrito"] == "casco historico de barajas", "subdistrito"] = "casco h.barajas"
    dataframe.loc[dataframe["subdistrito"] == "campo de las naciones-corralejos", "subdistrito"] = "corralejos"
    dataframe.loc[dataframe["subdistrito"] == "buena vista", "subdistrito"] = "buenavista"
    dataframe.loc[dataframe["subdistrito"] == "palos de moguer", "subdistrito"] = "palos de la frontera"
    dataframe.loc[dataframe["subdistrito"] == "chueca-justicia", "subdistrito"] = "justicia"
    dataframe.loc[dataframe["subdistrito"] == "malasana-universidad", "subdistrito"] = "universidad"
    dataframe.loc[dataframe["subdistrito"] == "huertas-cortes", "subdistrito"] = "cortes"
    dataframe.loc[dataframe["subdistrito"] == "lavapies-embajadores", "subdistrito"] = "embajadores"
    dataframe.loc[dataframe["subdistrito"] == "bernabeu-hispanoamerica", "subdistrito"] = "hispanoamerica"
    dataframe.loc[dataframe["subdistrito"] == "nuevos ministerios-rios rosas", "subdistrito"] = "rios rosas"
    dataframe.loc[dataframe["subdistrito"] == "pilar", "subdistrito"] = "el pilar"
    dataframe.loc[dataframe["subdistrito"] == "penagrande", "subdistrito"] = "pena grande"
    dataframe.loc[dataframe["subdistrito"] == "tres olivos - valverde", "subdistrito"] = "valverde"
    dataframe.loc[dataframe["subdistrito"] == "sanchinarro", "subdistrito"] = "pinar del rey"
    dataframe.loc[dataframe["subdistrito"] == "valdebebas - valdefuentes", "subdistrito"] = "valdefuentes"
    dataframe.loc[dataframe["subdistrito"] == "conde orgaz-piovera", "subdistrito"] = "piovera"
    dataframe.loc[dataframe["subdistrito"] == "penagrande", "subdistrito"] = "pena grande"
    dataframe.loc[dataframe["subdistrito"] == "aguilas", "subdistrito"] = "las aguilas"
    dataframe.loc[dataframe["subdistrito"] == "jeronimos", "subdistrito"] = "los jeronimos"
    dataframe.loc[dataframe["subdistrito"] == "cuzco-castillejos", "subdistrito"] = "castillejos"
    dataframe.loc[dataframe["subdistrito"] == "ventilla-almenara", "subdistrito"] = "almenara"
    dataframe.loc[dataframe["subdistrito"] == "12 de octubre-orcasur", "subdistrito"] = "orcasur"
    dataframe.loc[dataframe["subdistrito"] == "el canaveral - los berrocales", "subdistrito"] = "el canaveral"
    dataframe.loc[dataframe["subdistrito"] == "casco historico de vicalvaro", "subdistrito"] = "casco h.vicalvaro"
    dataframe.loc[dataframe["subdistrito"] == "valdebernardo - valderribas", "subdistrito"] = "valderrivas"
    dataframe.loc[dataframe["subdistrito"] == "ensanche de vallecas - la gavia", "subdistrito"] = "ensanche de vallecas"
    dataframe.loc[dataframe["subdistrito"] == "casco historico de vallecas", "subdistrito"] = "casco h.vallecas"
    dataframe.loc[dataframe["subdistrito"] == "virgen del cortijo - manoteras", "subdistrito"] = "pinar del rey"
    dataframe.loc[dataframe["subdistrito"] == "san andres", "subdistrito"] = "villaverde alto c.h."
    dataframe.loc[dataframe["subdistrito"] == "ambroz", "subdistrito"] = "casco h.vicalvaro"
    dataframe.loc[dataframe["subdistrito"] == "montecarmelo", "subdistrito"] = "valverde"
    dataframe.loc[dataframe["subdistrito"] == "arroyo del fresno", "subdistrito"] = "mirasierra"
    dataframe.loc[dataframe["subdistrito"] == "pau de carabanchel", "subdistrito"] = "buenavista"
    dataframe.loc[dataframe["subdistrito"] == "las tablas", "subdistrito"] = "valverde"

    
    return dataframe

def prepare_datasets(X, y):
    from sklearn.preprocessing import MinMaxScaler
    from sklearn.model_selection import train_test_split

    scaler_x = MinMaxScaler()
    X_scale = scaler_x.fit_transform(X)

    scaler_y = MinMaxScaler()
    y_scale = scaler_y.fit_transform(y)
    X_train, X_test, y_train, y_test = train_test_split(X_scale, y_scale, test_size=0.3)

    return scaler_x, scaler_y, X_train, X_test, y_train, y_test