def create_database():
    import pymysql

    host = 'localhost'
    user = 'tfm_user'
    password = 'tfmdatabase1234'
    database = 'tfm_database'

    connection = pymysql.connect(host=host, user=user, password=password)

    try:
        connection.select_db(database)
        cursor = connection.cursor()

        with open('database_schema.sql', 'r') as schema:
            database_schema = schema.read()
        
        database_schema = database_schema.replace('\n', '').split(';')[:-1]
        for sql_command in database_schema:
            cursor.execute(sql_command)
            connection.commit()

        print("\n--Base de datos creada correctamente--")
    except pymysql.OperationalError:
        print("\n--No existe la Base de datos--")