try:
    import pymysql
except ModuleNotFoundError:
    print(\"pymysql module not found. Installing...\")
    !pip install pymysql
    import pymysql

host = 'localhost'
user = 'tfm_user'
password = 'tfmdatabase1234'
database = 'tfm_database2'

connection = pymysql.connect(host=host, user=user, password=password)
schema = 
        """CREATE TABLE IF NOT EXISTS employees (,
            id INT AUTO_INCREMENT PRIMARY KEY,,
            name VARCHAR(100),",
            age INT,",
            salary FLOAT");"""

try:
    connection.select_db(database)
    cursor = connection.cursor()
    cursor.execute(schema)

except pymysql.OperationalError:
    print("No existe la BBDD")