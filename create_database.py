def create_database():
    try:
        import pymysql

    except ModuleNotFoundError:
        import pip
        pip.main(['install', 'pymysql'])
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

        cursor.execute(database_schema)
        connection.commit()


    except pymysql.OperationalError:
        print("No existe la BBDD")
